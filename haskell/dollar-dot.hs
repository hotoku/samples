f :: Int -> Int
f = (+) 2

g :: Int -> Int
g = (*) 3

printIt :: (Show a) => a -> IO ()
printIt a = putStrLn $ show a

x :: Int
-- これはエラー
-- x = f f f g g g 2
x = f ( f ( f (g ( g ( g 2)))))


y :: Int
-- 最後の$がないと`g . (g 2)`となって型が合わないことに注意
y = f . f . f . g . g . g $ 2


z :: Int
-- これでもOK
z = f $ f $ f $ g $ g $ g $ 2 






main :: IO ()
main = do
  printIt $ f 2
  printIt $ g 2
  printIt x
  printIt y
  printIt z
