const expect = require('expect');
const utils = require('./utils');


describe('test of util', () => {
  describe('add', () => {
    it('should add two numbers', () => {
      const ret = utils.add(1, 2);
      expect(ret).toEqual(3)
    })
  })
  describe('square', () => {
    it('should square a number', () => {
      const ret = utils.square(3)
      expect(ret).toEqual(9)
    })
  })
})
