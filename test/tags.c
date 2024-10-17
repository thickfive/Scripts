HEAD detached at detached-tag-20241017
Revert currently in progress.
  (run "git revert --continue" to continue)
  (use "git revert --skip" to skip this patch)
  (use "git revert --abort" to cancel the revert operation)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test/tags.c

nothing added to commit but untracked files present (use "git add" to track)

// 删除 tag
git tag -d detached-tag-20241017
// 推送到远端
git push origin :refs/tags/detached-tag-20241017