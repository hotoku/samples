(defun f1 (x)
  (1+ x))

(defun f2 (x)
  (f1 x))

(defun f3 (x)
  (f2 x))

(defun f4 (x)
  (let* ((x1 x)
         (x2 (f3 x1))
         (x3 (f3 x2)))
    x3))

;; Local Variables:
;; flycheck-disabled-checkers: emacs-lisp-checkdoc
;; End:
