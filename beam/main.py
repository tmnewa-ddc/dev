import json
import logging

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions
from apache_beam.runners.interactive.display import pipeline_graph


class PrintFn(beam.DoFn):
    """Prints information"""
    def process(self, element, name='', fmt=False):
        if name:
            print(f'------{name}------')
        pResult = element
        if fmt and type(element) == dict:
            pResult = 'json:' + json.dumps(element, indent=2)
        print(pResult)
        yield element


class MemberName():
    __data = {
        '001': ('Sabrina', True),
        '002': ('Emily', True),
        '003': ('Joan', True),
        '004': ('Chris', True),
        '005': ('Freddy', True),
        '006': ('Yvone', True),
        '007': ('Wens', True),
        '008': ('Jenny', True),
        '009': ('Stephanie', True),
        '010': ('Ken', True),
        '011': ('Terry', False)
    }

    @classmethod
    def queryStay(cls, id):
        result = cls.__data.get(id, ('', False))
        return result[0] if result[1] else ''


class MemberRole():
    __data = {
        'Loc_1': ['001'],
        'Loc_2': ['003', '004'],
        'Loc_3': ['002', '005', '006', '007', '008', '009', '010'],
        'Job_pm': ['001', '003', '006'],
        'Job_rd': ['004', '005', '007', '008'],
        'Job_data': ['002', '010'],
        'Job_art': ['009'],
        'Job_mis': ['011']
    }

    @classmethod
    def queryCate(cls, id, cate):
        for i, j in cls.__data.items():
            if id in j and cate and i.startswith(cate):
                return i.replace(cate+'_', '')
        return ''


class SpRoleFn(beam.DoFn):
    def process(self, element):
        locs = {}
        for i in element:
            loc = MemberRole.queryCate(i, 'Loc') or '-'
            if loc not in locs:
                locs[loc] = {}
            locs[loc][i] = MemberRole.queryCate(i, 'Job') or '-'
        for loc, jobs in locs.items():
            yield (loc, jobs)


class FmtRoleFn(beam.DoFn):
    def process(self, element):
        yield {
            'loc': element[0],
            'member': element[1]
        }


class MemberInfoFn(beam.DoFn):
    def process(self, element):
        static = {}
        members = {}
        locs = []
        for i in element[1]['name']:
            members.update(i)
        static['total'] = len(members)
        for i in element[1]['role']:
            loc = {
                'locate': i['loc'], 'member': {}, 'static': {'total': 0}
            }
            for id, job in i['member'].items():
                if job not in static:
                    static[job] = 0
                if id not in members:
                    continue
                static[job] += 1
                loc['static']['total'] += 1
                if job not in loc['static']:
                    loc['static'][job] = 0
                loc['static'][job] += 1
                loc['member'][id] = (members[id], job)
            locs.append(loc)
        for loc in sorted(locs, key=lambda d: d['locate'] if (d['locate']) != '-' else 'zzz'):
            yield {
                **loc,
                'static': {
                    c: f'{v}/{static[c]}' for c, v in loc['static'].items()
                }
            }


def setLocs(values):
    locs = {}
    for i in values:
        locs.update(i)
    return locs


def getMemberInfo(show_graph=False):
    """beam intro:
    ({Pipeline/PCollection} | {Label Text} >> {PTransform} | ...) -> {PCollection}
    """
    pipeline_options = PipelineOptions().view_as(SetupOptions)
    with beam.Pipeline(options=pipeline_options) as p:
        c1 = p | 'Get Dept' >> beam.Create([
            ['001'],
            ['002', '003', '006', '009'],
            ['004', '005', '007', '008', '010', '011'],
        ])
        procName = (
            c1
            | 'Get Name' >> beam.Map(lambda x: {i: n for i in x if (n := MemberName.queryStay(i))})
            | 'Combine Member' >> beam.CombineGlobally(lambda s: dict(i for m in s for i in m.items()))
            | 'Show Name' >> beam.ParDo(PrintFn(), name='Name')
            | 'NameSet' >> beam.Map(lambda x: ('-', x))
        )
        procRole = (
            c1
            | 'Get Role' >> beam.ParDo(SpRoleFn())
            | 'Combine Role' >> beam.CombinePerKey(setLocs)
            | 'Format Role' >> beam.ParDo(FmtRoleFn())
            | 'Show Role' >> beam.ParDo(PrintFn(), name='Role')
            | 'RoleSet' >> beam.Map(lambda x: ('-', x))
        )
        (
            ({'name': procName, 'role': procRole})
            | 'Merge' >> beam.CoGroupByKey()
            | 'Show Raw' >> beam.ParDo(PrintFn(), name='Merge Raw')
            | 'Member Info' >> beam.ParDo(MemberInfoFn())
            | 'Show Info' >> beam.ParDo(PrintFn(), name='Merge Info', fmt=True)
        )
        if show_graph:
            print('graph:\n')
            print(pipeline_graph.PipelineGraph(p).get_dot())


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    getMemberInfo()
