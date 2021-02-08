data MyMaybe a = MyNothing | MyJust a

instance Functor MyMaybe where
  fmap _ MyNothing = MyNothing
  fmap f (MyJust x) = MyJust (f x)

instance Applicative MyMaybe where
  pure x = MyJust x
  MyNothing <*> _ = MyNothing
  (MyJust f) <*> x = fmap f x

instance Monad MyMaybe where
  return x = MyJust x
  MyNothing >>= _ = MyNothing
  MyJust x >>= f = f x

instance (Show a) => Show (MyMaybe a) where
  show MyNothing = "Nothing"
  show (MyJust x) = show x

div2::Int -> MyMaybe Int
div2 x 
  | mod x 2 == 0 = MyJust (div x 2)
  | otherwise = MyNothing

maybePlus1::Int -> MyMaybe Int
maybePlus1 x = MyJust $ (+1) x

value::MyMaybe Int
value = MyJust 101 >>= \x ->
  div2 x >>= \y ->
  maybePlus1 y

value2::MyMaybe Int
value2 = do
  x <- MyJust 100
  y <- div2 x
  maybePlus1 y

main :: IO()
main = do
  putStrLn $ show value
  putStrLn $ show value2
