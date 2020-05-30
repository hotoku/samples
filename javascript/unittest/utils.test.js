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
  describe('reference', () => {
    it('should be same value but different reference', () => {
      const v1 = {
        x: 1
      }
      const v2 = {
        x: 1
      }
      expect(v1).toEqual(v2)
      expect(v1).not.toBe(v2)
    })
  })
)}
