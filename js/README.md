# JavaScript test coverage with Istanbul

https://istanbul.js.org/

## Run the tests without coverage
```
mocha
```

or
```
npm start
```
after adding mocha in `package.json`



## Adding the coverage
```
npm install -g nyc
nyc mocha
```


```
nyc report
```

```
----------|----------|----------|----------|----------|-------------------|
File      |  % Stmts | % Branch |  % Funcs |  % Lines | Uncovered Line #s |
----------|----------|----------|----------|----------|-------------------|
All files |    77.78 |      100 |    33.33 |    77.78 |                   |
 a.js     |    83.33 |      100 |       50 |    83.33 |                 6 |
 b.js     |    66.67 |      100 |        0 |    66.67 |                 2 |
----------|----------|----------|----------|----------|-------------------|
```


```
nyc report --reporter=lcov
```
Generates lcov.info and folder containing HTML report in lcov-report/
