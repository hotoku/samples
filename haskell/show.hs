data MyMaybe a = MyNothing | MyJust a

instance (Show a) => Show (MyMaybe a) where
  show (MyJust x) = show x
  show MyNothing = "Nothing"

main :: IO()
main = do
  putStrLn $ show $ MyJust 100
  putStrLn $ show $ (MyNothing::MyMaybe Int)
