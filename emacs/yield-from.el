;; -*- lexical-binding: t -*-

(require 'generator)

(iter-defun hotoku-generator ()
  (let ((n 0))
    (while (< n 3)
      (iter-yield n)
      (setq n (1+ n))))
  (iter-yield nil))

(iter-defun hotoku-generator-2 ()
  (let ((g (hotoku-generator)))
    (while t (iter-yield-from g))))

(let* ((g (hotoku-generator-2))
       (v nil))
  (while (setq v (iter-next g))
    (message (number-to-string v))))

;; Local Variables:
;; flycheck-disabled-checkers: (emacs-lisp-checkdoc)
;; End:
