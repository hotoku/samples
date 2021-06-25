(defun display-prefix (arg)
  "Display ARG"
  (interactive "P")
  (message "%s" arg))
;; M-x display-prefix => (nil)
;; C-u M-x display-prefix => (4)
