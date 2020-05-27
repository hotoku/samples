const expect = require('expect');
const sample = require("../dist/sample")


describe('test of sample', () => {
  describe('b', () => {
    it('should return (x+1)*200', () => {
      const x = 1
      const ret = sample.b(x)
      expect(ret).toEqual(200*(x+1))
    })
  })
})
