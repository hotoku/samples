a = [
  {
    x: 1
  },
  {
    x: 3
  },
  {
    x: 2
  }
]

console.log(a)

a.sort((o1, o2) => {
  if(o1.x < o2.x) return -1
  if(o2.x > o1.x) return 1
  return 0
})

console.log(a)

