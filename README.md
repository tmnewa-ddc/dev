Git Dev Test
===

目前的開發流程跟分支

## Commit

每個節點都應該是可完整使用的階段，過程可以透過如下技巧完善節點

*   stash：暫存變更
*   rebase i：修改歷程
*   reset soft：重置節點

### Main Branch (don't modify)

*   develop：開發分支，整合rd各分支用
*   beta/test：測試分支，外部測試用
*   master/main：產品分支，正式上線用

### Developer Open New Branch Rules

*   {fix, feature}/*：針對較明確的小規模任務使用
*   dev/*：副開發分支，當功能較龐大時獨立使用
*   hotfix/*：緊急修正分支，通常會開在產品分支上
*   bug/*：臭蟲分支，修正線上發現的問題使用

## Git hooks tools

透過 pre-commit 綁定提交前的檢查測試，確保程式碼無錯

go to [pre-commit](https://pre-commit.com) and [default-hooks](https://github.com/pre-commit/pre-commit-hooks)

```
$ brew install pre-commit
$ pre-commit install -f --install-hooks
$ pre-commit run
```

see: [DDC pre-commit]

## Cloud Build

go to [README_CloudBuild.md](docs/README_CloudBuild.md)

## Kubernetes Engine

go to [README_GKE.md](docs/README_GKE.md)


[DDC pre-commit]: https://github.com/tmnewa-ddc/pre-commit