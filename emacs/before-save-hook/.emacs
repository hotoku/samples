(defun hoge () (message "hoge"))
(add-hook 'before-save-hook 'hoge)

(add-to-list 'load-path "/Users/hotoku/project/hotoku-dot-emacs/el-get/py-autopep8")
(require 'py-autopep8)
(add-hook 'python-mode-hook 'py-autopep8-enable-on-save)
