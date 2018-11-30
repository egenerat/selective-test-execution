const assert = require('assert');
const a = require('../src/a.js');
const b = require('../src/b.js');

describe('a.js', () => {
  describe('#sayHello()', () => {
    it('should return "Hello"', () => {
      assert.equal(a.getHello(), "Hello");
    });
  });
});
