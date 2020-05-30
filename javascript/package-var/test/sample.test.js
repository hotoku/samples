const expect = require('expect');
const sample = require("../dist/sample")


describe('test of util', () => {
  describe('b', () => {
    it('should return a:b', () => {
      const ret = sample.b()
      expect(ret).toEqual('a:b')
    })
  })
})
