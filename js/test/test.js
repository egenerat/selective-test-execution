const assert = require('assert');
const a = require('../src/a.js');
const b = require('../src/b.js');

describe('a.js', () => {
  describe('#getHello()', () => {
    it('should return "Hello"', () => {
      assert.equal(a.getHello(), "Hello");
    });
  });
});

describe('b.js', () => {
  describe('#getResult()', () => {
    it('should return 1', () => {
      assert.equal(b.getResult(), 1);
    });
  });
});
