(defmacro mymacro1 (x)
  `(+ ,x 1))


(defmacro mymacro2 (x)
  `(mymacro1 ,x))


(mymacro2 10) ;; => 11
