{-# LANGUAGE TypeSynonymInstances #-}
{-# LANGUAGE FlexibleInstances #-}


newtype Parser a = Parser (String -> [(a, String)])

parse (Parser p) = p

instance Functor Parser where
  -- fmap :: (a -> b) -> m a -> m b
  fmap f (Parser p) = Parser (\cs -> [(f x, cs') | (x, cs') <- p cs])

instance Applicative Parser where
  -- pure :: a -> m a
  pure x = Parser (\cs -> [(x, cs)])
  -- (<*>) :: m (a -> b) -> m a -> m b
  (Parser p) <*> x = fmap p x
  
instance Monad Parser where
  return x = Parser (\cs -> [(x, cs)])
  p >>= f = Parser (\cs -> concat [parse (f a) cs' | (a, cs') <- parse p cs])



main :: IO ()
main = do
  putStrLn "1"
