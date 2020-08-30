;; -*- lexical-binding: t -*-

(require 'generator)

(iter-defun hotoku-generator ()
  (let ((n 0))
    (while (< n 3)
      (iter-yield n)
      (setq n (1+ n))))
  (iter-yield nil))

(let* ((g (hotoku-generator))
       (v (iter-next g)))
  (while v
    (message (number-to-string v))
    (setq v (iter-next g))))

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; End:
