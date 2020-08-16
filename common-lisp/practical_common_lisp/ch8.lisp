;;;; 与えられた範囲の素数に対する処理を行うマクロを書く

(defun primep (num)
  (when (> num 1)
    (loop for fac from 2 to (isqrt num) never (zerop (mod num fac)))))

(defun next-prime (num)
  (loop for n from num when (primep n) return n))

;;; endがループの終了判定のたびに評価される
(defmacro do-primes ((var start end) &body body)
  `(do ((,var (next-prime ,start) (next-prime (1+ ,var))))
       ((> ,var ,end))
     ,@body))

;;; end-valueという変数名が、実行時にvarの値と被ったり、環境の中の変数名とバッティングする可能性がある
(defmacro do-primes2 ((var start end) &body body)
  `(do ((,var (next-prime ,start) (next-prime (1+ ,var)))
        (end-value ,end))
       ((> ,var end-value))
     ,@body))

;;; gensymという関数で、安全に一時的な名前を作れる
(defmacro do-primes3 ((var start end) &body body)
  (let ((end-value (gensym)))
    `(do ((,var (next-prime ,start) (next-prime (1+ ,var)))
          (,end-value ,end))
         ((> ,var ,end-value))
       ,@body)))
