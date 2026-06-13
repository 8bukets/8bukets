# Knowledge Observation Insights (Unified)

**System Analysis:** 2026-06-13T06:32:47.746Z

---

# iCloud: web-app/node_modules/@typescript-eslint/type-utils/node_modules/balanced-match/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/type-utils/node_modules/balanced-match/README.md
> **Analyzed At:** 2026-06-13T06:32:46.214Z

## balanced-match
``. Supports regular expressions as well!

## Example
Get the first matching pair of braces:
```js
import { balanced } from 'balanced-match'

console.log(balanced('{', '}', 'pre{in{nested}}post'))
console.log(balanced('{', '}', 'pre{first}between{second}post'))
console.log(
  balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'),
)
```
The matches are:
```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## const m = balanced(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:
- **start** the index of the first match of `a`
- **end** the index of the matching `b`
- **pre** the preamble, `a` and `b` not included
- **body** the match, `a` and `b` not included
- **post** the postscript, `a` and `b` not included
If there's no match, `undefined` will be returned.

## const r = balanced.range(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ ,  ]`.
If there's no match, `undefined` will be returned.

---

# iCloud: web-app/node_modules/@typescript-eslint/type-utils/node_modules/@typescript-eslint/utils/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/type-utils/node_modules/@typescript-eslint/utils/README.md
> **Analyzed At:** 2026-06-13T06:32:46.214Z

## `@typescript-eslint/utils`
> Utilities for working with TypeScript + ESLint together.
[![NPM Version](https://img.shields.io/npm/v/@typescript-eslint/utils.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/utils)
[![NPM Downloads](https://img.shields.io/npm/dm/@typescript-eslint/utils.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/utils)
👉 See **https://typescript-eslint.io/packages/utils** for documentation on this package.
> See https://typescript-eslint.io for general documentation on typescript-eslint, the tooling that allows you to run ESLint and Prettier on TypeScript code.

---

# iCloud: web-app/node_modules/@typescript-eslint/parser/node_modules/@typescript-eslint/typescript-estree/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/parser/node_modules/@typescript-eslint/typescript-estree/README.md
> **Analyzed At:** 2026-06-13T06:32:46.231Z

## `@typescript-eslint/typescript-estree`
> A parser that produces an ESTree-compatible AST for TypeScript code.
[![NPM Version](https://img.shields.io/npm/v/@typescript-eslint/typescript-estree.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/utils)
[![NPM Downloads](https://img.shields.io/npm/dm/@typescript-eslint/typescript-estree.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/utils)

## Contributing
👉 See **https://typescript-eslint.io/packages/typescript-estree** for documentation on this package.
> See https://typescript-eslint.io for general documentation on typescript-eslint, the tooling that allows you to run ESLint and Prettier on TypeScript code.

---

# iCloud: web-app/node_modules/@typescript-eslint/type-utils/node_modules/@typescript-eslint/typescript-estree/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/type-utils/node_modules/@typescript-eslint/typescript-estree/README.md
> **Analyzed At:** 2026-06-13T06:32:46.216Z

## `@typescript-eslint/typescript-estree`
> A parser that produces an ESTree-compatible AST for TypeScript code.
[![NPM Version](https://img.shields.io/npm/v/@typescript-eslint/typescript-estree.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/utils)
[![NPM Downloads](https://img.shields.io/npm/dm/@typescript-eslint/typescript-estree.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/utils)

## Contributing
👉 See **https://typescript-eslint.io/packages/typescript-estree** for documentation on this package.
> See https://typescript-eslint.io for general documentation on typescript-eslint, the tooling that allows you to run ESLint and Prettier on TypeScript code.

---

# iCloud: web-app/node_modules/@types/yauzl/README.md

> **Source:** icloud://web-app/node_modules/@types/yauzl/README.md
> **Analyzed At:** 2026-06-13T06:32:46.233Z

## Installation
> `npm install --save @types/yauzl`

## Summary
This package contains type definitions for yauzl (https://github.com/thejoshwolfe/yauzl).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/yauzl.

## Additional Details
* Last updated: Tue, 07 Nov 2023 15:11:36 GMT
* Dependencies: [@types/node](https://npmjs.com/package/@types/node)

## Credits
These definitions were written by [Florian Keller](https://github.com/ffflorian).

---

# iCloud: web-app/node_modules/@typescript-eslint/tsconfig-utils/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/tsconfig-utils/README.md
> **Analyzed At:** 2026-06-13T06:32:46.218Z

## `@typescript-eslint/tsconfig-utils`
> Utilities for collecting TSConfigs for linting scenarios.
[![NPM Version](https://img.shields.io/npm/v/@typescript-eslint/tsconfig-utils.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/tsconfig-utils)
[![NPM Downloads](https://img.shields.io/npm/dm/@typescript-eslint/tsconfig-utils.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/tsconfig-utils)
The utilities in this package are separated from `@typescript-eslint/utils` so that they do not have a dependency on `eslint` or `@typescript-eslint/typescript-estree`.
> See https://typescript-eslint.io for general documentation on typescript-eslint, the tooling that allows you to run ESLint and Prettier on TypeScript code.

---

# iCloud: web-app/node_modules/@typescript-eslint/scope-manager/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/scope-manager/README.md
> **Analyzed At:** 2026-06-13T06:32:46.219Z

## `@typescript-eslint/scope-manager`
[![NPM Version](https://img.shields.io/npm/v/@typescript-eslint/scope-manager.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/scope-manager)
[![NPM Downloads](https://img.shields.io/npm/dm/@typescript-eslint/scope-manager.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/scope-manager)
👉 See **https://typescript-eslint.io/packages/scope-manager** for documentation on this package.
> See https://typescript-eslint.io for general documentation on typescript-eslint, the tooling that allows you to run ESLint and Prettier on TypeScript code.

---

# iCloud: web-app/node_modules/@types/uuid/README.md

> **Source:** icloud://web-app/node_modules/@types/uuid/README.md
> **Analyzed At:** 2026-06-13T06:32:46.234Z

## Installation
> `npm install --save @types/uuid`

## Summary
This package contains type definitions for uuid (https://github.com/uuidjs/uuid).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/uuid.

## Additional Details
* Last updated: Thu, 20 Jun 2024 21:07:25 GMT
* Dependencies: none

## Credits
These definitions were written by [Oliver Hoffmann](https://github.com/iamolivinius), [Felipe Ochoa](https://github.com/felipeochoa), [Chris Barth](https://github.com/cjbarth), [Linus Unnebäck](https://github.com/LinusU), and [Christoph Tavan](https://github.com/ctavan).

---

# iCloud: web-app/node_modules/@types/triple-beam/README.md

> **Source:** icloud://web-app/node_modules/@types/triple-beam/README.md
> **Analyzed At:** 2026-06-13T06:32:46.234Z

## Installation
> `npm install --save @types/triple-beam`

## Summary
This package contains type definitions for triple-beam (https://github.com/winstonjs/triple-beam).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/triple-beam.

## [index.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/triple-beam/index.d.ts)
````ts
export as namespace TripleBeam;

export const LEVEL: unique symbol;
export const MESSAGE: unique symbol;
export const SPLAT: unique symbol;
export const configs: Configs;

export interface Config {
    readonly levels: { [k: string]: number };
    readonly colors: { [k: string]: string };
}

export interface Configs {
    readonly cli: Config;
    readonly npm: Config;
    readonly syslog: Config;
}

````

## Additional Details
* Last updated: Tue, 07 Nov 2023 15:11:36 GMT
* Dependencies: none

## Credits
These definitions were written by [Daniel Byrne](https://github.com/danwbyrne).

---

# iCloud: web-app/node_modules/@types/tough-cookie/README.md

> **Source:** icloud://web-app/node_modules/@types/tough-cookie/README.md
> **Analyzed At:** 2026-06-13T06:32:46.235Z

## Installation
> `npm install --save @types/tough-cookie`

## Summary
This package contains type definitions for tough-cookie (https://github.com/salesforce/tough-cookie).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/tough-cookie.

## Additional Details
* Last updated: Tue, 07 Nov 2023 20:08:00 GMT
* Dependencies: none

## Credits
These definitions were written by [Leonard Thieu](https://github.com/leonard-thieu), [LiJinyao](https://github.com/LiJinyao), and [Michael Wei](https://github.com/no2chem).

---

# iCloud: web-app/node_modules/@types/three/README.md

> **Source:** icloud://web-app/node_modules/@types/three/README.md
> **Analyzed At:** 2026-06-13T06:32:46.235Z

## Installation
> `npm install --save @types/three`

## Summary
This package contains type definitions for three (https://threejs.org/).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/three.

## Additional Details
* Last updated: Wed, 10 Dec 2025 22:36:27 GMT
* Dependencies: [@dimforge/rapier3d-compat](https://npmjs.com/package/@dimforge/rapier3d-compat), [@tweenjs/tween.js](https://npmjs.com/package/@tweenjs/tween.js), [@types/stats.js](https://npmjs.com/package/@types/stats.js), [@types/webxr](https://npmjs.com/package/@types/webxr), [@webgpu/types](https://npmjs.com/package/@webgpu/types), [fflate](https://npmjs.com/package/fflate), [meshoptimizer](https://npmjs.com/package/meshoptimizer)

## Credits
These definitions were written by [Josh Ellis](https://github.com/joshuaellis), and [Nathan Bierema](https://github.com/Methuselah96).

---

# iCloud: web-app/node_modules/@typescript-eslint/project-service/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/project-service/README.md
> **Analyzed At:** 2026-06-13T06:32:46.224Z

## `@typescript-eslint/project-service`
> Standalone TypeScript project service wrapper for linting.
[![NPM Version](https://img.shields.io/npm/v/@typescript-eslint/project-service.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/project-service)
[![NPM Downloads](https://img.shields.io/npm/dm/@typescript-eslint/project-service.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/project-service)
A standalone export of the "Project Service" that powers typed linting for typescript-eslint.
> See https://typescript-eslint.io for general documentation on typescript-eslint, the tooling that allows you to run ESLint and Prettier on TypeScript code.

---

# iCloud: web-app/node_modules/@typescript-eslint/parser/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/parser/README.md
> **Analyzed At:** 2026-06-13T06:32:46.224Z

## `@typescript-eslint/parser`
> An ESLint parser which leverages TypeScript ESTree to allow for ESLint to lint TypeScript source code.
[![NPM Version](https://img.shields.io/npm/v/@typescript-eslint/parser.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/parser)
[![NPM Downloads](https://img.shields.io/npm/dm/@typescript-eslint/parser.svg?style=flat-square)](https://www.npmjs.com/package/@typescript-eslint/parser)
👉 See **https://typescript-eslint.io/packages/parser** for documentation on this package.
> See https://typescript-eslint.io for general documentation on typescript-eslint, the tooling that allows you to run ESLint and Prettier on TypeScript code.

---

# iCloud: web-app/node_modules/@typescript-eslint/parser/node_modules/minimatch/LICENSE.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/parser/node_modules/minimatch/LICENSE.md
> **Analyzed At:** 2026-06-13T06:32:46.226Z

## Blue Oak Model License
Version 1.0.0

## Purpose
This license gives everyone as much permission to work with
this software as possible, while protecting contributors
from liability.

## Acceptance
In order to receive this license, you must agree to its
rules. The rules of this license are both obligations
under that agreement and conditions to your license.
You must not do anything with this software that triggers
a rule that you cannot or will not follow.

## Copyright
Each contributor licenses you to do everything with this
software that would otherwise infringe that contributor's
copyright in it.

## Notices
You must ensure that everyone who gets a copy of
any part of this software from you, with or without
changes, also gets the text of this license or a link to
.

## Excuse
If anyone notifies you in writing that you have not
complied with [Notices](#notices), you can keep your
license by taking all practical steps to comply within 30
days after the notice. If you do not do so, your license
ends immediately.

## Patent
Each contributor licenses you to do everything with this
software that would otherwise infringe any patent claims
they can license or become able to license.

## Reliability
No contributor can revoke this license.

## No Liability
**_As far as the law allows, this software comes as is,
without any warranty or condition, and no contributor
will be liable to anyone for any damages related to this
software or this license, under any kind of legal claim._**

---

# iCloud: web-app/node_modules/@typescript-eslint/parser/node_modules/brace-expansion/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/parser/node_modules/brace-expansion/README.md
> **Analyzed At:** 2026-06-13T06:32:46.229Z

## brace-expansion
[Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html),
as known from sh/bash, in JavaScript.
[![CI](https://github.com/juliangruber/brace-expansion/actions/workflows/ci.yml/badge.svg)](https://github.com/juliangruber/brace-expansion/actions/workflows/ci.yml)
[![downloads](https://img.shields.io/npm/dm/brace-expansion.svg)](https://www.npmjs.org/package/brace-expansion)

## Example
```js
import { expand } from 'brace-expansion'

expand('file-{a,b,c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('-v{,,}')
// => ['-v', '-v', '-v']

expand('file{0..2}.jpg')
// => ['file0.jpg', 'file1.jpg', 'file2.jpg']

expand('file-{a..c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('file{2..0}.jpg')
// => ['file2.jpg', 'file1.jpg', 'file0.jpg']

expand('file{0..4..2}.jpg')
// => ['file0.jpg', 'file2.jpg', 'file4.jpg']

expand('file-{a..e..2}.jpg')
// => ['file-a.jpg', 'file-c.jpg', 'file-e.jpg']

expand('file{00..10..5}.jpg')
// => ['file00.jpg', 'file05.jpg', 'file10.jpg']

expand('{{A..C},{a..c}}')
// => ['A', 'B', 'C', 'a', 'b', 'c']

expand('ppp{,config,oe{,conf}}')
// => ['ppp', 'pppconfig', 'pppoe', 'pppoeconf']
```

## API
```js
import { expand } from 'brace-expansion'
```

## const expanded = expand(str, [options])
Return an array of all possible and valid expansions of `str`. If
none are found, `[str]` is returned.
The `options` object can provide a `max` value to cap the number
of expansions allowed. This is limited to `100_000` by default,
to prevent DoS attacks.
```js
const expansions = expand('{1..100}'.repeat(5), {
  max: 100,
})
// expansions.length will be 100, not 100^5
```
Valid expansions are:
```js
;/^(.*,)+(.+)?$/
// {a,b,...}
```
```js
;/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```
A numeric sequence from `x` to `y` inclusive, with optional increment.
If `x` or `y` start with a leading `0`, all the numbers will be padded
to have equal length. Negative numbers and backwards iteration work too.
```js
;/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```
An alphabetic sequence from `x` to `y` inclusive, with optional increment.
`x` and `y` must be exactly one character, and if given, `incr` must be a
number.
For compatibility reasons, the string `${` is not eligible for brace expansion.

---

# iCloud: web-app/node_modules/@typescript-eslint/parser/node_modules/balanced-match/README.md

> **Source:** icloud://web-app/node_modules/@typescript-eslint/parser/node_modules/balanced-match/README.md
> **Analyzed At:** 2026-06-13T06:32:46.231Z

## balanced-match
``. Supports regular expressions as well!

## Example
Get the first matching pair of braces:
```js
import { balanced } from 'balanced-match'

console.log(balanced('{', '}', 'pre{in{nested}}post'))
console.log(balanced('{', '}', 'pre{first}between{second}post'))
console.log(
  balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'),
)
```
The matches are:
```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## const m = balanced(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:
- **start** the index of the first match of `a`
- **end** the index of the matching `b`
- **pre** the preamble, `a` and `b` not included
- **body** the match, `a` and `b` not included
- **post** the postscript, `a` and `b` not included
If there's no match, `undefined` will be returned.

## const r = balanced.range(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ ,  ]`.
If there's no match, `undefined` will be returned.

---

# iCloud: web-app/node_modules/@types/webxr/README.md

> **Source:** icloud://web-app/node_modules/@types/webxr/README.md
> **Analyzed At:** 2026-06-13T06:32:46.234Z

## Installation
> `npm install --save @types/webxr`

## Summary
This package contains type definitions for webxr (https://www.w3.org/TR/webxr/).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/webxr.

## Additional Details
* Last updated: Mon, 29 Sep 2025 18:40:16 GMT
* Dependencies: none

## Credits
These definitions were written by [Rob Rohan](https://github.com/robrohan), [Raanan Weber](https://github.com/RaananW), [Sean T. McBeth](https://github.com/capnmidnight), and [Timmy Kokke](https://github.com/sorskoot).

---

# iCloud: web-app/node_modules/@types/stats.js/README.md

> **Source:** icloud://web-app/node_modules/@types/stats.js/README.md
> **Analyzed At:** 2026-06-13T06:32:46.268Z

## Installation
> `npm install --save @types/stats.js`

## Summary
This package contains type definitions for stats.js (https://github.com/mrdoob/stats.js).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/stats.js.

## [index.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/stats.js/index.d.ts)
````ts
declare class Stats {
    constructor();

    REVISION: number;
    dom: HTMLDivElement;

    addPanel(panel: Stats.Panel): Stats.Panel;

    /**
     * @param value 0:fps, 1: ms, 2: mb, 3+: custom
     */
    showPanel(value: number): void;

    begin(): void;
    end(): number;
    update(): void;

    // Backwards Compatibility

    /**
     * @deprecated Use `dom` instead.
     */
    domElement: HTMLDivElement;

    /**
     * @deprecated Use `showPanel` instead.
     */
    setMode(value: number): void;
}

declare namespace Stats {
    class Panel {
        constructor(name: string, foregroundColor: string, backgroundColor: string);
        dom: HTMLCanvasElement;
        update(value: number, maxValue: number): void;
    }
}

declare module "stats.js" {
    export = Stats;
}

````

## Additional Details
* Last updated: Mon, 05 May 2025 20:35:19 GMT
* Dependencies: none

## Credits
These definitions were written by [Gregory Dalton](https://github.com/gregolai), [Harm Berntsen](https://github.com/hberntsen), and [Dan Vanderkam](https://github.com/danvk).

---

# iCloud: web-app/node_modules/@types/retry/README.md

> **Source:** icloud://web-app/node_modules/@types/retry/README.md
> **Analyzed At:** 2026-06-13T06:32:46.270Z

## Installation
> `npm install --save @types/retry`

## Summary
This package contains type definitions for retry (https://github.com/tim-kos/node-retry).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/retry

## Additional Details
* Last updated: Thu, 03 Jan 2019 17:45:51 GMT
* Dependencies: none
* Global values: none

## Credits
These definitions were written by Stan Goldmann , BendingBender .

---

# iCloud: web-app/node_modules/@types/request/README.md

> **Source:** icloud://web-app/node_modules/@types/request/README.md
> **Analyzed At:** 2026-06-13T06:32:46.270Z

## Installation
> `npm install --save @types/request`

## Summary
This package contains type definitions for request (https://github.com/request/request).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/request.

## Additional Details
* Last updated: Mon, 28 Jul 2025 22:02:21 GMT
* Dependencies: [@types/caseless](https://npmjs.com/package/@types/caseless), [@types/node](https://npmjs.com/package/@types/node), [@types/tough-cookie](https://npmjs.com/package/@types/tough-cookie), [form-data](https://npmjs.com/package/form-data)

## Credits
These definitions were written by [Carlos Ballesteros Velasco](https://github.com/soywiz), [bonnici](https://github.com/bonnici), [Bart van der Schoor](https://github.com/Bartvds), [Joe Skeen](https://github.com/joeskeen), [Christopher Currens](https://github.com/ccurrens), [Jon Stevens](https://github.com/lookfirst), [Matt R. Wilson](https://github.com/mastermatt), [Jose Colella](https://github.com/josecolella), and [Marek Urbanowicz](https://github.com/murbanowicz).

---

# iCloud: web-app/node_modules/@types/react-reconciler/README.md

> **Source:** icloud://web-app/node_modules/@types/react-reconciler/README.md
> **Analyzed At:** 2026-06-13T06:32:46.271Z

## Installation
> `npm install --save @types/react-reconciler`

## Summary
This package contains type definitions for react-reconciler (https://reactjs.org/).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react-reconciler.

## Additional Details
* Last updated: Wed, 11 Dec 2024 14:36:56 GMT
* Dependencies: none
* Peer dependencies: [@types/react](https://npmjs.com/package/@types/react)

## Credits
These definitions were written by [Nathan Bierema](https://github.com/Methuselah96), [Zhang Haocong](https://github.com/zhanghaocong), and [Mathieu Dutour](https://github.com/mathieudutour).

---

# iCloud: web-app/node_modules/@types/react/README.md

> **Source:** icloud://web-app/node_modules/@types/react/README.md
> **Analyzed At:** 2026-06-13T06:32:46.272Z

## Installation
> `npm install --save @types/react`

## Summary
This package contains type definitions for react (https://react.dev/).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react/v18.

## Additional Details
* Last updated: Thu, 05 Feb 2026 09:44:59 GMT
* Dependencies: [@types/prop-types](https://npmjs.com/package/@types/prop-types), [csstype](https://npmjs.com/package/csstype)

## Credits
These definitions were written by [Asana](https://asana.com), [AssureSign](http://www.assuresign.com), [Microsoft](https://microsoft.com), [John Reilly](https://github.com/johnnyreilly), [Benoit Benezech](https://github.com/bbenezech), [Patricio Zavolinsky](https://github.com/pzavolinsky), [Eric Anderson](https://github.com/ericanderson), [Dovydas Navickas](https://github.com/DovydasNavickas), [Josh Rutherford](https://github.com/theruther4d), [Guilherme Hübner](https://github.com/guilhermehubner), [Ferdy Budhidharma](https://github.com/ferdaber), [Johann Rakotoharisoa](https://github.com/jrakotoharisoa), [Olivier Pascal](https://github.com/pascaloliv), [Martin Hochel](https://github.com/hotell), [Frank Li](https://github.com/franklixuefei), [Jessica Franco](https://github.com/Jessidhia), [Saransh Kataria](https://github.com/saranshkataria), [Kanitkorn Sujautra](https://github.com/lukyth), [Sebastian Silbermann](https://github.com/eps1lon), [Kyle Scully](https://github.com/zieka), [Cong Zhang](https://github.com/dancerphil), [Dimitri Mitropoulos](https://github.com/dimitropoulos), [JongChan Choi](https://github.com/disjukr), [Victor Magalhães](https://github.com/vhfmag), [Priyanshu Rav](https://github.com/priyanshurav), [Dmitry Semigradsky](https://github.com/Semigradsky), and [Matt Pocock](https://github.com/mattpocock).

---

# iCloud: web-app/node_modules/@types/prop-types/README.md

> **Source:** icloud://web-app/node_modules/@types/prop-types/README.md
> **Analyzed At:** 2026-06-13T06:32:46.273Z

## Installation
> `npm install --save @types/prop-types`

## Summary
This package contains type definitions for prop-types (https://github.com/facebook/prop-types).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/prop-types.

## Additional Details
* Last updated: Mon, 09 Jun 2025 20:02:33 GMT
* Dependencies: none

## Credits
These definitions were written by [DovydasNavickas](https://github.com/DovydasNavickas), [Ferdy Budhidharma](https://github.com/ferdaber), and [Sebastian Silbermann](https://github.com/eps1lon).

---

# iCloud: web-app/node_modules/@types/offscreencanvas/README.md

> **Source:** icloud://web-app/node_modules/@types/offscreencanvas/README.md
> **Analyzed At:** 2026-06-13T06:32:46.273Z

## Installation
> `npm install --save @types/offscreencanvas`

## Summary
This package contains type definitions for offscreencanvas (https://html.spec.whatwg.org/multipage/canvas.html#the-offscreencanvas-interface).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/offscreencanvas.

## Additional Details
* Last updated: Tue, 07 Nov 2023 09:09:39 GMT
* Dependencies: none

## Credits
These definitions were written by [Klaus Reimer](https://github.com/kayahr), [Oleg Varaksin](https://github.com/ova2), and [Sean T.McBeth](https://github.com/capnmidnight).

---

# iCloud: web-app/node_modules/@types/node/README.md

> **Source:** icloud://web-app/node_modules/@types/node/README.md
> **Analyzed At:** 2026-06-13T06:32:46.274Z

## Installation
> `npm install --save @types/node`

## Summary
This package contains type definitions for node (https://nodejs.org/).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/node/v20.

## Additional Details
* Last updated: Fri, 06 Mar 2026 00:57:44 GMT
* Dependencies: [undici-types](https://npmjs.com/package/undici-types)

## Credits
These definitions were written by [Microsoft TypeScript](https://github.com/Microsoft), [Alberto Schiabel](https://github.com/jkomyno), [Andrew Makarov](https://github.com/r3nya), [Benjamin Toueg](https://github.com/btoueg), [David Junger](https://github.com/touffy), [Mohsen Azimi](https://github.com/mohsen1), [Nikita Galkin](https://github.com/galkin), [Sebastian Silbermann](https://github.com/eps1lon), [Wilco Bakker](https://github.com/WilcoBakker), [Marcin Kopacz](https://github.com/chyzwar), [Trivikram Kamat](https://github.com/trivikr), [Junxiao Shi](https://github.com/yoursunny), [Ilia Baryshnikov](https://github.com/qwelias), [ExE Boss](https://github.com/ExE-Boss), [Piotr Błażejewicz](https://github.com/peterblazejewicz), [Anna Henningsen](https://github.com/addaleax), [Victor Perin](https://github.com/victorperin), [NodeJS Contributors](https://github.com/NodeJS), [Linus Unnebäck](https://github.com/LinusU), [wafuwafu13](https://github.com/wafuwafu13), [Matteo Collina](https://github.com/mcollina), and [Dmitry Semigradsky](https://github.com/Semigradsky).

---

# iCloud: web-app/node_modules/@types/matter-js/README.md

> **Source:** icloud://web-app/node_modules/@types/matter-js/README.md
> **Analyzed At:** 2026-06-13T06:32:46.275Z

## Installation
> `npm install --save @types/matter-js`

## Summary
This package contains type definitions for matter-js (https://github.com/liabru/matter-js).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/matter-js.

## Additional Details
* Last updated: Sat, 20 Sep 2025 20:32:23 GMT
* Dependencies: none

## Credits
These definitions were written by [Ivane Gegia](https://twitter.com/ivanegegia), [David Asmuth](https://github.com/piranha771), [Piotr Pietrzak](https://github.com/hasparus), [slikts](https://github.com/slikts), and [Steven Snoeijen](https://github.com/stevensnoeijen).

---

# iCloud: web-app/node_modules/@types/json5/README.md

> **Source:** icloud://web-app/node_modules/@types/json5/README.md
> **Analyzed At:** 2026-06-13T06:32:46.276Z

## Installation
> `npm install --save @types/json5`

## Summary
This package contains type definitions for JSON5 (http://json5.org/).

## Details
Files were exported from https://www.github.com/DefinitelyTyped/DefinitelyTyped/tree/types-2.0/json5

## Additional Details
* Last updated: Mon, 19 Sep 2016 17:28:59 GMT
* File structure: ProperModule
* Library Dependencies: none
* Module Dependencies: none
* Global values: json5

## Credits
These definitions were written by Jason Swearingen .

---

# iCloud: web-app/node_modules/@types/json-schema/README.md

> **Source:** icloud://web-app/node_modules/@types/json-schema/README.md
> **Analyzed At:** 2026-06-13T06:32:46.277Z

## Installation
> `npm install --save @types/json-schema`

## Summary
This package contains type definitions for json-schema (https://github.com/kriszyp/json-schema).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/json-schema.

## Additional Details
* Last updated: Tue, 07 Nov 2023 03:09:37 GMT
* Dependencies: none

## Credits
These definitions were written by [Boris Cherny](https://github.com/bcherny), [Lucian Buzzo](https://github.com/lucianbuzzo), [Roland Groza](https://github.com/rolandjitsu), and [Jason Kwok](https://github.com/JasonHK).

---

# iCloud: web-app/node_modules/@types/estree/README.md

> **Source:** icloud://web-app/node_modules/@types/estree/README.md
> **Analyzed At:** 2026-06-13T06:32:46.277Z

## Installation
> `npm install --save @types/estree`

## Summary
This package contains type definitions for estree (https://github.com/estree/estree).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/estree.

## Additional Details
* Last updated: Fri, 06 Jun 2025 00:04:33 GMT
* Dependencies: none

## Credits
These definitions were written by [RReverser](https://github.com/RReverser).

---

# iCloud: web-app/node_modules/@types/draco3d/README.md

> **Source:** icloud://web-app/node_modules/@types/draco3d/README.md
> **Analyzed At:** 2026-06-13T06:32:46.278Z

## Installation
> `npm install --save @types/draco3d`

## Summary
This package contains type definitions for draco3d (https://github.com/google/draco#readme).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/draco3d.

## Additional Details
* Last updated: Tue, 14 May 2024 15:07:51 GMT
* Dependencies: none

## Credits
These definitions were written by [Don McCurdy](https://github.com/donmccurdy), and [Horizon0514](https://github.com/horizon0514).

---

# iCloud: web-app/node_modules/@types/caseless/README.md

> **Source:** icloud://web-app/node_modules/@types/caseless/README.md
> **Analyzed At:** 2026-06-13T06:32:46.279Z

## Installation
> `npm install --save @types/caseless`

## Summary
This package contains type definitions for caseless (https://github.com/mikeal/caseless).

## Details
Files were exported from https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/caseless.

## [index.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/caseless/index.d.ts)
````ts
type KeyType = string;
type ValueType = any;
type RawDict = object;

declare function caseless(dict?: RawDict): caseless.Caseless;

declare namespace caseless {
    function httpify(resp: object, headers: RawDict): Caseless;

    interface Caseless {
        set(name: KeyType, value: ValueType, clobber?: boolean): KeyType | false;
        set(dict: RawDict): void;
        has(name: KeyType): KeyType | false;
        get(name: KeyType): ValueType | undefined;
        swap(name: KeyType): void;
        del(name: KeyType): boolean;
    }

    interface Httpified {
        headers: RawDict;
        setHeader(name: KeyType, value: ValueType, clobber?: boolean): KeyType | false;
        setHeader(dict: RawDict): void;
        hasHeader(name: KeyType): KeyType | false;
        getHeader(name: KeyType): ValueType | undefined;
        removeHeader(name: KeyType): boolean;
    }
}

export = caseless;

````

## Additional Details
* Last updated: Mon, 06 Nov 2023 22:41:05 GMT
* Dependencies: none

## Credits
These definitions were written by [downace](https://github.com/downace), [Matt R. Wilson](https://github.com/mastermatt), and [Emily Klassen](https://github.com/forivall).

---

# iCloud: web-app/node_modules/@tweenjs/tween.js/README.md

> **Source:** icloud://web-app/node_modules/@tweenjs/tween.js/README.md
> **Analyzed At:** 2026-06-13T06:32:46.280Z

## tween.js
JavaScript (TypeScript) tweening engine for easy animations, incorporating optimised Robert Penner's equations.
[![NPM Version][npm-image]][npm-url]
[![CDNJS][cdnjs-image]][cdnjs-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Build and Tests][ci-image]][ci-url]
More languages: [English](./README.md), [简体中文](./README_zh-CN.md)
---
```html


<div id="box"></div>




```
[Try this example on CodePen](https://codepen.io/trusktr/pen/KKGaBVz?editors=1000)

## From CDN
Install from a content-delivery network (CDN) like in the above example.
From cdnjs:
```html

```
Or from unpkg.com:
```html

```
Note that unpkg.com supports a semver version in the URL, where the `^` in the URL tells unpkg to give you the latest version 20.x.x.

## Build and include in your project with script tag
Currently npm is required to build the project.
```bash
git clone https://github.com/tweenjs/tween.js
cd tween.js
npm install
npm run build
```
This will create some builds in the `dist` directory. There are currently two different builds of the library:
- UMD : `tween.umd.js`
- ES6 Module : `tween.es.js`
You are now able to copy tween.umd.js into your project, then include it with
a script tag, which will add TWEEN to the global scope,
```html

```
or import TWEEN as a JavaScript module,
```html

```
where `path/to` is replaced with the location where you placed the file.

## With `npm install` and `import` from `node_modules`
You can add tween.js as an npm dependency:
```bash
npm install @tweenjs/tween.js
```

## With a build tool
If you are using [Node.js](https://nodejs.org/), [Parcel](https://parceljs.org/), [Webpack](https://webpack.js.org/), [Rollup](https://rollupjs.org/), [Vite](https://vitejs.dev/), or another build tool, then you can now use the following to include tween.js:
```javascript
import * as TWEEN from '@tweenjs/tween.js'
```

## Without a build tool
You can import from `node_modules` if you serve node_modules as part of your website, using an `importmap` script tag. First, assuming `node_modules` is at the root of your website, you can write an import map:
```html

```
Now in any of your module scripts you can import it by its package name:
```javascript
import * as TWEEN from '@tweenjs/tween.js'
```

## Features
- Does one thing and one thing only: tween properties
- Doesn't take care of CSS units (e.g. appending `px`)
- Doesn't interpolate colors
- Easing functions are reusable outside of Tween
- Can also use custom easing functions

## Documentation
- [User guide](./docs/user_guide.md)
- [Contributor guide](./docs/contributor_guide.md)
- [Tutorial](https://web.archive.org/web/20220601192930/http://learningthreejs.com/blog/2011/08/17/tweenjs-for-smooth-animation/) using tween.js with three.js
- Also: [libtween](https://github.com/jsm174/libtween), a port of tween.js to C by [jsm174](https://github.com/jsm174)

## Examples
hello world
(source)
Bars
(source)
Black and red
(source)
Graphs
(source)
Simplest possible example
(source)
Video and time
(source)
Array interpolation
(source)
Dynamic to, object
(source)
Dynamic to, interpolation array
(source)
Dynamic to, large interpolation array
(source)
Repeat
(source)
Relative values
(source)
Yoyo
(source)
Stop all chained tweens
(source)
Custom functions
(source)
Relative start time
(source)
Pause tween
(source)
Complex properties
(source)
Animate an array of values
(source)

## Tests
You need to install `npm` first--this comes with node.js, so install that one first. Then, cd to `tween.js`'s (or wherever you cloned the repo) directory and run:
```bash
npm install
```
To run the tests run:
```bash
npm test
```
If you want to add any feature or change existing features, you _must_ run the tests to make sure you didn't break anything else. Any pull request (PR) needs to have updated passing tests for feature changes (or new passing tests for new features or fixes) in `src/tests.ts` a PR to be accepted. See [contributing](CONTRIBUTING.md) for more information.

## People
Maintainers: [Joe Pea (@trusktr)](https://github.com/trusktr).
[All contributors](http://github.com/tweenjs/tween.js/contributors).

## Projects using tween.js
[](https://lume.io)
[![A-Frame VR](https://tweenjs.github.io/tween.js/assets/projects/10_aframe.png)](https://aframe.io)
[![MOMA Inventing Abstraction 1910-1925](https://tweenjs.github.io/tween.js/assets/projects/09_moma.png)](http://www.moma.org/interactives/exhibitions/2012/inventingabstraction/)
[![Web Lab](https://tweenjs.github.io/tween.js/assets/projects/08_web_lab.png)](http://www.chromeweblab.com/)
[![MACCHINA I](https://tweenjs.github.io/tween.js/assets/projects/07_macchina.png)](http://5013.es/toys/macchina)
[![Minesweeper 3D](https://tweenjs.github.io/tween.js/assets/projects/06_minesweeper3d.png)](http://egraether.com/mine3d/)
[![ROME](https://tweenjs.github.io/tween.js/assets/projects/05_rome.png)](http://ro.me)
[![WebGL Globe](https://tweenjs.github.io/tween.js/assets/projects/04_webgl_globe.png)](http://data-arts.appspot.com/globe)
[![Androidify](https://tweenjs.github.io/tween.js/assets/projects/03_androidify.png)](http://www.androidify.com/)
[![The Wilderness Downtown](https://tweenjs.github.io/tween.js/assets/projects/01_wilderness.png)](http://thewildernessdowntown.com/)
[![Linechart](https://tweenjs.github.io/tween.js/assets/projects/00_linechart.png)](http://dejavis.org/linechart)
[npm-image]: https://img.shields.io/npm/v/@tweenjs/tween.js.svg
[npm-url]: https://npmjs.org/package/@tweenjs/tween.js
[downloads-image]: https://img.shields.io/npm/dm/@tweenjs/tween.js.svg
[downloads-url]: https://npmjs.org/package/@tweenjs/tween.js
[ci-image]: https://github.com/tweenjs/tween.js/workflows/build%20and%20tests/badge.svg?branch=master
[ci-url]: https://github.com/tweenjs/tween.js/actions
[cdnjs-image]: https://img.shields.io/cdnjs/v/tween.js.svg
[cdnjs-url]: https://cdnjs.com/libraries/tween.js

---

# iCloud: web-app/node_modules/@ts-morph/common/readme.md

> **Source:** icloud://web-app/node_modules/@ts-morph/common/readme.md
> **Analyzed At:** 2026-06-13T06:32:46.281Z

## @ts-morph/common
Common functionality for [ts-morph](../ts-morph) and [@ts-morph/bootstrap](../bootstrap).
Please do not depend on this library!

---

# iCloud: web-app/node_modules/@ts-morph/common/node_modules/minimatch/LICENSE.md

> **Source:** icloud://web-app/node_modules/@ts-morph/common/node_modules/minimatch/LICENSE.md
> **Analyzed At:** 2026-06-13T06:32:46.282Z

## Blue Oak Model License
Version 1.0.0

## Purpose
This license gives everyone as much permission to work with
this software as possible, while protecting contributors
from liability.

## Acceptance
In order to receive this license, you must agree to its
rules. The rules of this license are both obligations
under that agreement and conditions to your license.
You must not do anything with this software that triggers
a rule that you cannot or will not follow.

## Copyright
Each contributor licenses you to do everything with this
software that would otherwise infringe that contributor's
copyright in it.

## Notices
You must ensure that everyone who gets a copy of
any part of this software from you, with or without
changes, also gets the text of this license or a link to
.

## Excuse
If anyone notifies you in writing that you have not
complied with [Notices](#notices), you can keep your
license by taking all practical steps to comply within 30
days after the notice. If you do not do so, your license
ends immediately.

## Patent
Each contributor licenses you to do everything with this
software that would otherwise infringe any patent claims
they can license or become able to license.

## Reliability
No contributor can revoke this license.

## No Liability
**_As far as the law allows, this software comes as is,
without any warranty or condition, and no contributor
will be liable to anyone for any damages related to this
software or this license, under any kind of legal claim._**

---

# iCloud: web-app/node_modules/@ts-morph/common/node_modules/brace-expansion/README.md

> **Source:** icloud://web-app/node_modules/@ts-morph/common/node_modules/brace-expansion/README.md
> **Analyzed At:** 2026-06-13T06:32:46.284Z

## brace-expansion
[Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html),
as known from sh/bash, in JavaScript.
[![CI](https://github.com/juliangruber/brace-expansion/actions/workflows/ci.yml/badge.svg)](https://github.com/juliangruber/brace-expansion/actions/workflows/ci.yml)
[![downloads](https://img.shields.io/npm/dm/brace-expansion.svg)](https://www.npmjs.org/package/brace-expansion)

## Example
```js
import { expand } from 'brace-expansion'

expand('file-{a,b,c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('-v{,,}')
// => ['-v', '-v', '-v']

expand('file{0..2}.jpg')
// => ['file0.jpg', 'file1.jpg', 'file2.jpg']

expand('file-{a..c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('file{2..0}.jpg')
// => ['file2.jpg', 'file1.jpg', 'file0.jpg']

expand('file{0..4..2}.jpg')
// => ['file0.jpg', 'file2.jpg', 'file4.jpg']

expand('file-{a..e..2}.jpg')
// => ['file-a.jpg', 'file-c.jpg', 'file-e.jpg']

expand('file{00..10..5}.jpg')
// => ['file00.jpg', 'file05.jpg', 'file10.jpg']

expand('{{A..C},{a..c}}')
// => ['A', 'B', 'C', 'a', 'b', 'c']

expand('ppp{,config,oe{,conf}}')
// => ['ppp', 'pppconfig', 'pppoe', 'pppoeconf']
```

## API
```js
import { expand } from 'brace-expansion'
```

## const expanded = expand(str, [options])
Return an array of all possible and valid expansions of `str`. If
none are found, `[str]` is returned.
The `options` object can provide a `max` value to cap the number
of expansions allowed. This is limited to `100_000` by default,
to prevent DoS attacks.
```js
const expansions = expand('{1..100}'.repeat(5), {
  max: 100,
})
// expansions.length will be 100, not 100^5
```
Valid expansions are:
```js
;/^(.*,)+(.+)?$/
// {a,b,...}
```
```js
;/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```
A numeric sequence from `x` to `y` inclusive, with optional increment.
If `x` or `y` start with a leading `0`, all the numbers will be padded
to have equal length. Negative numbers and backwards iteration work too.
```js
;/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```
An alphabetic sequence from `x` to `y` inclusive, with optional increment.
`x` and `y` must be exactly one character, and if given, `incr` must be a
number.
For compatibility reasons, the string `${` is not eligible for brace expansion.

---

# iCloud: web-app/node_modules/@ts-morph/common/node_modules/balanced-match/README.md

> **Source:** icloud://web-app/node_modules/@ts-morph/common/node_modules/balanced-match/README.md
> **Analyzed At:** 2026-06-13T06:32:46.286Z

## balanced-match
``. Supports regular expressions as well!

## Example
Get the first matching pair of braces:
```js
import { balanced } from 'balanced-match'

console.log(balanced('{', '}', 'pre{in{nested}}post'))
console.log(balanced('{', '}', 'pre{first}between{second}post'))
console.log(
  balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'),
)
```
The matches are:
```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## const m = balanced(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:
- **start** the index of the first match of `a`
- **end** the index of the matching `b`
- **pre** the preamble, `a` and `b` not included
- **body** the match, `a` and `b` not included
- **post** the postscript, `a` and `b` not included
If there's no match, `undefined` will be returned.

## const r = balanced.range(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ ,  ]`.
If there's no match, `undefined` will be returned.

---

# iCloud: web-app/node_modules/@tootallnate/once/README.md

> **Source:** icloud://web-app/node_modules/@tootallnate/once/README.md
> **Analyzed At:** 2026-06-13T06:32:46.287Z

## Installation
Install with `npm`:
```bash
$ npm install @tootallnate/once
```

## once(emitter: EventEmitter, name: string, opts?: OnceOptions): Promise&lt;[...Args]&gt;
Creates a Promise that waits for event `name` to occur on `emitter`, and resolves
the promise with an array of the values provided to the event handler. If an
`error` event occurs before the event specified by `name`, then the Promise is
rejected with the error argument.
```typescript
import once from '@tootallnate/once';
import { EventEmitter } from 'events';

const emitter = new EventEmitter();

setTimeout(() => {
    emitter.emit('foo', 'bar');
}, 100);

const [result] = await once(emitter, 'foo');
console.log({ result });
// { result: 'bar' }
```

## Promise Strong Typing
The main feature that this module provides over other "once" implementations is that
the Promise that is returned is _**strongly typed**_ based on the type of `emitter`
and the `name` of the event. Some examples are shown below.
_The process "exit" event contains a single number for exit code:_
```typescript
const [code] = await once(process, 'exit');
//     ^ number
```
_A child process "exit" event contains either an exit code or a signal:_
```typescript
const child = spawn('echo', []);
const [code, signal] = await once(child, 'exit');
//     ^ number | null
//           ^ string | null
```
_A forked child process "message" event is type `any`, so you can cast the Promise directly:_
```typescript
const child = fork('file.js');

// With `await`
const [message, _]: [WorkerPayload, unknown] = await once(child, 'message');

// With Promise
const messagePromise: Promise<[WorkerPayload, unknown]> = once(child, 'message');

// Better yet would be to leave it as `any`, and validate the payload
// at runtime with i.e. `ajv` + `json-schema-to-typescript`
```
_If the TypeScript definition does not contain an overload for the specified event name, then the Promise will have type `unknown[]` and your code will need to narrow the result manually:_
```typescript
interface CustomEmitter extends EventEmitter {
    on(name: 'foo', listener: (a: string, b: number) => void): this;
}

const emitter: CustomEmitter = new EventEmitter();

// "foo" event is a defined overload, so it's properly typed
const fooPromise = once(emitter, 'foo');
//    ^ Promise<[a: string, b: number]>

// "bar" event in not a defined overload, so it gets `unknown[]`
const barPromise = once(emitter, 'bar');
//    ^ Promise<unknown[]>
```

## OnceOptions
-   `signal` - `AbortSignal` instance to unbind event handlers before the Promise has been fulfilled.

---

# iCloud: web-app/node_modules/@standard-schema/spec/README.md

> **Source:** icloud://web-app/node_modules/@standard-schema/spec/README.md
> **Analyzed At:** 2026-06-13T06:32:46.314Z

## The specifications
The specifications can be found below in their entirety. Libraries wishing to implement a spec can copy/paste the code block below into their codebase. They're also available at `@standard-schema/spec` on [npm](https://www.npmjs.com/package/@standard-schema/spec) and [JSR](https://jsr.io/@standard-schema/spec).
```ts
// #########################
// ###   Standard Typed  ###
// #########################

/** The Standard Typed interface. This is a base type extended by other specs. */
export interface StandardTypedV1<Input = unknown, Output = Input> {
  /** The Standard properties. */
  readonly "~standard": StandardTypedV1.Props<Input, Output>;
}

export declare namespace StandardTypedV1 {
  /** The Standard Typed properties interface. */
  export interface Props<Input = unknown, Output = Input> {
    /** The version number of the standard. */
    readonly version: 1;
    /** The vendor name of the schema library. */
    readonly vendor: string;
    /** Inferred types associated with the schema. */
    readonly types?: Types<Input, Output> | undefined;
  }

  /** The Standard Typed types interface. */
  export interface Types<Input = unknown, Output = Input> {
    /** The input type of the schema. */
    readonly input: Input;
    /** The output type of the schema. */
    readonly output: Output;
  }

  /** Infers the input type of a Standard Typed. */
  export type InferInput<Schema extends StandardTypedV1> = NonNullable<
    Schema["~standard"]["types"]
  >["input"];

  /** Infers the output type of a Standard Typed. */
  export type InferOutput<Schema extends StandardTypedV1> = NonNullable<
    Schema["~standard"]["types"]
  >["output"];
}

// ##########################
// ###   Standard Schema  ###
// ##########################

/** The Standard Schema interface. */
export interface StandardSchemaV1<Input = unknown, Output = Input> {
  /** The Standard Schema properties. */
  readonly "~standard": StandardSchemaV1.Props<Input, Output>;
}

export declare namespace StandardSchemaV1 {
  /** The Standard Schema properties interface. */
  export interface Props<Input = unknown, Output = Input>
    extends StandardTypedV1.Props<Input, Output> {
    /** Validates unknown input values. */
    readonly validate: (
      value: unknown,
      options?: StandardSchemaV1.Options | undefined
    ) => Result<Output> | Promise<Result<Output>>;
  }

  /** The result interface of the validate function. */
  export type Result<Output> = SuccessResult<Output> | FailureResult;

  /** The result interface if validation succeeds. */
  export interface SuccessResult<Output> {
    /** The typed output value. */
    readonly value: Output;
    /** A falsy value for `issues` indicates success. */
    readonly issues?: undefined;
  }

  export interface Options {
    /** Explicit support for additional vendor-specific parameters, if needed. */
    readonly libraryOptions?: Record<string, unknown> | undefined;
  }

  /** The result interface if validation fails. */
  export interface FailureResult {
    /** The issues of failed validation. */
    readonly issues: ReadonlyArray<Issue>;
  }

  /** The issue interface of the failure output. */
  export interface Issue {
    /** The error message of the issue. */
    readonly message: string;
    /** The path of the issue, if any. */
    readonly path?: ReadonlyArray<PropertyKey | PathSegment> | undefined;
  }

  /** The path segment interface of the issue. */
  export interface PathSegment {
    /** The key representing a path segment. */
    readonly key: PropertyKey;
  }

  /** The Standard types interface. */
  export interface Types<Input = unknown, Output = Input>
    extends StandardTypedV1.Types<Input, Output> {}

  /** Infers the input type of a Standard. */
  export type InferInput<Schema extends StandardTypedV1> =
    StandardTypedV1.InferInput<Schema>;

  /** Infers the output type of a Standard. */
  export type InferOutput<Schema extends StandardTypedV1> =
    StandardTypedV1.InferOutput<Schema>;
}

// ###############################
// ###   Standard JSON Schema  ###
// ###############################

/** The Standard JSON Schema interface. */
export interface StandardJSONSchemaV1<Input = unknown, Output = Input> {
  /** The Standard JSON Schema properties. */
  readonly "~standard": StandardJSONSchemaV1.Props<Input, Output>;
}

export declare namespace StandardJSONSchemaV1 {
  /** The Standard JSON Schema properties interface. */
  export interface Props<Input = unknown, Output = Input>
    extends StandardTypedV1.Props<Input, Output> {
    /** Methods for generating the input/output JSON Schema. */
    readonly jsonSchema: StandardJSONSchemaV1.Converter;
  }

  /** The Standard JSON Schema converter interface. */
  export interface Converter {
    /** Converts the input type to JSON Schema. May throw if conversion is not supported. */
    readonly input: (
      options: StandardJSONSchemaV1.Options
    ) => Record<string, unknown>;
    /** Converts the output type to JSON Schema. May throw if conversion is not supported. */
    readonly output: (
      options: StandardJSONSchemaV1.Options
    ) => Record<string, unknown>;
  }

  /**
   * The target version of the generated JSON Schema.
   *
   * It is *strongly recommended* that implementers support `"draft-2020-12"` and `"draft-07"`, as they are both in wide use. All other targets can be implemented on a best-effort basis. Libraries should throw if they don't support a specified target.
   *
   * The `"openapi-3.0"` target is intended as a standardized specifier for OpenAPI 3.0 which is a superset of JSON Schema `"draft-04"`.
   */
  export type Target =
    | "draft-2020-12"
    | "draft-07"
    | "openapi-3.0"
    // Accepts any string for future targets while preserving autocomplete
    | ({} & string);

  /** The options for the input/output methods. */
  export interface Options {
    /** Specifies the target version of the generated JSON Schema. Support for all versions is on a best-effort basis. If a given version is not supported, the library should throw. */
    readonly target: Target;

    /** Explicit support for additional vendor-specific parameters, if needed. */
    readonly libraryOptions?: Record<string, unknown> | undefined;
  }

  /** The Standard types interface. */
  export interface Types<Input = unknown, Output = Input>
    extends StandardTypedV1.Types<Input, Output> {}

  /** Infers the input type of a Standard. */
  export type InferInput<Schema extends StandardTypedV1> =
    StandardTypedV1.InferInput<Schema>;

  /** Infers the output type of a Standard. */
  export type InferOutput<Schema extends StandardTypedV1> =
    StandardTypedV1.InferOutput<Schema>;
}
```

---

# iCloud: web-app/node_modules/@so-ric/colorspace/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@so-ric/colorspace/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.315Z

## 1.1.4
- Revert release 1.1.3 which introduced a breaking change

## 1.1.3
- Apply security patches

---

# iCloud: web-app/node_modules/@so-ric/colorspace/README.md

> **Source:** icloud://web-app/node_modules/@so-ric/colorspace/README.md
> **Analyzed At:** 2026-06-13T06:32:46.318Z

## colorspace
Colorspace is a simple module which generates HEX color codes for namespaces.
The base color is decided by the first part of the namespace. All other parts of
the namespace alters the color tone. This way you can visually see which
namespaces belong together and which does not.

## Installation
The module is released in the public npm registry and can be installed by
running:
```
npm install --save @so-ric/colorspace
```

## Usage
We assume that you've already required the module using the following code:
```js
'use strict';

var colorspace = require('@so-ric/colorspace');
```
The returned function accepts 2 arguments:
1. `namespace` **string**, The namespace that needs to have a HEX color
generated.
2. `delimiter`, **string**, **optional**, Delimiter to find the different
sections of the namespace. Defaults to `:`

## Example
```js
console.log(colorspace('color')) // #6b4b3a
console.log(colorspace('color:space')) // #796B67
```

---

# iCloud: web-app/node_modules/@rtsao/scc/README.md

> **Source:** icloud://web-app/node_modules/@rtsao/scc/README.md
> **Analyzed At:** 2026-06-13T06:32:46.322Z

## `@rtsao/scc`
Find strongly connected components of a directed graph using [Tarjan's algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm).
This algorithm efficiently yields both a topological order and list of any cycles.

## Installation
```
yarn add @rtsao/scc
```
```
npm install @rtsao/scc
```

## Usage
```js
const scc = require("@rtsao/scc");

const digraph = new Map([
  ["a", new Set(["c", "d"])],
  ["b", new Set(["a"])],
  ["c", new Set(["b"])],
  ["d", new Set(["e"])],
  ["e", new Set()]
]);

const components = scc(digraph);
// [ Set { 'e' }, Set { 'd' }, Set { 'b', 'c', 'a' } ]
```

## Illustration of example input digraph
```
┌───┐     ┌───┐
│ d │ ◀── │ a │ ◀┐
└───┘     └───┘  │
  │         │    │
  ▼         ▼    │
┌───┐     ┌───┐  │
│ e │     │ c │  │
└───┘     └───┘  │
            │    │
            ▼    │
          ┌───┐  │
          │ b │ ─┘
          └───┘
```

---

# iCloud: web-app/node_modules/@resvg/resvg-wasm/README.md

> **Source:** icloud://web-app/node_modules/@resvg/resvg-wasm/README.md
> **Analyzed At:** 2026-06-13T06:32:46.328Z

## @resvg/resvg-wasm
> resvg-js is a high-performance SVG renderer and toolkit, powered by Rust based [resvg](https://github.com/RazrFalcon/resvg/) and [napi-rs](https://github.com/napi-rs/napi-rs).
This is the **WebAssembly** binary for [`@resvg/resvg-js`](https://github.com/yisibl/resvg-js)

## Playground
https://resvg-js.vercel.app

## License
[MPLv2.0](https://www.mozilla.org/en-US/MPL/)
Copyright (c) 2021-present, yisibl(一丝)

---

# iCloud: web-app/node_modules/@react-three/fiber/readme.md

> **Source:** icloud://web-app/node_modules/@react-three/fiber/readme.md
> **Analyzed At:** 2026-06-13T06:32:46.329Z

## Does it have limitations?
None. Everything that works in Threejs will work here without exception.

## Is it slower than plain Threejs?
No. There is no overhead. Components render outside of React. It outperforms Threejs in scale due to React's scheduling abilities.

## Can it keep up with frequent feature updates to Threejs?
Yes. It merely expresses Threejs in JSX: `` becomes `new THREE.Mesh()`, and that happens dynamically. If a new Threejs version adds, removes or changes features, it will be available to you instantly without depending on updates to this library.

## What does it look like?
Let's make a re-usable component that has its own state, reacts to user-input and participates in the render-loop. (live demo).
```jsx
import { createRoot } from 'react-dom/client'
import React, { useRef, useState } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'

function Box(props) {
  // This reference gives us direct access to the THREE.Mesh object
  const ref = useRef()
  // Hold state for hovered and clicked events
  const [hovered, hover] = useState(false)
  const [clicked, click] = useState(false)
  // Subscribe this component to the render-loop, rotate the mesh every frame
  useFrame((state, delta) => (ref.current.rotation.x += delta))
  // Return the view, these are regular Threejs elements expressed in JSX
  return (
    <mesh
      {...props}
      ref={ref}
      scale={clicked ? 1.5 : 1}
      onClick={(event) => click(!clicked)}
      onPointerOver={(event) => hover(true)}
      onPointerOut={(event) => hover(false)}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? 'hotpink' : 'orange'} />
    </mesh>
  )
}

createRoot(document.getElementById('root')).render(
  <Canvas>
    <ambientLight />
    <pointLight position={[10, 10, 10]} />
    <Box position={[-1.2, 0, 0]} />
    <Box position={[1.2, 0, 0]} />
  </Canvas>,
)
```
Show TypeScript example
```bash
npm install @types/three
```
```tsx
import * as THREE from 'three'
import { createRoot } from 'react-dom/client'
import React, { useRef, useState } from 'react'
import { Canvas, useFrame, ThreeElements } from '@react-three/fiber'

function Box(props: ThreeElements['mesh']) {
  const ref = useRef<THREE.Mesh>(null!)
  const [hovered, hover] = useState(false)
  const [clicked, click] = useState(false)
  useFrame((state, delta) => (ref.current.rotation.x += delta))
  return (
    <mesh
      {...props}
      ref={ref}
      scale={clicked ? 1.5 : 1}
      onClick={(event) => click(!clicked)}
      onPointerOver={(event) => hover(true)}
      onPointerOut={(event) => hover(false)}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? 'hotpink' : 'orange'} />
    </mesh>
  )
}

createRoot(document.getElementById('root') as HTMLElement).render(
  <Canvas>
    <ambientLight />
    <pointLight position={[10, 10, 10]} />
    <Box position={[-1.2, 0, 0]} />
    <Box position={[1.2, 0, 0]} />
  </Canvas>,
)
```
Live demo: https://codesandbox.io/s/icy-tree-brnsm?file=/src/App.tsx
Show React Native example
This example relies on react 18 and uses `expo-cli`, but you can create a bare project with their template or with the `react-native` CLI.
```bash
# Install expo-cli, this will create our app
npm install expo-cli -g
# Create app and cd into it
expo init my-app
cd my-app
# Install dependencies
npm install three @react-three/fiber react
# Start
expo start
```
Some configuration may be required to tell the Metro bundler about your assets if you use `useLoader` or Drei abstractions like `useGLTF` and `useTexture`:
```js
// metro.config.js
module.exports = {
  resolver: {
    sourceExts: ['js', 'jsx', 'json', 'ts', 'tsx', 'cjs'],
    assetExts: ['glb', 'png', 'jpg'],
  },
}
```
```tsx
import React, { useRef, useState } from 'react'
import { Canvas, useFrame } from '@react-three/fiber/native'
function Box(props) {
  const mesh = useRef(null)
  const [hovered, setHover] = useState(false)
  const [active, setActive] = useState(false)
  useFrame((state, delta) => (mesh.current.rotation.x += delta))
  return (
    <mesh
      {...props}
      ref={mesh}
      scale={active ? 1.5 : 1}
      onClick={(event) => setActive(!active)}
      onPointerOver={(event) => setHover(true)}
      onPointerOut={(event) => setHover(false)}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? 'hotpink' : 'orange'} />
    </mesh>
  )
}
export default function App() {
  return (
    <Canvas>
      <ambientLight />
      <pointLight position={[10, 10, 10]} />
      <Box position={[-1.2, 0, 0]} />
      <Box position={[1.2, 0, 0]} />
    </Canvas>
  )
}
```
---

## Documentation, tutorials, examples
Visit [docs.pmnd.rs](https://docs.pmnd.rs/react-three-fiber)

## Fundamentals
You need to be versed in both React and Threejs before rushing into this. If you are unsure about React consult the official [React docs](https://react.dev/learn), especially [the section about hooks](https://react.dev/reference/react). As for Threejs, make sure you at least glance over the following links:
1. Make sure you have a [basic grasp of Threejs](https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene). Keep that site open.
2. When you know what a scene is, a camera, mesh, geometry, material, fork the [demo above](https://github.com/pmndrs/react-three-fiber#what-does-it-look-like).
3. [Look up](https://threejs.org/docs/index.html#api/en/objects/Mesh) the JSX elements that you see (mesh, ambientLight, etc), _all_ threejs exports are native to three-fiber.
4. Try changing some values, scroll through our [API](https://docs.pmnd.rs/react-three-fiber/API) to see what the various settings and hooks do.
Some reading material:
- [Threejs-docs](https://threejs.org/docs)
- [Threejs-examples](https://threejs.org/examples)
- [Threejs-fundamentals](https://threejs.org/manual/#en/fundamentals)
- [three.js-journey](https://threejs-journey.com)
- [Discover Threejs](https://discoverthreejs.com)
- [Do's and don'ts](https://discoverthreejs.com/tips-and-tricks) for performance and best practices
- [react-three-fiber alligator.io tutorial](https://alligator.io/react/react-with-threejs) by [@dghez\_](https://twitter.com/dghez_)

## Ecosystem
- [`@react-three/gltfjsx`](https://github.com/pmndrs/gltfjsx) &ndash; turns GLTFs into JSX components
- [`@react-three/drei`](https://github.com/pmndrs/drei) &ndash; useful helpers for react-three-fiber
- [`@react-three/postprocessing`](https://github.com/pmndrs/react-postprocessing) &ndash; post-processing effects
- [`@react-three/flex`](https://github.com/pmndrs/react-three-flex) &ndash; flexbox for react-three-fiber
- [`@react-three/xr`](https://github.com/pmndrs/react-xr) &ndash; VR/AR controllers and events
- [`@react-three/cannon`](https://github.com/pmndrs/use-cannon) &ndash; physics based hooks
- [`@react-three/a11y`](https://github.com/pmndrs/react-three-a11y) &ndash; real a11y for your scene
- [`zustand`](https://github.com/pmndrs/zustand) &ndash; state management
- [`react-spring`](https://github.com/pmndrs/react-spring) &ndash; a spring-physics-based animation library
- [`react-use-gesture`](https://github.com/pmndrs/react-use-gesture) &ndash; mouse/touch gestures
- [`leva`](https://github.com/pmndrs/leva) &ndash; create GUI controls in seconds

## How to contribute
If you like this project, please consider helping out. All contributions are welcome as well as donations to [Opencollective](https://opencollective.com/react-three-fiber), or in crypto `BTC: 36fuguTPxGCNnYZSRdgdh6Ea94brCAjMbH`, `ETH: 0x6E3f79Ea1d0dcedeb33D3fC6c34d2B1f156F2682`.

## Backers
Thank you to all our backers! 🙏

## Contributors
This project exists thanks to all the people who contribute.

---

# iCloud: web-app/node_modules/@protobufjs/utf8/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/utf8/README.md
> **Analyzed At:** 2026-06-13T06:32:46.338Z

## API
---
* **utf8.length(string: `string`): `number`**
Calculates the UTF8 byte length of a string.
* **utf8.read(buffer: `Uint8Array`, start: `number`, end: `number`): `string`**
Reads UTF8 bytes as a string.
* **utf8.write(string: `string`, buffer: `Uint8Array`, offset: `number`): `number`**
Writes a string as UTF8 bytes.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/pool/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/pool/README.md
> **Analyzed At:** 2026-06-13T06:32:46.340Z

## API
---
* **pool(alloc: `function(size: number): Uint8Array`, slice: `function(this: Uint8Array, start: number, end: number): Uint8Array`, [size=8192: `number`]): `function(size: number): Uint8Array`**
Creates a pooled allocator.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/path/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/path/README.md
> **Analyzed At:** 2026-06-13T06:32:46.341Z

## API
---
* **path.isAbsolute(path: `string`): `boolean`**
Tests if the specified path is absolute.
* **path.normalize(path: `string`): `string`**
Normalizes the specified path.
* **path.resolve(originPath: `string`, includePath: `string`, [alreadyNormalized=false: `boolean`]): `string`**
Resolves the specified include path against the specified origin path.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/inquire/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/inquire/README.md
> **Analyzed At:** 2026-06-13T06:32:46.342Z

## API
---
* **inquire(moduleName: `string`): `?Object`**
Requires a module only if available.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/float/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/float/README.md
> **Analyzed At:** 2026-06-13T06:32:46.343Z

## API
---
* **writeFloatLE(val: `number`, buf: `Uint8Array`, pos: `number`)**
Writes a 32 bit float to a buffer using little endian byte order.
* **writeFloatBE(val: `number`, buf: `Uint8Array`, pos: `number`)**
Writes a 32 bit float to a buffer using big endian byte order.
* **readFloatLE(buf: `Uint8Array`, pos: `number`): `number`**
Reads a 32 bit float from a buffer using little endian byte order.
* **readFloatBE(buf: `Uint8Array`, pos: `number`): `number`**
Reads a 32 bit float from a buffer using big endian byte order.
* **writeDoubleLE(val: `number`, buf: `Uint8Array`, pos: `number`)**
Writes a 64 bit double to a buffer using little endian byte order.
* **writeDoubleBE(val: `number`, buf: `Uint8Array`, pos: `number`)**
Writes a 64 bit double to a buffer using big endian byte order.
* **readDoubleLE(buf: `Uint8Array`, pos: `number`): `number`**
Reads a 64 bit double from a buffer using little endian byte order.
* **readDoubleBE(buf: `Uint8Array`, pos: `number`): `number`**
Reads a 64 bit double from a buffer using big endian byte order.

## Performance
-----------
There is a simple benchmark included comparing raw read/write performance of this library (float), float's fallback for old browsers, the [ieee754](https://www.npmjs.com/package/ieee754) module and node's [buffer](https://nodejs.org/api/buffer.html). On an i7-2600k running node 6.9.1 it yields:
```
benchmarking writeFloat performance ...

float x 42,741,625 ops/sec ±1.75% (81 runs sampled)
float (fallback) x 11,272,532 ops/sec ±1.12% (85 runs sampled)
ieee754 x 8,653,337 ops/sec ±1.18% (84 runs sampled)
buffer x 12,412,414 ops/sec ±1.41% (83 runs sampled)
buffer (noAssert) x 13,471,149 ops/sec ±1.09% (84 runs sampled)

                      float was fastest
           float (fallback) was 73.5% slower
                    ieee754 was 79.6% slower
                     buffer was 70.9% slower
          buffer (noAssert) was 68.3% slower

benchmarking readFloat performance ...

float x 44,382,729 ops/sec ±1.70% (84 runs sampled)
float (fallback) x 20,925,938 ops/sec ±0.86% (87 runs sampled)
ieee754 x 17,189,009 ops/sec ±1.01% (87 runs sampled)
buffer x 10,518,437 ops/sec ±1.04% (83 runs sampled)
buffer (noAssert) x 11,031,636 ops/sec ±1.15% (87 runs sampled)

                      float was fastest
           float (fallback) was 52.5% slower
                    ieee754 was 61.0% slower
                     buffer was 76.1% slower
          buffer (noAssert) was 75.0% slower

benchmarking writeDouble performance ...

float x 38,624,906 ops/sec ±0.93% (83 runs sampled)
float (fallback) x 10,457,811 ops/sec ±1.54% (85 runs sampled)
ieee754 x 7,681,130 ops/sec ±1.11% (83 runs sampled)
buffer x 12,657,876 ops/sec ±1.03% (83 runs sampled)
buffer (noAssert) x 13,372,795 ops/sec ±0.84% (85 runs sampled)

                      float was fastest
           float (fallback) was 73.1% slower
                    ieee754 was 80.1% slower
                     buffer was 67.3% slower
          buffer (noAssert) was 65.3% slower

benchmarking readDouble performance ...

float x 40,527,888 ops/sec ±1.05% (84 runs sampled)
float (fallback) x 18,696,480 ops/sec ±0.84% (86 runs sampled)
ieee754 x 14,074,028 ops/sec ±1.04% (87 runs sampled)
buffer x 10,092,367 ops/sec ±1.15% (84 runs sampled)
buffer (noAssert) x 10,623,793 ops/sec ±0.96% (84 runs sampled)

                      float was fastest
           float (fallback) was 53.8% slower
                    ieee754 was 65.3% slower
                     buffer was 75.1% slower
          buffer (noAssert) was 73.8% slower
```
To run it yourself:
```
$> npm run bench
```
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/fetch/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/fetch/README.md
> **Analyzed At:** 2026-06-13T06:32:46.345Z

## API
---
Fetches the contents of a file.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/eventemitter/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/eventemitter/README.md
> **Analyzed At:** 2026-06-13T06:32:46.346Z

## API
---
* **new EventEmitter()**
Constructs a new event emitter instance.
* **EventEmitter#on(evt: `string`, fn: `function`, [ctx: `Object`]): `EventEmitter`**
Registers an event listener.
* **EventEmitter#off([evt: `string`], [fn: `function`]): `EventEmitter`**
Removes an event listener or any matching listeners if arguments are omitted.
* **EventEmitter#emit(evt: `string`, ...args: `*`): `EventEmitter`**
Emits an event by calling its listeners with the specified arguments.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/codegen/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/codegen/README.md
> **Analyzed At:** 2026-06-13T06:32:46.348Z

## API
---
* **codegen([functionParams: `string[]`], [functionName: string]): `Codegen`**
Begins generating a function.
* **codegen.verbose = `false`**
When set to true, codegen will log generated code to console. Useful for debugging.
Invoking **codegen** returns an appender function that appends code to the function's body and returns itself:
* **Codegen(formatString: `string`, [...formatParams: `any`]): Codegen**
Appends code to the function's body. The format string can contain placeholders specifying the types of inserted format parameters:
* `%d`: Number (integer or floating point value)
* `%f`: Floating point value
* `%i`: Integer value
* `%j`: JSON.stringify'ed value
* `%s`: String value
* `%%`: Percent sign
* **Codegen([scope: `Object.<string,*>`]): `Function`**
Finishes the function and returns it.
* **Codegen.toString([functionNameOverride: `string`]): `string`**
Returns the function as a string.

## Example
-------
```js
var codegen = require("@protobufjs/codegen");

var add = codegen(["a", "b"], "add") // A function with parameters "a" and "b" named "add"
  ("// awesome comment")             // adds the line to the function's body
  ("return a + b - c + %d", 1)       // replaces %d with 1 and adds the line to the body
  ({ c: 1 });                        // adds "c" with a value of 1 to the function's scope

console.log(add.toString()); // function add(a, b) { return a + b - c + 1 }
console.log(add(1, 2));      // calculates 1 + 2 - 1 + 1 = 3
```
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/base64/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/base64/README.md
> **Analyzed At:** 2026-06-13T06:32:46.349Z

## API
---
* **base64.length(string: `string`): `number`**
Calculates the byte length of a base64 encoded string.
* **base64.encode(buffer: `Uint8Array`, start: `number`, end: `number`): `string`**
Encodes a buffer to a base64 encoded string.
* **base64.decode(string: `string`, buffer: `Uint8Array`, offset: `number`): `number`**
Decodes a base64 encoded string to a buffer.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@protobufjs/aspromise/README.md

> **Source:** icloud://web-app/node_modules/@protobufjs/aspromise/README.md
> **Analyzed At:** 2026-06-13T06:32:46.350Z

## API
---
* **asPromise(fn: `function`, ctx: `Object`, ...params: `*`): `Promise`**
Returns a promise from a node-style callback function.
**License:** [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

---

# iCloud: web-app/node_modules/@pkgjs/parseargs/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@pkgjs/parseargs/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.352Z

## Features
* add `default` option parameter ([#142](https://github.com/pkgjs/parseargs/issues/142)) ([cd20847](https://github.com/pkgjs/parseargs/commit/cd20847a00b2f556aa9c085ac83b942c60868ec1))

## Features
* add parsed meta-data to returned properties ([#129](https://github.com/pkgjs/parseargs/issues/129)) ([91bfb4d](https://github.com/pkgjs/parseargs/commit/91bfb4d3f7b6937efab1b27c91c45d1205f1497e))

## Bug Fixes
* **runtime:** support node 14+ ([#135](https://github.com/pkgjs/parseargs/issues/135)) ([6a1c5a6](https://github.com/pkgjs/parseargs/commit/6a1c5a6f7cadf2f035e004027e2742e3c4ce554b))

## ⚠ BREAKING CHANGES
* drop handling of electron arguments (#121)

## Code Refactoring
* drop handling of electron arguments ([#121](https://github.com/pkgjs/parseargs/issues/121)) ([a2ffd53](https://github.com/pkgjs/parseargs/commit/a2ffd537c244a062371522b955acb45a404fc9f2))

## ⚠ BREAKING CHANGES
* switch type:string option arguments to greedy, but with error for suspect cases in strict mode (#88)
* positionals now opt-in when strict:true (#116)
* create result.values with null prototype (#111)

## Features
* create result.values with null prototype ([#111](https://github.com/pkgjs/parseargs/issues/111)) ([9d539c3](https://github.com/pkgjs/parseargs/commit/9d539c3d57f269c160e74e0656ad4fa84ff92ec2))
* positionals now opt-in when strict:true ([#116](https://github.com/pkgjs/parseargs/issues/116)) ([3643338](https://github.com/pkgjs/parseargs/commit/364333826b746e8a7dc5505b4b22fd19ac51df3b))
* switch type:string option arguments to greedy, but with error for suspect cases in strict mode ([#88](https://github.com/pkgjs/parseargs/issues/88)) ([c2b5e72](https://github.com/pkgjs/parseargs/commit/c2b5e72161991dfdc535909f1327cc9b970fe7e8))

## Bug Fixes
* resist pollution ([#106](https://github.com/pkgjs/parseargs/issues/106)) ([ecf2dec](https://github.com/pkgjs/parseargs/commit/ecf2dece0a9f2a76d789384d5d71c68ffe64022a))

## Features
* Add strict mode to parser ([#74](https://github.com/pkgjs/parseargs/issues/74)) ([8267d02](https://github.com/pkgjs/parseargs/commit/8267d02083a87b8b8a71fcce08348d1e031ea91c))

## ⚠ BREAKING CHANGES
* rework results to remove redundant `flags` property and store value true for boolean options (#83)
* switch to existing ERR_INVALID_ARG_VALUE (#97)

## Code Refactoring
* rework results to remove redundant `flags` property and store value true for boolean options ([#83](https://github.com/pkgjs/parseargs/issues/83)) ([be153db](https://github.com/pkgjs/parseargs/commit/be153dbed1d488cb7b6e27df92f601ba7337713d))
* switch to existing ERR_INVALID_ARG_VALUE ([#97](https://github.com/pkgjs/parseargs/issues/97)) ([084a23f](https://github.com/pkgjs/parseargs/commit/084a23f9fde2da030b159edb1c2385f24579ce40))

## ⚠ BREAKING CHANGES
* Require type to be specified for each supplied option (#95)

## Features
* Require type to be specified for each supplied option ([#95](https://github.com/pkgjs/parseargs/issues/95)) ([02cd018](https://github.com/pkgjs/parseargs/commit/02cd01885b8aaa59f2db8308f2d4479e64340068))

## ⚠ BREAKING CHANGES
* parsing, revisit short option groups, add support for combined short and value (#75)
* restructure configuration to take options bag (#63)

## Code Refactoring
* parsing, revisit short option groups, add support for combined short and value ([#75](https://github.com/pkgjs/parseargs/issues/75)) ([a92600f](https://github.com/pkgjs/parseargs/commit/a92600fa6c214508ab1e016fa55879a314f541af))
* restructure configuration to take options bag ([#63](https://github.com/pkgjs/parseargs/issues/63)) ([b412095](https://github.com/pkgjs/parseargs/commit/b4120957d90e809ee8b607b06e747d3e6a6b213e))

## Features
* **parser:** support short-option groups ([#59](https://github.com/pkgjs/parseargs/issues/59)) ([882067b](https://github.com/pkgjs/parseargs/commit/882067bc2d7cbc6b796f8e5a079a99bc99d4e6ba))

## Features
* basic support for shorts ([#50](https://github.com/pkgjs/parseargs/issues/50)) ([a2f36d7](https://github.com/pkgjs/parseargs/commit/a2f36d7da4145af1c92f76806b7fe2baf6beeceb))

## Bug Fixes
* always store value for a=b ([#43](https://github.com/pkgjs/parseargs/issues/43)) ([a85e8dc](https://github.com/pkgjs/parseargs/commit/a85e8dc06379fd2696ee195cc625de8fac6aee42))
* support single dash as positional ([#49](https://github.com/pkgjs/parseargs/issues/49)) ([d795bf8](https://github.com/pkgjs/parseargs/commit/d795bf877d068fd67aec381f30b30b63f97109ad))

## Bug Fixes
* only use arrays in results for multiples ([#42](https://github.com/pkgjs/parseargs/issues/42)) ([c357584](https://github.com/pkgjs/parseargs/commit/c357584847912506319ed34a0840080116f4fd65))

## Features
* expand scenarios covered by default arguments for environments ([#20](https://github.com/pkgjs/parseargs/issues/20)) ([582ada7](https://github.com/pkgjs/parseargs/commit/582ada7be0eca3a73d6e0bd016e7ace43449fa4c))
* update readme and include contributing guidelines ([8edd6fc](https://github.com/pkgjs/parseargs/commit/8edd6fc863cd705f6fac732724159ebe8065a2b0))

## Bug Fixes
* do not strip excess leading dashes on long option names ([#21](https://github.com/pkgjs/parseargs/issues/21)) ([f848590](https://github.com/pkgjs/parseargs/commit/f848590ebf3249ed5979ff47e003fa6e1a8ec5c0))
* name & readme ([3f057c1](https://github.com/pkgjs/parseargs/commit/3f057c1b158a1bdbe878c64b57460c58e56e465f))
* package.json values ([9bac300](https://github.com/pkgjs/parseargs/commit/9bac300e00cd76c77076bf9e75e44f8929512da9))
* update readme name ([957d8d9](https://github.com/pkgjs/parseargs/commit/957d8d96e1dcb48297c0a14345d44c0123b2883e))

## Build System
* first release as minor ([421c6e2](https://github.com/pkgjs/parseargs/commit/421c6e2569a8668ad14fac5a5af5be60479a7571))

---

# iCloud: web-app/node_modules/@pkgjs/parseargs/README.md

> **Source:** icloud://web-app/node_modules/@pkgjs/parseargs/README.md
> **Analyzed At:** 2026-06-13T06:32:46.354Z

## parseArgs
[![Coverage][coverage-image]][coverage-url]
Polyfill of `util.parseArgs()`

## `util.parseArgs([config])`
<!-- YAML
added: v18.3.0
changes:
- version: REPLACEME
pr-url: https://github.com/nodejs/node/pull/43459
description: add support for returning detailed parse information
using `tokens` in input `config` and returned properties.
-->
> Stability: 1 - Experimental
the parser. `config` supports the following properties:
with `execPath` and `filename` removed.
Keys of `options` are the long names of options and values are an
{Object} accepting the following properties:
times. If `true`, all values will be collected in an array. If
`false`, values for the option are last-wins. **Default:** `false`.
value when it is not set by args. It must be of the same type as the
the `type` property. When `multiple` is `true`, it must be an array.
are encountered, or when arguments are passed that do not match the
`type` configured in `options`.
**Default:** `true`.
arguments.
**Default:** `false` if `strict` is `true`, otherwise `true`.
the built-in behavior, from adding additional checks through to reprocessing
the tokens in different ways.
**Default:** `false`.
or {boolean} values.
* `positionals` {string\[]} Positional arguments.
section. Only returned if `config` includes `tokens: true`.
Provides a higher level API for command-line argument parsing than interacting
with `process.argv` directly. Takes a specification for the expected arguments
and returns a structured object with the parsed options and positionals.
```mjs
import { parseArgs } from 'node:util';
const args = ['-f', '--bar', 'b'];
const options = {
  foo: {
    type: 'boolean',
    short: 'f'
  },
  bar: {
    type: 'string'
  }
};
const {
  values,
  positionals
} = parseArgs({ args, options });
console.log(values, positionals);
// Prints: [Object: null prototype] { foo: true, bar: 'b' } []
```
```cjs
const { parseArgs } = require('node:util');
const args = ['-f', '--bar', 'b'];
const options = {
  foo: {
    type: 'boolean',
    short: 'f'
  },
  bar: {
    type: 'string'
  }
};
const {
  values,
  positionals
} = parseArgs({ args, options });
console.log(values, positionals);
// Prints: [Object: null prototype] { foo: true, bar: 'b' } []
```
`util.parseArgs` is experimental and behavior may change. Join the
conversation in [pkgjs/parseargs][] to contribute to the design.

## `parseArgs` `tokens`
Detailed parse information is available for adding custom behaviours by
specifying `tokens: true` in the configuration.
The returned tokens have properties describing:
* all tokens
source argument for a token is `args[token.index]`.
* option tokens
* `name` {string} Long name of option.
Undefined for boolean options.
like `--foo=bar`.
* positional tokens
* option-terminator token
The returned tokens are in the order encountered in the input args. Options
that appear more than once in args produce a token for each use. Short option
groups like `-xy` expand to a token for each option. So `-xxx` produces
three tokens.
For example to use the returned tokens to add support for a negated option
like `--no-color`, the tokens can be reprocessed to change the value stored
for the negated option.
```mjs
import { parseArgs } from 'node:util';

const options = {
  'color': { type: 'boolean' },
  'no-color': { type: 'boolean' },
  'logfile': { type: 'string' },
  'no-logfile': { type: 'boolean' },
};
const { values, tokens } = parseArgs({ options, tokens: true });

// Reprocess the option tokens and overwrite the returned values.
tokens
  .filter((token) => token.kind === 'option')
  .forEach((token) => {
    if (token.name.startsWith('no-')) {
      // Store foo:false for --no-foo
      const positiveName = token.name.slice(3);
      values[positiveName] = false;
      delete values[token.name];
    } else {
      // Resave value so last one wins if both --foo and --no-foo.
      values[token.name] = token.value ?? true;
    }
  });

const color = values.color;
const logfile = values.logfile ?? 'default.log';

console.log({ logfile, color });
```
```cjs
const { parseArgs } = require('node:util');

const options = {
  'color': { type: 'boolean' },
  'no-color': { type: 'boolean' },
  'logfile': { type: 'string' },
  'no-logfile': { type: 'boolean' },
};
const { values, tokens } = parseArgs({ options, tokens: true });

// Reprocess the option tokens and overwrite the returned values.
tokens
  .filter((token) => token.kind === 'option')
  .forEach((token) => {
    if (token.name.startsWith('no-')) {
      // Store foo:false for --no-foo
      const positiveName = token.name.slice(3);
      values[positiveName] = false;
      delete values[token.name];
    } else {
      // Resave value so last one wins if both --foo and --no-foo.
      values[token.name] = token.value ?? true;
    }
  });

const color = values.color;
const logfile = values.logfile ?? 'default.log';

console.log({ logfile, color });
```
Example usage showing negated options, and when an option is used
multiple ways then last one wins.
```console
$ node negate.js
{ logfile: 'default.log', color: undefined }
$ node negate.js --no-logfile --no-color
{ logfile: false, color: false }
$ node negate.js --logfile=test.log --color
{ logfile: 'test.log', color: true }
$ node negate.js --no-logfile --logfile=test.log --color --no-color
{ logfile: 'test.log', color: false }
```
-----

## Table of Contents
- [`util.parseArgs([config])`](#utilparseargsconfig)
- [Scope](#scope)
- [Version Matchups](#version-matchups)
- [🚀 Getting Started](#-getting-started)
- [🙌 Contributing](#-contributing)
- [💡 `process.mainArgs` Proposal](#-processmainargs-proposal)
- [Implementation:](#implementation)
- [📃 Examples](#-examples)
- [F.A.Qs](#faqs)
- [Links & Resources](#links--resources)
-----

## Scope
It is already possible to build great arg parsing modules on top of what Node.js provides; the prickly API is abstracted away by these modules. Thus, process.parseArgs() is not necessarily intended for library authors; it is intended for developers of simple CLI tools, ad-hoc scripts, deployed Node.js applications, and learning materials.
It is exceedingly difficult to provide an API which would both be friendly to these Node.js users while being extensible enough for libraries to build upon. We chose to prioritize these use cases because these are currently not well-served by Node.js' API.
----

## Version Matchups
| Node.js | @pkgjs/parseArgs |
| -- | -- |
| [v18.3.0](https://nodejs.org/docs/latest-v18.x/api/util.html#utilparseargsconfig) | [v0.9.1](https://github.com/pkgjs/parseargs/tree/v0.9.1#utilparseargsconfig) |
| [v16.17.0](https://nodejs.org/dist/latest-v16.x/docs/api/util.html#utilparseargsconfig), [v18.7.0](https://nodejs.org/docs/latest-v18.x/api/util.html#utilparseargsconfig) | [0.10.0](https://github.com/pkgjs/parseargs/tree/v0.10.0#utilparseargsconfig) |
----

## 🚀 Getting Started
1. **Install dependencies.**
   ```bash
   npm install
```
2. **Open the index.js file and start editing!**
3. **Test your code by calling parseArgs through our test file**
   ```bash
   npm test
```
----

## 🙌 Contributing
Any person who wants to contribute to the initiative is welcome! Please first read the [Contributing Guide](CONTRIBUTING.md)
Additionally, reading the [`Examples w/ Output`](#-examples-w-output) section of this document will be the best way to familiarize yourself with the target expected behavior for parseArgs() once it is fully implemented.
This package was implemented using [tape](https://www.npmjs.com/package/tape) as its test harness.
----

## 💡 `process.mainArgs` Proposal
> Note: This can be moved forward independently of the `util.parseArgs()` proposal/work.

## Implementation:
```javascript
process.mainArgs = process.argv.slice(process._exec ? 1 : 2)
```
----

## 📃 Examples
```js
const { parseArgs } = require('@pkgjs/parseargs');
```
```js
const { parseArgs } = require('@pkgjs/parseargs');
// specify the options that may be used
const options = {
  foo: { type: 'string'},
  bar: { type: 'boolean' },
};
const args = ['--foo=a', '--bar'];
const { values, positionals } = parseArgs({ args, options });
// values = { foo: 'a', bar: true }
// positionals = []
```
```js
const { parseArgs } = require('@pkgjs/parseargs');
// type:string & multiple
const options = {
  foo: {
    type: 'string',
    multiple: true,
  },
};
const args = ['--foo=a', '--foo', 'b'];
const { values, positionals } = parseArgs({ args, options });
// values = { foo: [ 'a', 'b' ] }
// positionals = []
```
```js
const { parseArgs } = require('@pkgjs/parseargs');
// shorts
const options = {
  foo: {
    short: 'f',
    type: 'boolean'
  },
};
const args = ['-f', 'b'];
const { values, positionals } = parseArgs({ args, options, allowPositionals: true });
// values = { foo: true }
// positionals = ['b']
```
```js
const { parseArgs } = require('@pkgjs/parseargs');
// unconfigured
const options = {};
const args = ['-f', '--foo=a', '--bar', 'b'];
const { values, positionals } = parseArgs({ strict: false, args, options, allowPositionals: true });
// values = { f: true, foo: 'a', bar: true }
// positionals = ['b']
```
----

## F.A.Qs
- Is `cmd --foo=bar baz` the same as `cmd baz --foo=bar`?
- yes
- Does the parser execute a function?
- no
- Does the parser execute one of several functions, depending on input?
- no
- Can subcommands take options that are distinct from the main command?
- no
- Does it output generated help when no options match?
- no
- Does it generated short usage?  Like: `usage: ls [-ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1] [file ...]`
- no (no usage/help at all)
- Does the user provide the long usage text?  For each option?  For the whole command?
- no
- Do subcommands (if implemented) have their own usage output?
- no
- Does usage print if the user runs `cmd --help`?
- no
- Does it set `process.exitCode`?
- no
- Does usage print to stderr or stdout?
- N/A
- Does it check types?  (Say, specify that an option is a boolean, number, etc.)
- no
- Can an option have more than one type?  (string or false, for example)
- no
- Can the user define a type?  (Say, `type: path` to call `path.resolve()` on the argument.)
- no
- Does a `--foo=0o22` mean 0, 22, 18, or "0o22"?
- `"0o22"`
- Does it coerce types?
- no
- Does `--no-foo` coerce to `--foo=false`?  For all options?  Only boolean options?
- no, it sets `{values:{'no-foo': true}}`
- Is `--foo` the same as `--foo=true`?  Only for known booleans?  Only at the end?
- no, they are not the same. There is no special handling of `true` as a value so it is just another string.
- Does it read environment variables?  Ie, is `FOO=1 cmd` the same as `cmd --foo=1`?
- no
- Do unknown arguments raise an error?  Are they parsed?  Are they treated as positional arguments?
- no, they are parsed, not treated as positionals
- Does `--` signal the end of options?
- yes
- Is `--` included as a positional?
- no
- Is `program -- foo` the same as `program foo`?
- yes, both store `{positionals:['foo']}`
- Does the API specify whether a `--` was present/relevant?
- no
- Is `-bar` the same as `--bar`?
- no, `-bar` is a short option or options, with expansion logic that follows the
[Utility Syntax Guidelines in POSIX.1-2017](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html). `-bar` expands to `-b`, `-a`, `-r`.
- Is `---foo` the same as `--foo`?
- no
- the first is a long option named `'-foo'`
- the second is a long option named `'foo'`
- Is `-` a positional? ie, `bash some-test.sh | tap -`
- yes

## Links & Resources
* [Initial Tooling Issue](https://github.com/nodejs/tooling/issues/19)
* [Initial Proposal](https://github.com/nodejs/node/pull/35015)
* [parseArgs Proposal](https://github.com/nodejs/node/pull/42675)
[coverage-image]: https://img.shields.io/nycrc/pkgjs/parseargs
[coverage-url]: https://github.com/pkgjs/parseargs/blob/main/.nycrc
[pkgjs/parseargs]: https://github.com/pkgjs/parseargs

---

# iCloud: web-app/node_modules/@opentelemetry/semantic-conventions/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/semantic-conventions/README.md
> **Analyzed At:** 2026-06-13T06:32:46.356Z

## OpenTelemetry Semantic Conventions
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
Semantic Convention constants for use with the OpenTelemetry SDK/APIs. [This document][trace-semantic_conventions] defines standard attributes for traces.

## Installation
```bash
npm install --save @opentelemetry/semantic-conventions
```

## Import Structure
This package has 2 separate entry-points:
- The main entry-point, `@opentelemetry/semantic-conventions`, includes only stable semantic conventions.
This entry-point follows semantic versioning 2.0: it will not include breaking changes except with a change in the major version number.
- The "incubating" entry-point, `@opentelemetry/semantic-conventions/incubating`, contains unstable semantic conventions (sometimes called "experimental") and, for convenience, a re-export of the stable semantic conventions.
This entry-point is _NOT_ subject to the restrictions of semantic versioning and _MAY_ contain breaking changes in minor releases. See below for suggested usage of this entry-point.
Exported constants follow this naming scheme:
- `ATTR_${attributeName}` for attributes
- `METRIC_${metricName}` for metric names
- `EVENT_${eventName}` for event names
The `ATTR`, `METRIC`, `EVENT`, and `VALUE` static strings were used to facilitate readability and filtering in auto-complete lists in IDEs.

## Stable SemConv
```bash
npm install --save @opentelemetry/semantic-conventions
```
```ts
import {
  ATTR_NETWORK_PEER_ADDRESS,
  ATTR_NETWORK_PEER_PORT,
  ATTR_NETWORK_PROTOCOL_NAME,
  ATTR_NETWORK_PROTOCOL_VERSION,
  NETWORK_TRANSPORT_VALUE_TCP,
} from '@opentelemetry/semantic-conventions';

const span = tracer.startSpan(spanName, spanOptions)
  .setAttributes({
    [ATTR_NETWORK_PEER_ADDRESS]: 'localhost',
    [ATTR_NETWORK_PEER_PORT]: 8080,
    [ATTR_NETWORK_PROTOCOL_NAME]: 'http',
    [ATTR_NETWORK_PROTOCOL_VERSION]: '1.1',
    [ATTR_NETWORK_TRANSPORT]: NETWORK_TRANSPORT_VALUE_TCP,
  });
```

## Unstable SemConv
Because the "incubating" entry-point may include breaking changes in minor versions, it is recommended that instrumentation libraries **not** import `@opentelemetry/semantic-conventions/incubating` in runtime code, but instead **copy relevant definitions into their own code base**. (This is the same [recommendation](https://opentelemetry.io/docs/specs/semconv/non-normative/code-generation/#stability-and-versioning) as for other languages.)
For example, create a "src/semconv.ts" (or "lib/semconv.js" if implementing in JavaScript) file that copies from [experimental_attributes.ts](./src/experimental_attributes.ts) or [experimental_metrics.ts](./src/experimental_metrics.ts):
```ts
// src/semconv.ts
export const ATTR_DB_NAMESPACE = 'db.namespace';
export const ATTR_DB_OPERATION_NAME = 'db.operation.name';
```
```ts
// src/instrumentation.ts
import {
  ATTR_SERVER_PORT,
  ATTR_SERVER_ADDRESS,
} from '@opentelemetry/semantic-conventions';
import {
  ATTR_DB_NAMESPACE,
  ATTR_DB_OPERATION_NAME,
} from './semconv';

span.setAttributes({
  [ATTR_DB_NAMESPACE]: ...,
  [ATTR_DB_OPERATION_NAME]: ...,
  [ATTR_SERVER_PORT]: ...,
  [ATTR_SERVER_ADDRESS]: ...,
})
```
Occasionally, one should review changes to `@opentelemetry/semantic-conventions` to see if any used unstable conventions have changed or been stabilized. However, an update to a newer minor version of the package will never be breaking.

## Why not pin the version?
A considered alternative for using unstable exports is to **pin** the version. I.e., depend on an exact version, rather than on a version range.
```bash
npm install --save-exact @opentelemetry/semantic-conventions  # Don't do this.
```
Then, import directly from `@opentelemetry/semantic-conventions/incubating`.
This is **not** recommended.
In some languages having multiple versions of a package in a single application is not possible. This _is_ possible in JavaScript. The primary argument against pinning this package is that it can easily lead to many copies being installed in an application's `node_modules/...`, which can cause significant disk usage. In a disk-constrained environment, such as AWS Lambda Layers, that can be a blocker.

## Deprecations
There are two main types of deprecations in this package:
1. "semconv deprecations": The process of defining the OpenTelemetry [Semantic Conventions][semconv-docs] sometimes involves deprecating a particular field name as conventions are [stabilized][semconv-stability]. For example, the [stabilization of HTTP conventions][semconv-http-stabilization] included deprecating the `http.url` span attribute in favor of `url.full`. When using this JS package, that appears as a deprecation of the `ATTR_HTTP_URL` export in favour of `ATTR_URL_FULL`.
2. "JS package deprecations": Independently, this JavaScript package has twice changed how it exports the Semantic Conventions constants, e.g. `ATTR_HTTP_URL` instead of `SEMATTRS_HTTP_URL`. The two older forms are still included in 1.x versions of this package for backwards compatibility. The rest of this section shows how to migrate to the latest form.

## Migrating from `SEMATTRS_*`, `SEMRESATTRS_*`, ...
Deprecated as of `@opentelemetry/semantic-conventions@1.26.0`.
**Deprecated usage:**
```js
import {
  SEMRESATTRS_SERVICE_NAME,
  SEMATTRS_HTTP_ROUTE,
  SEMATTRS_DB_SYSTEM,
  DBSYSTEMVALUES_POSTGRESQL
} from '@opentelemetry/semantic-conventions';

// 'service.name' resource attribute
console.log(SEMRESATTRS_SERVICE_NAME); // migrate to 'ATTR_SERVICE_NAME'

// 'http.route' attribute
console.log(SEMATTRS_HTTP_ROUTE); // migrate to 'ATTR_HTTP_ROUTE'

// 'db.system' attribute
console.log(SEMATTRS_DB_SYSTEM); // migrate to 'ATTR_DB_SYSTEM' (in incubating [*])

// 'postgresql' enum value for 'db.system' attribute
console.log(DBSYSTEMVALUES_POSTGRESQL); // migrate to 'DB_SYSTEM_VALUE_POSTGRESQL' (in incubating [*])
```
See [Migrated usage](#migrated-usage) below.

## Migrating from `SemanticAttributes.*`, `SemanticResourceAttributes.*`, ...
Deprecated as of `@opentelemetry/semantic-conventions@1.0.0`.
Before v1.0.0, constants were exported in namespace objects `SemanticResourceAttributes` and `SemanticAttributes`, and a namespace object for enumerated values for some fields (e.g. `DbSystemValues` for values of the 'db.system' enum). For example:
**Deprecated usage:**
```js
import {
  SemanticAttributes,
  SemanticResourceAttributes,
  DbSystemValues,
} from '@opentelemetry/semantic-conventions';

// 'service.name' resource attribute
console.log(SemanticResourceAttributes.SERVICE_NAME); // migrate to 'ATTR_SERVICE_NAME'

// 'http.route' attribute
console.log(SemanticAttributes.HTTP_ROUTE); // migrate to 'ATTR_HTTP_ROUTE'

// 'db.system' attribute
console.log(SemanticAttributes.DB_SYSTEM); // migrate to 'ATTR_DB_SYSTEM' (in incubating [*])

// 'postgresql' enum value for 'db.system' attribute
console.log(DbSystemValues.POSTGRESQL); // migrate to 'DB_SYSTEM_VALUE_POSTGRESQL' (in incubating [*])
```
See [Migrated usage](#migrated-usage) below.

## Migrated usage
If using any unstable conventions, copy the relevant definitions into your code base (e.g. to "src/semconv.ts", see [above](#unstable-semconv)):
```ts
// src/semconv.ts
export const ATTR_DB_SYSTEM = 'db.system' as const;
export const DB_SYSTEM_VALUE_POSTGRESQL = "postgresql" as const;
```
then:
```js
import {
  ATTR_SERVICE_NAME,
  ATTR_HTTP_ROUTE,
  METRIC_HTTP_CLIENT_REQUEST_DURATION
} from '@opentelemetry/semantic-conventions'; // stable semconv
import {
  ATTR_DB_SYSTEM,
  DB_SYSTEM_VALUE_POSTGRESQL
} from './semconv'; // unstable semconv

console.log(ATTR_SERVICE_NAME); // 'service.name'
console.log(ATTR_HTTP_ROUTE);   // 'http.route'

// Bonus: the older exports did not include metric names from semconv.
// 'http.client.request.duration' metric name
console.log(METRIC_HTTP_CLIENT_REQUEST_DURATION);

console.log(ATTR_DB_SYSTEM);    // 'db.system'
// 'postgresql' enum value for 'db.system' attribute
console.log(DB_SYSTEM_VALUE_POSTGRESQL);
```

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[npm-url]: https://www.npmjs.com/package/@opentelemetry/semantic-conventions
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Fsemantic-conventions.svg
[semconv-docs]: https://github.com/open-telemetry/semantic-conventions/blob/main/docs/README.md
[semconv-stability]: https://opentelemetry.io/docs/specs/otel/versioning-and-stability/#semantic-conventions-stability
[semconv-http-stabilization]: https://opentelemetry.io/blog/2023/http-conventions-declared-stable/
[trace-semantic_conventions]: https://github.com/open-telemetry/semantic-conventions/tree/main/specification/trace/semantic_conventions

---

# iCloud: web-app/node_modules/@opentelemetry/sdk-trace-node/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/sdk-trace-node/README.md
> **Analyzed At:** 2026-06-13T06:32:46.365Z

## OpenTelemetry Node SDK
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
This module provides *automated instrumentation and tracing* for Node.js applications.
For manual instrumentation see the
[@opentelemetry/sdk-trace-base](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-sdk-trace-base) package.
**Note: Much of OpenTelemetry JS documentation is written assuming the compiled application is run as CommonJS.**
For more details on ECMAScript Modules vs CommonJS, refer to [esm-support](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/esm-support.md).

## How auto instrumentation works
This package exposes a `NodeTracerProvider`.
For loading instrumentations please use `registerInstrumentations` function from [opentelemetry-instrumentation](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation)
OpenTelemetry comes with a growing number of instrumentation plugins for well known modules (see [supported modules](https://github.com/open-telemetry/opentelemetry-js#instrumentations)) and an API to create custom instrumentation (see [the instrumentation developer guide](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/instrumentation-guide.md)).
> **Please note:** This module does *not* bundle any plugins. They need to be installed separately.
This is done by wrapping all tracing-relevant functions.
This instrumentation code will automatically
- extract a trace-context identifier from inbound requests to allow distributed tracing (if applicable)
- make sure that this current trace-context is propagated while the transaction traverses an application (see [context document in @opentelemetry/api][def-context] for an in-depth explanation)
- add this trace-context identifier to outbound requests to allow continuing the distributed trace on the next hop (if applicable)
- create and end spans

## Creating custom spans on top of auto-instrumentation
Additionally to automated instrumentation, `NodeTracerProvider` exposes the same API as [@opentelemetry/sdk-trace-base](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-sdk-trace-base), allowing creating custom spans if needed.

## Installation
```bash
npm install --save @opentelemetry/api
npm install --save @opentelemetry/sdk-trace-node

# Install instrumentation plugins
npm install --save @opentelemetry/instrumentation-http
# and for example one additional
npm install --save @opentelemetry/instrumentation-graphql
```

## Usage
The following code will configure the `NodeTracerProvider` to instrument `http`
(and any other installed [supported
modules](https://github.com/open-telemetry/opentelemetry-js#plugins))
using `@opentelemetry/plugin-http`.
```javascript
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');

// Create and configure NodeTracerProvider
const provider = new NodeTracerProvider();

// Initialize the provider
provider.register();

// register and load instrumentation and old plugins - old plugins will be loaded automatically as previously
// but instrumentations needs to be added
registerInstrumentations({
});

// Your application code - http will automatically be instrumented if
// @opentelemetry/plugin-http is present
const http = require('http');
```

## Instrumentation configuration
In the following example:
- the express instrumentation is enabled
- the http instrumentation has a custom config for a `requestHook`
```javascript
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express');

const provider = new NodeTracerProvider();
provider.register();

// register and load instrumentation and old plugins - old plugins will be loaded automatically as previously
// but instrumentations needs to be added
registerInstrumentations({
  instrumentations: [
    new ExpressInstrumentation(),
    new HttpInstrumentation({
        requestHook: (span, request) => {
          span.setAttribute("custom request hook attribute", "request");
        },
    }),
  ],
});


```

## Examples
See how to automatically instrument [http](https://github.com/open-telemetry/opentelemetry-js/tree/main/examples/http) and [gRPC](https://github.com/open-telemetry/opentelemetry-js/tree/main/examples/grpc) / [grpc-js](https://github.com/open-telemetry/opentelemetry-js/tree/main/examples/grpc-js) using node-sdk.

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[def-context]: https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/context.md
[npm-url]: https://www.npmjs.com/package/@opentelemetry/sdk-trace-node
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Fsdk-trace-node.svg

---

# iCloud: web-app/node_modules/@opentelemetry/sdk-trace-base/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/sdk-trace-base/README.md
> **Analyzed At:** 2026-06-13T06:32:46.368Z

## OpenTelemetry Tracing SDK
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
The `tracing` module contains the foundation for all tracing SDKs of [opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js).
Used standalone, this module provides methods for manual instrumentation of code, offering full control over span creation for client-side JavaScript (browser) and Node.js.
It does **not** provide automated instrumentation of known libraries, context propagation or distributed-context out-of-the-box.
For a `TracerProvider` that includes default context management and propagation for Node.js, please see
[@opentelemetry/sdk-trace-node](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-sdk-trace-node).
For a `TracerProvider` that includes default context management and propagation for Browser, please see
[@opentelemetry/sdk-trace-web](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-sdk-trace-web).

## Installation
```bash
npm install --save @opentelemetry/api
npm install --save @opentelemetry/sdk-trace-base
```

## Usage
```js
const { trace } = require('@opentelemetry/api');
const { BasicTracerProvider } = require('@opentelemetry/sdk-trace-base');

// To start a trace, you first need to initialize the Tracer provider.
// NOTE: The default OpenTelemetry tracer provider does not record any tracing information.
//       Registering a working tracer provider allows the API methods to record traces.
trace.setGlobalTracerProvider(new BasicTracerProvider());

// Important: requires a context manager and propagator to be registered manually.
// propagation.setGlobalPropagator(propagator);     // replace `propagator` with your `TextMapPropagator`, for example: `W3CTraceContextPropagator` from `@openetelemetry/core`
// context.setGlobalContextManager(contextManager); // replace `contextManager` with your `ContextManager`: `AsyncLocalStorageContextManager` from `@openetelemetry/async-hooks`

// To create a span in a trace, we used the global singleton tracer to start a new span.
const span = trace.getTracer('default').startSpan('foo');

// Set a span attribute
span.setAttribute('key', 'value');

// We must end the spans so they become available for exporting.
span.end();
```

## Config
Tracing configuration is a merge of user supplied configuration with both the default
configuration as specified in [config.ts](./src/config.ts) and an
environmentally configurable sampling (via `OTEL_TRACES_SAMPLER` and `OTEL_TRACES_SAMPLER_ARG`).

## Built-in Samplers
Sampler is used to make decisions on `Span` sampling.

## AlwaysOn Sampler
Samples every trace regardless of upstream sampling decisions.
> This is used as a default Sampler
```js
const {
  AlwaysOnSampler,
  BasicTracerProvider,
} = require("@opentelemetry/sdk-trace-base");

const tracerProvider = new BasicTracerProvider({
  sampler: new AlwaysOnSampler()
});
```

## AlwaysOff Sampler
Doesn't sample any trace, regardless of upstream sampling decisions.
```js
const {
  AlwaysOffSampler,
  BasicTracerProvider,
} = require("@opentelemetry/sdk-trace-base");

const tracerProvider = new BasicTracerProvider({
  sampler: new AlwaysOffSampler()
});
```

## TraceIdRatioBased Sampler
Samples some percentage of traces, calculated deterministically using the trace ID.
Any trace that would be sampled at a given percentage will also be sampled at any higher percentage.
The `TraceIDRatioSampler` may be used with the `ParentBasedSampler` to respect the sampled flag of an incoming trace.
```js
const {
  BasicTracerProvider,
  TraceIdRatioBasedSampler,
} = require("@opentelemetry/sdk-trace-base");

const tracerProvider = new BasicTracerProvider({
  // See details of ParentBasedSampler below
  sampler: new ParentBasedSampler({
    // Trace ID Ratio Sampler accepts a positional argument
    // which represents the percentage of traces which should
    // be sampled.
    root: new TraceIdRatioBasedSampler(0.5)
  });
});
```

## ParentBased Sampler
- This is a composite sampler. `ParentBased` helps distinguished between the
following cases:
- No parent (root span).
- Remote parent with `sampled` flag `true`
- Remote parent with `sampled` flag `false`
- Local parent with `sampled` flag `true`
- Local parent with `sampled` flag `false`
Required parameters:
- `root(Sampler)` - Sampler called for spans with no parent (root spans)
Optional parameters:
- `remoteParentSampled(Sampler)` (default: `AlwaysOn`)
- `remoteParentNotSampled(Sampler)` (default: `AlwaysOff`)
- `localParentSampled(Sampler)` (default: `AlwaysOn`)
- `localParentNotSampled(Sampler)` (default: `AlwaysOff`)
|Parent|parent.isRemote()|parent.isSampled()|Invoke sampler|
|---|---|---|---|
|absent|n/a|n/a|`root()`|
|present|true|true|`remoteParentSampled()`|
|present|true|false|`remoteParentNotSampled()`|
|present|false|true|`localParentSampled()`|
|present|false|false|`localParentNotSampled()`|
```js
const {
  AlwaysOffSampler,
  BasicTracerProvider,
  ParentBasedSampler,
  TraceIdRatioBasedSampler,
} = require("@opentelemetry/sdk-trace-base");

const tracerProvider = new BasicTracerProvider({
  sampler: new ParentBasedSampler({
    // By default, the ParentBasedSampler will respect the parent span's sampling
    // decision. This is configurable by providing a different sampler to use
    // based on the situation. See configuration details above.
    //
    // This will delegate the sampling decision of all root traces (no parent)
    // to the TraceIdRatioBasedSampler.
    // See details of TraceIdRatioBasedSampler above.
    root: new TraceIdRatioBasedSampler(0.5)
  })
});
```

## Example
See [examples/basic-tracer-node](https://github.com/open-telemetry/opentelemetry-js/tree/main/examples/basic-tracer-node) for an end-to-end example, including exporting created spans.

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[npm-url]: https://www.npmjs.com/package/@opentelemetry/sdk-trace-base
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Fsdk-trace-base.svg

---

# iCloud: web-app/node_modules/@opentelemetry/resources/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/resources/README.md
> **Analyzed At:** 2026-06-13T06:32:46.380Z

## OpenTelemetry Resources Util
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
The OpenTelemetry Resource is an immutable representation of the entity producing telemetry. For example, a process producing telemetry that is running in a container on Kubernetes has a Pod name, it is in a namespace and possibly is part of a Deployment which also has a name. All three of these attributes can be included in the `Resource`.
[This document][resource-semantic_conventions] defines standard attributes for resources which are accessible via [`@opentelemetry/semantic-conventions`](https://github.com/open-telemetry/opentelemetry-js/tree/main/semantic-conventions).

## Installation
```bash
npm install --save @opentelemetry/resources
```

## Usage
```typescript
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions';
import { resourceFromAttributes } from '@opentelemetry/resources';

const resource = resourceFromAttributes({
    [ATTR_SERVICE_NAME]: 'api-service',
});

const anotherResource = resourceFromAttributes({
    'service.version': '2.0.0',
    'service.group': 'instrumentation-group'
});
const mergedResource = resource.merge(anotherResource);
```

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[npm-url]: https://www.npmjs.com/package/@opentelemetry/resources
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Fresources.svg
[resource-semantic_conventions]: https://github.com/open-telemetry/opentelemetry-specification/tree/master/specification/resource/semantic_conventions

---

# iCloud: web-app/node_modules/@opentelemetry/instrumentation/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/instrumentation/README.md
> **Analyzed At:** 2026-06-13T06:32:46.391Z

## OpenTelemetry Instrumentation for web and node
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
**Note: This is an experimental package under active development. New releases may include breaking changes.**

## Installation
**Note: Much of OpenTelemetry JS documentation is written assuming the compiled application is run as CommonJS.**
For more details on ECMAScript Modules vs CommonJS, refer to [esm-support](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/esm-support.md).
```bash
npm install --save @opentelemetry/instrumentation
```

## Usage in Node
```typescript
import {
  InstrumentationBase,
  InstrumentationConfig,
  InstrumentationNodeModuleDefinition,
  InstrumentationNodeModuleFile,
} from '@opentelemetry/instrumentation';

import type * as module_name_to_be_patched from 'module_name_to_be_patched';

export class MyInstrumentation extends InstrumentationBase {
  constructor(config: InstrumentationConfig = {}) {
    super('MyInstrumentation', VERSION, config);
  }

  /**
   * Init method will be called when the plugin is constructed.
   * It returns an `InstrumentationNodeModuleDefinition` which describes
   *   the node module to be instrumented and patched.
   * It may also return a list of `InstrumentationNodeModuleDefinition`s if
   *   the plugin should patch multiple modules or versions.
   */
  protected init() {
    const module = new InstrumentationNodeModuleDefinition(
      'module_name_to_be_patched',
      ['1.*'],
       this._onPatchMain,
       this._onUnPatchMain,
    );
    // in case you need to patch additional files - this is optional
    module.files.push(this._addPatchingMethod());

    return module;
    // you can also define more modules then just return an array of modules
    // return [module1, module2, ....]
  }

  private _onPatchMain(moduleExports: typeof module_name_to_be_patched) {
    this._wrap(
      moduleExports,
      'mainMethodName',
      this._patchMainMethodName()
    );
    return moduleExports;
  }

  private _onUnPatchMain(moduleExports: typeof module_name_to_be_patched) {
    this._unwrap(moduleExports, 'mainMethodName');
  }

  private _addPatchingMethod(): InstrumentationNodeModuleFile {
    const file = new InstrumentationNodeModuleFile(
      'module_name_to_be_patched/src/some_file.js',
      this._onPatchMethodName,
      this._onUnPatchMethodName,
    );
    return file;
  }

  private _onPatchMethodName(moduleExports: typeof module_name_to_be_patched) {
    this._wrap(
      moduleExports,
      'methodName',
      this._patchMethodName()
    );
    return moduleExports;
  }

  private _onUnPatchMethodName(moduleExports: typeof module_name_to_be_patched) {
    this._unwrap(moduleExports, 'methodName');
  }

  private _patchMethodName(): (original) => any {
    const plugin = this;
    return function methodName(original) {
      return function patchMethodName(this: any): PromiseOrValue<module_name_to_be_patched.methodName> {
        console.log('methodName', arguments);
        return original.apply(this, arguments);
      };
    };
  }

  private _patchMainMethodName(): (original) => any {
    const plugin = this;
    return function mainMethodName(original) {
      return function patchMainMethodName(this: any): PromiseOrValue<module_name_to_be_patched.mainMethodName> {
        console.log('mainMethodName', arguments);
        return original.apply(this, arguments);
      };
    };
  }
}

// Later, but before the module to instrument is required

const myInstrumentation = new MyInstrumentation();
myInstrumentation.setTracerProvider(provider); // this is optional, only if global TracerProvider shouldn't be used
myInstrumentation.setMeterProvider(meterProvider); // this is optional
myInstrumentation.enable();
// or use Auto Loader
```

## Usage in Web
```typescript
import {
  InstrumentationBase,
  InstrumentationConfig,
} from '@opentelemetry/instrumentation';

import { Instrumentation } from '@opentelemetry/instrumentation';

export class MyInstrumentation extends InstrumentationBase {
  constructor(config: InstrumentationConfig = {}) {
    super('MyInstrumentation', VERSION, config);
  }

  private _patchOpen() {
    return (original: OpenFunction): OpenFunction => {
      const plugin = this;
      return function patchOpen(this: XMLHttpRequest, ...args): void {
        console.log('open', arguments);
        return original.apply(this, args);
      };
    };
  }

  public enable() {
    this._wrap(XMLHttpRequest.prototype, 'open', this._patchOpen());
  }
  public disable() {
    this._unwrap(XMLHttpRequest.prototype, 'open');
  }
}

// Later

const myInstrumentation = new MyInstrumentation();
myInstrumentation.setTracerProvider(provider); // this is optional, only if global TracerProvider shouldn't be used
myInstrumentation.setMeterProvider(meterProvider); // this is optional, only if global MeterProvider shouldn't be used
myInstrumentation.enable();
// or use Auto Loader
```

## NODE - Auto Loader
```javascript
const { B3Propagator } = require('@opentelemetry/propagator-b3');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');

const tracerProvider = new NodeTracerProvider();

tracerProvider.register({
  propagator: new B3Propagator(),
});

registerInstrumentations({
  instrumentations: [
    new HttpInstrumentation(),
  ],
  //tracerProvider: tracerProvider, // optional, only if global TracerProvider shouldn't be used
  //meterProvider: meterProvider, // optional, only if global MeterProvider shouldn't be used
});

```

## WEB - Auto Loader
```javascript
const { B3Propagator } = require('@opentelemetry/propagator-b3');
const { registerInstrumentations } = require('@opentelemetry/instrumentation');
const { XMLHttpRequestInstrumentation } = require('@opentelemetry/instrumentation-xml-http-request');
const { WebTracerProvider } = require('@opentelemetry/sdk-trace-web');

const tracerProvider = new WebTracerProvider();

tracerProvider.register({
  propagator: new B3Propagator(),
});

registerInstrumentations({
  instrumentations: [
    new XMLHttpRequestInstrumentation({
      ignoreUrls: [/localhost/],
      propagateTraceHeaderCorsUrls: [
        'http://localhost:8090',
      ],
    }),
  ],
  //tracerProvider: tracerProvider, // optional, only if global TracerProvider shouldn't be used
  //meterProvider: meterProvider, // optional, only if global MeterProvider shouldn't be used
});
```

## Selection of the used TracerProvider/MeterProvider
The `registerInstrumentations()` API allows to specify which `TracerProvider` and/or `MeterProvider` to use by the given options object.
If nothing is specified the global registered provider is used. Usually this is what most users want therefore it's recommended to keep this default.
There might be use case where someone has the need for more providers within an application. Please note that special care must be takes in such setups
to avoid leaking information from one provider to the other because there are a lot places where e.g. the global `ContextManager` or `Propagator` is used.

## Instrumentation for ECMAScript Modules (ESM) in Node.js (experimental)
Node.js uses a different module loader for ECMAScript Modules (ESM) vs. CommonJS (CJS).
A `require()` call will cause Node.js to use the CommonJS module loader.
An `import ...` statement or `import()` call will cause Node.js to use the ECMAScript module loader.
If your application is written in JavaScript as ESM, or it must compile to ESM from TypeScript, then a loader hook is required to properly patch instrumentation.
The custom hook for ESM instrumentation is `--experimental-loader=@opentelemetry/instrumentation/hook.mjs`.
This flag must be passed to the `node` binary, which is often done as a startup command and/or in the `NODE_OPTIONS` environment variable.
For more details on ECMAScript Modules vs CommonJS, refer to [esm-support](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/esm-support.md).

## Limitations
Instrumentations for external modules (e.g. express, mongodb,...) hooks the `require` call or `import` statement. Therefore following conditions need to be met that this mechanism can work:
- Instrumentations are registered **before** the module to instrument is `require`ed (CJS only)
- modules are not included in a bundle. Tools like `esbuild`, `webpack`, ... usually have some mechanism to exclude specific modules from bundling

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
Third-party licenses and copyright notices can be found in the [LICENSES directory](./LICENSES).

## Useful links
- For more information on OpenTelemetry, visit: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[npm-url]: https://www.npmjs.com/package/@opentelemetry/instrumentation
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Finstrumentation.svg

---

# iCloud: web-app/node_modules/@opentelemetry/core/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/core/README.md
> **Analyzed At:** 2026-06-13T06:32:46.398Z

## OpenTelemetry Core
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
This package provides default implementations of the OpenTelemetry API for trace and metrics. It's intended for use both on the server and in the browser.

## Built-in Implementations
- [OpenTelemetry Core](#opentelemetry-core)
- [Built-in Implementations](#built-in-implementations)
- [Built-in Propagators](#built-in-propagators)
- [W3CTraceContextPropagator Propagator](#w3ctracecontextpropagator-propagator)
- [Composite Propagator](#composite-propagator)
- [Baggage Propagator](#baggage-propagator)
- [Useful links](#useful-links)
- [License](#license)

## W3CTraceContextPropagator Propagator
OpenTelemetry provides a text-based approach to propagate context to remote services using the [W3C Trace Context](https://www.w3.org/TR/trace-context/) HTTP headers.
```js
const api = require("@opentelemetry/api");
const { W3CTraceContextPropagator } = require("@opentelemetry/core");

/* Set Global Propagator */
api.propagation.setGlobalPropagator(new W3CTraceContextPropagator());
```

## Composite Propagator
Combines multiple propagators into a single propagator.
> This is used as a default Propagator
```js
const api = require("@opentelemetry/api");
const { CompositePropagator } = require("@opentelemetry/core");

/* Set Global Propagator */
api.propagation.setGlobalPropagator(new CompositePropagator());
```

## Baggage Propagator
Provides a text-based approach to propagate [baggage](https://w3c.github.io/baggage/) to remote services using the [OpenTelemetry Baggage Propagation](https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/baggage/api.md#baggage-propagation) HTTP headers.
```js
const api = require("@opentelemetry/api");
const { W3CBaggagePropagator } = require("@opentelemetry/core");

/* Set Global Propagator */
api.propagation.setGlobalPropagator(new W3CBaggagePropagator());
```

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[npm-url]: https://www.npmjs.com/package/@opentelemetry/core
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Fcore.svg

---

# iCloud: web-app/node_modules/@opentelemetry/context-async-hooks/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/context-async-hooks/README.md
> **Analyzed At:** 2026-06-13T06:32:46.411Z

## OpenTelemetry async_hooks-based Context Managers
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
This package provides two [`ContextManager`](https://open-telemetry.github.io/opentelemetry-js/interfaces/_opentelemetry_api.ContextManager.html) implementations built on APIs from Node.js's [`async_hooks`][async-hooks-doc] module. If you're looking for a `ContextManager` to use in browser environments, consider [opentelemetry-context-zone](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-context-zone) or [opentelemetry-context-zone-peer-dep](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-context-zone-peer-dep).
See [the definition of the `ContextManager` interface][def-context-manager] and the problem it solves.

## API
Two `ContextManager` implementations are exported:
- `AsyncLocalStorageContextManager`, based on [`AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage)
- `AsyncHooksContextManager`, based on [`AsyncHook`](https://nodejs.org/api/async_hooks.html#async_hooks_class_asynchook). This is **deprecated** and will be removed in v3 (planned for mid-2025. `AsyncLocalStorage` is simpler, faster, available in Node.js v14.8.0 and later, and avoids [this possible DoS vulnerability](https://nodejs.org/en/blog/vulnerability/january-2026-dos-mitigation-async-hooks).

## Prior art
Context propagation is a big subject when talking about tracing in Node.js. If you want more information about it here are some resources:
-  (which was the old way of doing context propagation)
- [Datadog's own implementation][dd-js-tracer-scope] for their JavaScript tracer
- [OpenTracing implementation][opentracing-scope]
- [Discussion about context propagation][diag-team-scope-discussion] by the Node.js Diagnostics Working Group

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[def-context-manager]: https://opentelemetry.io/docs/instrumentation/js/api/context/#context-manager
[dd-js-tracer-scope]: https://github.com/DataDog/dd-trace-js/blob/master/packages/dd-trace/src/scope.js
[opentracing-scope]: https://github.com/opentracing/opentracing-javascript/pull/113
[diag-team-scope-discussion]: https://github.com/nodejs/diagnostics/issues/300
[npm-url]: https://www.npmjs.com/package/@opentelemetry/context-async-hooks
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Fcontext-async-hooks.svg

---

# iCloud: web-app/node_modules/@opentelemetry/api-logs/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/api-logs/README.md
> **Analyzed At:** 2026-06-13T06:32:46.413Z

## OpenTelemetry Logs Bridge API for JavaScript
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
**Note: This is an experimental package under active development. New releases may include breaking changes.**
This package provides everything needed to interact with the unstable OpenTelemetry Logs Bridge API, including all TypeScript interfaces, enums, and no-op implementations. It is intended for use both on the server and in the browser.
**Note: This module defines a log backend API. The API is not intended to be called by application developers directly.
It is provided for logging library authors to build log appenders, which use this API to bridge between existing
logging libraries and the OpenTelemetry log data model.**

## Alpha Software - Use at your own risk
The Logs Bridge API is considered alpha software and there is no guarantee of stability or long-term support. When the API is stabilized, it will be made available and supported long-term in the `@opentelemetry/api` package and this package will be deprecated.

## Quick Start
Purposefully left blank until SDK is available.

## Version Compatibility
Because the npm installer and node module resolution algorithm could potentially allow two or more copies of any given package to exist within the same `node_modules` structure, the OpenTelemetry API takes advantage of a variable on the `global` object to store the global API. When an API method in the API package is called, it checks if this `global` API exists and proxies calls to it if and only if it is a compatible API version. This means if a package has a dependency on an OpenTelemetry API version which is not compatible with the API used by the end user, the package will receive a no-op implementation of the API.

## API Methods
If you are writing an instrumentation library, or prefer to call the API methods directly rather than using the `register` method on the Tracer/Meter/Logger Provider, OpenTelemetry provides direct access to the underlying API methods through the `@opentelemetry/api-logs` package. API entry points are defined as global singleton objects `trace`, `metrics`, `logs`, `propagation`, and `context` which contain methods used to initialize SDK implementations and acquire resources from the API.
- [Logs API Documentation][logs-api-docs]
```javascript
const api = require("@opentelemetry/api-logs");

/* A specific implementation of LoggerProvider comes from an SDK */
const loggerProvider = createLoggerProvider();

/* Initialize LoggerProvider */
api.logs.setGlobalLoggerProvider(loggerProvider);
/* returns loggerProvider (no-op if a working provider has not been initialized) */
api.logs.getLoggerProvider();
/* returns a logger from the registered global logger provider (no-op if a working provider has not been initialized) */
const logger = api.logs.getLogger(name, version);

// logging a log record in a log appender
logger.emit({ severityNumber: SeverityNumber.TRACE, body: 'log data' });
```

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat
[npm-url]: https://www.npmjs.com/package/@opentelemetry/api-logs
[npm-img]: https://badge.fury.io/js/%40opentelemetry%2Fapi-logs.svg
[logs-api-docs]: https://open-telemetry.github.io/opentelemetry-js/modules/_opentelemetry_api_logs.html

---

# iCloud: web-app/node_modules/@opentelemetry/api/README.md

> **Source:** icloud://web-app/node_modules/@opentelemetry/api/README.md
> **Analyzed At:** 2026-06-13T06:32:46.419Z

## OpenTelemetry API for JavaScript
API Reference
&nbsp;&nbsp;&bull;&nbsp;&nbsp;
Documentation
This package provides everything needed to interact with the OpenTelemetry API, including all TypeScript interfaces, enums, and no-op implementations. It is intended for use both on the server and in the browser.
The methods in this package perform no operations by default. This means they can be safely called by a library or end-user application whether there is an SDK registered or not. In order to generate and export telemetry data, you will also need an SDK such as the [OpenTelemetry JS SDK][opentelemetry-js].

## You Will Need
- An application you wish to instrument
- [OpenTelemetry JS SDK][opentelemetry-js]
- Node.js >=8.5.0 (14+ is preferred) or an ECMAScript 5+ compatible browser
**Note:** ECMAScript 5+ compatibility is for this package only. Please refer to the documentation for the SDK you are using to determine its minimum ECMAScript version.
**Note for library authors:** Only your end users will need an OpenTelemetry SDK. If you wish to support OpenTelemetry in your library, you only need to use the OpenTelemetry API. For more information, please read the [tracing documentation][docs-tracing].

## Install Dependencies
```sh
npm install @opentelemetry/api @opentelemetry/sdk-trace-base
```

## Trace Your Application
In order to get started with tracing, you will need to first register an SDK. The SDK you are using may provide a convenience method which calls the registration methods for you, but if you would like to call them directly they are documented here: [SDK registration methods][docs-sdk-registration].
Once you have registered an SDK, you can start and end spans. A simple example of basic SDK registration and tracing a simple operation is below. The example should export spans to the console once per second. For more information, see the [tracing documentation][docs-tracing].
```javascript
const { trace }  = require("@opentelemetry/api");
const { BasicTracerProvider, ConsoleSpanExporter, SimpleSpanProcessor }  = require("@opentelemetry/sdk-trace-base");

// Create and register an SDK
const provider = new BasicTracerProvider({
  spanProcessors: [new SimpleSpanProcessor(new ConsoleSpanExporter())]
});
trace.setGlobalTracerProvider(provider);

// Acquire a tracer from the global tracer provider which will be used to trace the application
const name = 'my-application-name';
const version = '0.1.0';
const tracer = trace.getTracer(name, version);

// Trace your application by creating spans
async function operation() {
  const span = tracer.startSpan("do operation");

  // mock some work by sleeping 1 second
  await new Promise((resolve, reject) => {
    setTimeout(resolve, 1000);
  })

  span.end();
}

async function main() {
  while (true) {
    await operation();
  }
}

main();
```

## Version Compatibility
Because the npm installer and node module resolution algorithm could potentially allow two or more copies of any given package to exist within the same `node_modules` structure, the OpenTelemetry API takes advantage of a variable on the `global` object to store the global API. When an API method in the API package is called, it checks if this `global` API exists and proxies calls to it if and only if it is a compatible API version. This means if a package has a dependency on an OpenTelemetry API version which is not compatible with the API used by the end user, the package will receive a no-op implementation of the API.

## 0.20.0 to 0.21.0
- [#78](https://github.com/open-telemetry/opentelemetry-js-api/issues/78) `api.context.bind` arguments reversed and `context` is now a required argument.
- [#46](https://github.com/open-telemetry/opentelemetry-js-api/issues/46) Noop classes and singletons are no longer exported. To create a noop span it is recommended to use `api.trace.wrapSpanContext` with `INVALID_SPAN_CONTEXT` instead of using the `NOOP_TRACER`.

## 1.0.0-rc.3 to 0.20.0
- Removing `TimedEvent` which was not part of spec
- `HttpBaggage` renamed to `HttpBaggagePropagator`
- [#45](https://github.com/open-telemetry/opentelemetry-js-api/pull/45) `Span#context` renamed to `Span#spanContext`
- [#47](https://github.com/open-telemetry/opentelemetry-js-api/pull/47) `getSpan`/`setSpan`/`getSpanContext`/`setSpanContext` moved to `trace` namespace
- [#55](https://github.com/open-telemetry/opentelemetry-js-api/pull/55) `getBaggage`/`setBaggage`/`createBaggage` moved to `propagation` namespace

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url]

## License
Apache 2.0 - See [LICENSE][license-url] for more information.
[opentelemetry-js]: https://github.com/open-telemetry/opentelemetry-js
[discussions-url]: https://github.com/open-telemetry/opentelemetry-js/discussions
[license-url]: https://github.com/open-telemetry/opentelemetry-js/blob/main/api/LICENSE
[docs-tracing]: https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/tracing.md
[docs-sdk-registration]: https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/sdk-registration.md

---

# iCloud: web-app/node_modules/@nodelib/fs.walk/README.md

> **Source:** icloud://web-app/node_modules/@nodelib/fs.walk/README.md
> **Analyzed At:** 2026-06-13T06:32:46.438Z

## @nodelib/fs.walk
> A library for efficiently walking a directory recursively.

## :bulb: Highlights
* :moneybag: Returns useful information: `name`, `path`, `dirent` and `stats` (optional).
* :rocket: On Node.js 10.10+ uses the mechanism without additional calls to determine the entry type for performance reasons. See [`old` and `modern` mode](https://github.com/nodelib/nodelib/blob/master/packages/fs/fs.scandir/README.md#old-and-modern-mode).
* :gear: Built-in directories/files and error filtering system.
* :link: Can safely work with broken symbolic links.

## Install
```console
npm install @nodelib/fs.walk
```

## Usage
```ts
import * as fsWalk from '@nodelib/fs.walk';

fsWalk.walk('path', (error, entries) => { /* … */ });
```

## .walk(path, [optionsOrSettings], callback)
Reads the directory recursively and asynchronously. Requires a callback function.
> :book: If you want to use the Promise API, use `util.promisify`.
```ts
fsWalk.walk('path', (error, entries) => { /* … */ });
fsWalk.walk('path', {}, (error, entries) => { /* … */ });
fsWalk.walk('path', new fsWalk.Settings(), (error, entries) => { /* … */ });
```

## .walkStream(path, [optionsOrSettings])
Reads the directory recursively and asynchronously. [Readable Stream](https://nodejs.org/dist/latest-v12.x/docs/api/stream.html#stream_readable_streams) is used as a provider.
```ts
const stream = fsWalk.walkStream('path');
const stream = fsWalk.walkStream('path', {});
const stream = fsWalk.walkStream('path', new fsWalk.Settings());
```

## .walkSync(path, [optionsOrSettings])
Reads the directory recursively and synchronously. Returns an array of entries.
```ts
const entries = fsWalk.walkSync('path');
const entries = fsWalk.walkSync('path', {});
const entries = fsWalk.walkSync('path', new fsWalk.Settings());
```

## path
* Required: `true`
* Type: `string | Buffer | URL`
A path to a file. If a URL is provided, it must use the `file:` protocol.

## optionsOrSettings
* Required: `false`
* Type: `Options | Settings`
* Default: An instance of `Settings` class
An [`Options`](#options) object or an instance of [`Settings`](#settings) class.
> :book: When you pass a plain object, an instance of the `Settings` class will be created automatically. If you plan to call the method frequently, use a pre-created instance of the `Settings` class.

## Settings([options])
A class of full settings of the package.
```ts
const settings = new fsWalk.Settings({ followSymbolicLinks: true });

const entries = fsWalk.walkSync('path', settings);
```

## Entry
* `name` — The name of the entry (`unknown.txt`).
* `path` — The path of the entry relative to call directory (`root/unknown.txt`).
* `dirent` — An instance of [`fs.Dirent`](./src/types/index.ts) class.
* [`stats`] — An instance of `fs.Stats` class.

## basePath
* Type: `string`
* Default: `undefined`
By default, all paths are built relative to the root path. You can use this option to set custom root path.
In the example below we read the files from the `root` directory, but in the results the root path will be `custom`.
```ts
fsWalk.walkSync('root'); // → ['root/file.txt']
fsWalk.walkSync('root', { basePath: 'custom' }); // → ['custom/file.txt']
```

## concurrency
* Type: `number`
* Default: `Infinity`
The maximum number of concurrent calls to `fs.readdir`.
> :book: The higher the number, the higher performance and the load on the File System. If you want to read in quiet mode, set the value to `4 * os.cpus().length` (4 is default size of [thread pool work scheduling](http://docs.libuv.org/en/v1.x/threadpool.html#thread-pool-work-scheduling)).

## deepFilter
* Type: [`DeepFilterFunction`](./src/settings.ts)
* Default: `undefined`
A function that indicates whether the directory will be read deep or not.
```ts
// Skip all directories that starts with `node_modules`
const filter: DeepFilterFunction = (entry) => !entry.path.startsWith('node_modules');
```

## entryFilter
* Type: [`EntryFilterFunction`](./src/settings.ts)
* Default: `undefined`
A function that indicates whether the entry will be included to results or not.
```ts
// Exclude all `.js` files from results
const filter: EntryFilterFunction = (entry) => !entry.name.endsWith('.js');
```

## errorFilter
* Type: [`ErrorFilterFunction`](./src/settings.ts)
* Default: `undefined`
A function that allows you to skip errors that occur when reading directories.
For example, you can skip `ENOENT` errors if required:
```ts
// Skip all ENOENT errors
const filter: ErrorFilterFunction = (error) => error.code == 'ENOENT';
```

## stats
* Type: `boolean`
* Default: `false`
Adds an instance of `fs.Stats` class to the [`Entry`](#entry).
> :book: Always use `fs.readdir` with additional `fs.lstat/fs.stat` calls to determine the entry type.

## followSymbolicLinks
* Type: `boolean`
* Default: `false`
Follow symbolic links or not. Call `fs.stat` on symbolic link if `true`.

## `throwErrorOnBrokenSymbolicLink`
* Type: `boolean`
* Default: `true`
Throw an error when symbolic link is broken if `true` or safely return `lstat` call if `false`.

## `pathSegmentSeparator`
* Type: `string`
* Default: `path.sep`
By default, this package uses the correct path separator for your OS (`\` on Windows, `/` on Unix-like systems). But you can set this option to any separator character(s) that you want to use instead.

## `fs`
* Type: `FileSystemAdapter`
* Default: A default FS methods
By default, the built-in Node.js module (`fs`) is used to work with the file system. You can replace any method with your own.
```ts
interface FileSystemAdapter {
	lstat: typeof fs.lstat;
	stat: typeof fs.stat;
	lstatSync: typeof fs.lstatSync;
	statSync: typeof fs.statSync;
	readdir: typeof fs.readdir;
	readdirSync: typeof fs.readdirSync;
}

const settings = new fsWalk.Settings({
	fs: { lstat: fakeLstat }
});
```

## Changelog
See the [Releases section of our GitHub project](https://github.com/nodelib/nodelib/releases) for changelog for each release version.

## License
This software is released under the terms of the MIT license.

---

# iCloud: web-app/node_modules/@nodelib/fs.stat/README.md

> **Source:** icloud://web-app/node_modules/@nodelib/fs.stat/README.md
> **Analyzed At:** 2026-06-13T06:32:46.441Z

## @nodelib/fs.stat
> Get the status of a file with some features.

## :bulb: Highlights
Wrapper around standard method `fs.lstat` and `fs.stat` with some features.
* :beginner: Normally follows symbolic link.
* :gear: Can safely work with broken symbolic link.

## Install
```console
npm install @nodelib/fs.stat
```

## Usage
```ts
import * as fsStat from '@nodelib/fs.stat';

fsStat.stat('path', (error, stats) => { /* … */ });
```

## .stat(path, [optionsOrSettings], callback)
Returns an instance of `fs.Stats` class for provided path with standard callback-style.
```ts
fsStat.stat('path', (error, stats) => { /* … */ });
fsStat.stat('path', {}, (error, stats) => { /* … */ });
fsStat.stat('path', new fsStat.Settings(), (error, stats) => { /* … */ });
```

## .statSync(path, [optionsOrSettings])
Returns an instance of `fs.Stats` class for provided path.
```ts
const stats = fsStat.stat('path');
const stats = fsStat.stat('path', {});
const stats = fsStat.stat('path', new fsStat.Settings());
```

## path
* Required: `true`
* Type: `string | Buffer | URL`
A path to a file. If a URL is provided, it must use the `file:` protocol.

## optionsOrSettings
* Required: `false`
* Type: `Options | Settings`
* Default: An instance of `Settings` class
An [`Options`](#options) object or an instance of [`Settings`](#settings) class.
> :book: When you pass a plain object, an instance of the `Settings` class will be created automatically. If you plan to call the method frequently, use a pre-created instance of the `Settings` class.

## Settings([options])
A class of full settings of the package.
```ts
const settings = new fsStat.Settings({ followSymbolicLink: false });

const stats = fsStat.stat('path', settings);
```

## `followSymbolicLink`
* Type: `boolean`
* Default: `true`
Follow symbolic link or not. Call `fs.stat` on symbolic link if `true`.

## `markSymbolicLink`
* Type: `boolean`
* Default: `false`
Mark symbolic link by setting the return value of `isSymbolicLink` function to always `true` (even after `fs.stat`).
> :book: Can be used if you want to know what is hidden behind a symbolic link, but still continue to know that it is a symbolic link.

## `throwErrorOnBrokenSymbolicLink`
* Type: `boolean`
* Default: `true`
Throw an error when symbolic link is broken if `true` or safely return `lstat` call if `false`.

## `fs`
* Type: [`FileSystemAdapter`](./src/adapters/fs.ts)
* Default: A default FS methods
By default, the built-in Node.js module (`fs`) is used to work with the file system. You can replace any method with your own.
```ts
interface FileSystemAdapter {
	lstat?: typeof fs.lstat;
	stat?: typeof fs.stat;
	lstatSync?: typeof fs.lstatSync;
	statSync?: typeof fs.statSync;
}

const settings = new fsStat.Settings({
	fs: { lstat: fakeLstat }
});
```

## Changelog
See the [Releases section of our GitHub project](https://github.com/nodelib/nodelib/releases) for changelog for each release version.

## License
This software is released under the terms of the MIT license.

---

# iCloud: web-app/node_modules/@nodelib/fs.scandir/README.md

> **Source:** icloud://web-app/node_modules/@nodelib/fs.scandir/README.md
> **Analyzed At:** 2026-06-13T06:32:46.444Z

## @nodelib/fs.scandir
> List files and directories inside the specified directory.

## :bulb: Highlights
The package is aimed at obtaining information about entries in the directory.
* :moneybag: Returns useful information: `name`, `path`, `dirent` and `stats` (optional).
* :gear: On Node.js 10.10+ uses the mechanism without additional calls to determine the entry type. See [`old` and `modern` mode](#old-and-modern-mode).
* :link: Can safely work with broken symbolic links.

## Install
```console
npm install @nodelib/fs.scandir
```

## Usage
```ts
import * as fsScandir from '@nodelib/fs.scandir';

fsScandir.scandir('path', (error, stats) => { /* … */ });
```

## .scandir(path, [optionsOrSettings], callback)
Returns an array of plain objects ([`Entry`](#entry)) with information about entry for provided path with standard callback-style.
```ts
fsScandir.scandir('path', (error, entries) => { /* … */ });
fsScandir.scandir('path', {}, (error, entries) => { /* … */ });
fsScandir.scandir('path', new fsScandir.Settings(), (error, entries) => { /* … */ });
```

## .scandirSync(path, [optionsOrSettings])
Returns an array of plain objects ([`Entry`](#entry)) with information about entry for provided path.
```ts
const entries = fsScandir.scandirSync('path');
const entries = fsScandir.scandirSync('path', {});
const entries = fsScandir.scandirSync(('path', new fsScandir.Settings());
```

## path
* Required: `true`
* Type: `string | Buffer | URL`
A path to a file. If a URL is provided, it must use the `file:` protocol.

## optionsOrSettings
* Required: `false`
* Type: `Options | Settings`
* Default: An instance of `Settings` class
An [`Options`](#options) object or an instance of [`Settings`](#settingsoptions) class.
> :book: When you pass a plain object, an instance of the `Settings` class will be created automatically. If you plan to call the method frequently, use a pre-created instance of the `Settings` class.

## Settings([options])
A class of full settings of the package.
```ts
const settings = new fsScandir.Settings({ followSymbolicLinks: false });

const entries = fsScandir.scandirSync('path', settings);
```

## Entry
* `name` — The name of the entry (`unknown.txt`).
* `path` — The path of the entry relative to call directory (`root/unknown.txt`).
* `dirent` — An instance of [`fs.Dirent`](./src/types/index.ts) class. On Node.js below 10.10 will be emulated by [`DirentFromStats`](./src/utils/fs.ts) class.
* `stats` (optional) — An instance of `fs.Stats` class.
For example, the `scandir` call for `tools` directory with one directory inside:
```ts
{
	dirent: Dirent { name: 'typedoc', /* … */ },
	name: 'typedoc',
	path: 'tools/typedoc'
}
```

## stats
* Type: `boolean`
* Default: `false`
Adds an instance of `fs.Stats` class to the [`Entry`](#entry).
> :book: Always use `fs.readdir` without the `withFileTypes` option. ??TODO??

## followSymbolicLinks
* Type: `boolean`
* Default: `false`
Follow symbolic links or not. Call `fs.stat` on symbolic link if `true`.

## `throwErrorOnBrokenSymbolicLink`
* Type: `boolean`
* Default: `true`
Throw an error when symbolic link is broken if `true` or safely use `lstat` call if `false`.

## `pathSegmentSeparator`
* Type: `string`
* Default: `path.sep`
By default, this package uses the correct path separator for your OS (`\` on Windows, `/` on Unix-like systems). But you can set this option to any separator character(s) that you want to use instead.

## `fs`
* Type: [`FileSystemAdapter`](./src/adapters/fs.ts)
* Default: A default FS methods
By default, the built-in Node.js module (`fs`) is used to work with the file system. You can replace any method with your own.
```ts
interface FileSystemAdapter {
	lstat?: typeof fs.lstat;
	stat?: typeof fs.stat;
	lstatSync?: typeof fs.lstatSync;
	statSync?: typeof fs.statSync;
	readdir?: typeof fs.readdir;
	readdirSync?: typeof fs.readdirSync;
}

const settings = new fsScandir.Settings({
	fs: { lstat: fakeLstat }
});
```

## `old` and `modern` mode
This package has two modes that are used depending on the environment and parameters of use.

## old
* Node.js below `10.10` or when the `stats` option is enabled
When working in the old mode, the directory is read first (`fs.readdir`), then the type of entries is determined (`fs.lstat` and/or `fs.stat` for symbolic links).

## modern
* Node.js 10.10+ and the `stats` option is disabled
In the modern mode, reading the directory (`fs.readdir` with the `withFileTypes` option) is combined with obtaining information about its entries. An additional call for symbolic links (`fs.stat`) is still present.
This mode makes fewer calls to the file system. It's faster.

## Changelog
See the [Releases section of our GitHub project](https://github.com/nodelib/nodelib/releases) for changelog for each release version.

## License
This software is released under the terms of the MIT license.

---

# iCloud: web-app/node_modules/@next/swc-darwin-arm64/README.md

> **Source:** icloud://web-app/node_modules/@next/swc-darwin-arm64/README.md
> **Analyzed At:** 2026-06-13T06:32:46.446Z

## `@next/swc-darwin-arm64`
This is the **aarch64-apple-darwin** binary for `@next/swc`

---

# iCloud: web-app/node_modules/@next/env/README.md

> **Source:** icloud://web-app/node_modules/@next/env/README.md
> **Analyzed At:** 2026-06-13T06:32:46.448Z

## `@next/env`
Next.js' util for loading dotenv files in with the proper priorities

---

# iCloud: web-app/node_modules/@monogrid/gainmap-js/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@monogrid/gainmap-js/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.451Z

## Features
* adds AgXToneMapping and NeutralToneMapping to encoding SDR Material shader ([8c163da](https://github.com/MONOGRID/gainmap-js/commit/8c163da5c208412814d3f4ee9e3647d0ad3bba12))

## Features
* removes wasm dependency and implements pure-js JPG encoder ([#73](https://github.com/MONOGRID/gainmap-js/issues/73)) ([00b6e43](https://github.com/MONOGRID/gainmap-js/commit/00b6e43f2ada89e39d76491017ff173574a20873))

## Features
* WebGPU support ([#72](https://github.com/MONOGRID/gainmap-js/issues/72)) ([0d85bec](https://github.com/MONOGRID/gainmap-js/commit/0d85becd0e8b79fc5adfb5bbd757e35e032ee77e))

## Features
* **decode:** removes `DOMParser`, decode is now compatible with Web Workers ([b6a607d](https://github.com/MONOGRID/gainmap-js/commit/b6a607d1be3e7e86524e059c9eb61c8ee2a9e6f7))

## Bug Fixes
* remove LogLuv following threejs removal https://github.com/mrdoob/three.js/pull/29144 ([1df2154](https://github.com/MONOGRID/gainmap-js/commit/1df2154dce59aff39439eb4974c42b55eddc862b))

## Bug Fixes
* **package.json:** publint fixes so that package is correctly imported in next.js ([#36](https://github.com/MONOGRID/gainmap-js/issues/36)) ([490df10](https://github.com/MONOGRID/gainmap-js/commit/490df10f401a82267595dd9e161cc6a0bbce3d94))

## Bug Fixes
* adds setRenderer on LoaderBase ([#34](https://github.com/MONOGRID/gainmap-js/issues/34)) ([18ad0ec](https://github.com/MONOGRID/gainmap-js/commit/18ad0eca49d95685b7f78fc4137f4aaf1338e782))

## Bug Fixes
* **libultrahdr-wasm:** encoding of odd sized images ([#31](https://github.com/MONOGRID/gainmap-js/issues/31)) ([efd52c3](https://github.com/MONOGRID/gainmap-js/commit/efd52c385387d2575c161e243b07369100e8e349))

## Bug Fixes
* **encode:** encodes a valid image when an invalid tonemapping value was provided as input ([94cec23](https://github.com/MONOGRID/gainmap-js/commit/94cec2363aa0dcb3cc46fca048c68ed7e555ebd0))

## Bug Fixes
* **encode:**  hdrCapacityMax correctly computed in output metadata ([f5f2215](https://github.com/MONOGRID/gainmap-js/commit/f5f22152eb236831cb9f23646445e6459be18285))
* **encode:** findTextureMinMax correctly finds min values in textures ([fd94680](https://github.com/MONOGRID/gainmap-js/commit/fd94680a76fdb04b5aa85b4210f3aec21b45a727))

## Bug Fixes
* **loaders:** properly catches render errors and calls onError callback ([b9bcdd1](https://github.com/MONOGRID/gainmap-js/commit/b9bcdd127576fa61c6ee92c876f4845cd80b4d34)), closes [#16](https://github.com/MONOGRID/gainmap-js/issues/16)

## Features
* **core:** disables default mipmap generation, enables user to specify renderTarget (and toDataTexture) options ([147d278](https://github.com/MONOGRID/gainmap-js/commit/147d2783224cb0a2039d762abf4e4b972b0e86da)), closes [#14](https://github.com/MONOGRID/gainmap-js/issues/14) [#15](https://github.com/MONOGRID/gainmap-js/issues/15)

## BREAKING CHANGES
* **core:** `generateMipmaps` is no longer `true` by default, both `minFilter` is  no longer `LinearMipMapLinearFilter` by default but `LinearFilter`, `wrapS` and `warpT` are no longer `RepeatWrapping` by default but `ClampToEdgeWrapping`

## Bug Fixes
* **core:** QuadRenderer dispose method now properly disposes of its internal resources ([#13](https://github.com/MONOGRID/gainmap-js/issues/13)) ([8e4473d](https://github.com/MONOGRID/gainmap-js/commit/8e4473da77732080de24f98dd271fecda06f9e53))
* **HDRJPGLoader:** renders (and returns) an SDR image when provided with a normal jpeg file ([#12](https://github.com/MONOGRID/gainmap-js/issues/12)) ([5222151](https://github.com/MONOGRID/gainmap-js/commit/5222151e6b5c95df79f1c4085cf36f30bd9c2dc4))

## Bug Fixes
* **decode:** changes usage of `NoColorSpace` to `LinearSRGBColorSpace` ([587dc03](https://github.com/MONOGRID/gainmap-js/commit/587dc0377876533b18b506516d8757e04e830c62))
* **loaders:** fixes LoadingManager `onLoad` actually waiting for gainmaps to be generated ([77170f5](https://github.com/MONOGRID/gainmap-js/commit/77170f57c5ad277d3e97d1236ab93a29106c4a99))

## Bug Fixes
* **jpegrloader:** rename JPEGRLoader to HDRJPEGLoader, old name kept for compatibility ([ac6e386](https://github.com/MONOGRID/gainmap-js/commit/ac6e38610886b7adec5806a7ad301bff1ec00d62))

## Bug Fixes
* **decode:** clamp max values in the decode shader to min/max half float ([96986be](https://github.com/MONOGRID/gainmap-js/commit/96986be23dd95825d19fac3b3de520d59d8ad936))

## Bug Fixes
* **gainmaploader:** fix GainMapLoader progress handler not being calculated correctly ([a8e556a](https://github.com/MONOGRID/gainmap-js/commit/a8e556ab1d465a9bd705960d175464cf8d434ea1))

## Bug Fixes
* **decode:** improves compatibility with browsers with no createImageBitmap ([12c7609](https://github.com/MONOGRID/gainmap-js/commit/12c7609ee815a460f95419aab328b412e759f012))
* **decoder:** fix bug when using decodeResult.renderTarget.texture as source for PMREMGenerator ([4ebb983](https://github.com/MONOGRID/gainmap-js/commit/4ebb983d5bbc7f524e4b1231f630e3714cf1f870))

## Bug Fixes
* **decode:** implements proper feature testing for QuadRenderer.toArray ([20109ad](https://github.com/MONOGRID/gainmap-js/commit/20109ad31977124c1169f096e8ccd36628599f89))

## Features
* removes libultrahdr wasm from the decoding part of the library, allows users to load JPEGR files using pure js ([#9](https://github.com/MONOGRID/gainmap-js/issues/9)) ([3ad16f9](https://github.com/MONOGRID/gainmap-js/commit/3ad16f97fec6040fdfdfb4cd5e71b1ac8e504e28))

## BREAKING CHANGES
* The encoder portion of the library has been separated and moved to `@monogrid/gainmap-js/encode`, in order to save file size on user's bundles, all encoding functions must now be imported with that path.
`JPEGRLoader` has been moved from `@monogrid/gainmap-js/libultrahdr` to `@monogrid/gainmap-js` because it now uses a pure js approach

## Bug Fixes
* fixes Firefox Compatibility ([1cec657](https://github.com/MONOGRID/gainmap-js/commit/1cec65708127b6fd064277f4f923fc0f65610fa2))
* **libultrahdr:** fixes circular dependency between JPEGRLoader and libultrahdr ([f30f786](https://github.com/MONOGRID/gainmap-js/commit/f30f7865fb27a601635168b8a104a9935653e758))

## Features
* **decode:** adds threejs loaders ([b32f02a](https://github.com/MONOGRID/gainmap-js/commit/b32f02a09d20fbd9d17b35c65cf4dba8aafc9ed5))

## Bug Fixes
* **release:** add publishConfig to package.json ([cffff0b](https://github.com/MONOGRID/gainmap-js/commit/cffff0b31050ab54040922748b82d97e6aa820a3))

## Bug Fixes
* **release:** scoped package for NPM publishing ([0e30758](https://github.com/MONOGRID/gainmap-js/commit/0e307589e51dd05e160062f2ae78fc746cbdf5aa))

---

# iCloud: web-app/node_modules/@monogrid/gainmap-js/CODE_OF_CONDUCT.md

> **Source:** icloud://web-app/node_modules/@monogrid/gainmap-js/CODE_OF_CONDUCT.md
> **Analyzed At:** 2026-06-13T06:32:46.453Z

## Our Pledge
We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.
We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards
Examples of behavior that contributes to a positive environment for our
community include:
* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
overall community
Examples of unacceptable behavior include:
* The use of sexualized language or imagery, and sexual attention or
advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
professional setting

## Enforcement Responsibilities
Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.
Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope
This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
gainmap@monogrid.com.
All complaints will be reviewed and investigated promptly and fairly.
All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines
Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

## 1. Correction
**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.
**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

## 2. Warning
**Community Impact**: A violation through a single incident or series
of actions.
**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

## 3. Temporary Ban
**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.
**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

## 4. Permanent Ban
**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.
**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution
This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.
Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).
[homepage]: https://www.contributor-covenant.org
For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

---

# iCloud: web-app/node_modules/@monogrid/gainmap-js/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@monogrid/gainmap-js/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.456Z

## Contributing to gainmap-js
First off, thanks for taking the time to contribute! ❤️
All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉
> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

## Table of Contents
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Your First Code Contribution](#your-first-code-contribution)
- [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
- [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)

## I Have a Question
> If you want to ask a question, we assume that you have read the available [Documentation](https://github.com/MONOGRID/gainmap-js/wiki).
Before you ask a question, it is best to search for existing [Issues](https://github.com/MONOGRID/gainmap-js/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.
If you then still feel the need to ask a question and need clarification, we recommend the following:
- Open an [Issue](https://github.com/MONOGRID/gainmap-js/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.
We will then take care of the issue as soon as possible.
<!--
You might want to create a separate issue tag for questions and include it in this description. People should then tag their issues accordingly.
Depending on how large the project is, you may want to outsource the questioning, e.g. to Stack Overflow or Gitter. You may add additional contact and information possibilities:
- IRC
- Slack
- Gitter
- Stack Overflow tag
- Blog
- FAQ
- Roadmap
- E-Mail List
- Forum
-->

## I Want To Contribute
> ### Legal Notice 
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

## Before Submitting a Bug Report
A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.
- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://github.com/MONOGRID/gainmap-js/wiki). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/MONOGRID/gainmap-jsissues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

## How Do I Submit a Good Bug Report?
> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to .
We use GitHub issues to track bugs and errors. If you run into an issue with the project:
- Open an [Issue](https://github.com/MONOGRID/gainmap-js/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.
Once it's filed:
- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

## Suggesting Enhancements
This section guides you through submitting an enhancement suggestion for gainmap-js, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

## Before Submitting an Enhancement
- Make sure that you are using the latest version.
- Read the [documentation](https://github.com/MONOGRID/gainmap-js/wiki) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/MONOGRID/gainmap-js/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

## How Do I Submit a Good Enhancement Suggestion?
Enhancement suggestions are tracked as [GitHub issues](https://github.com/MONOGRID/gainmap-js/issues).
- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. 
- **Explain why this enhancement would be useful** to most gainmap-js users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

## Attribution
This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!

---

# iCloud: web-app/node_modules/@monogrid/gainmap-js/README.md

> **Source:** icloud://web-app/node_modules/@monogrid/gainmap-js/README.md
> **Analyzed At:** 2026-06-13T06:32:46.458Z

## gainmap-js
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMONOGRID%2Fgainmap-js.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FMONOGRID%2Fgainmap-js?ref=badge_shield)
A Javascript (TypeScript) Encoder/Decoder Implementation of Adobe's Gain Map Technology for storing HDR Images using an SDR Image + a "Gain map"
> :warning: This library is intended for encoding and decoding gain map images for the [three.js](https://github.com/mrdoob/three.js/) 3D Library
>
> It can be used for general encode/decode of gain maps but it depends on the three.js library which, in itself, is quite heavy if you only use it to encode/decode gain maps.

## Share Your Project!
Have you built something awesome using this library? We’d love to see what you’ve created!
Whether it’s a small demo or a full-scale application, your project can inspire others and help improve the library. Please share your work in one of these ways:
* GitHub Issues: [Open a new issue](https://github.com/MONOGRID/gainmap-js/issues/new) in this repository with a brief description, screenshots, and links to your project.
* Email: Send us an email at gainmap@monogrid.com with your project details.
Your contributions and creative ideas make our community stronger. We can’t wait to see what you build!

## Live Demo
* [WebGPU Version](https://monogrid.github.io/gainmap-js/webgpu.html)
* [Legacy WebGL Version](https://monogrid.github.io/gainmap-js/)
Both compares loading:
1. a `JPEG` file with embedded gain map data
2. a `webp` sdr file + a `webp` gain map + metadata JSON
3. a comparable size `.hdr` file for comparison

## [Free online encoder](https://gainmap-creator.monogrid.com)
Use it to convert `.hdr` and `.exr` files into gain maps. It's free and the whole process happens in your browser.

## Installing
```bash
$ npm install @monogrid/gainmap-js three
```

## What is a Gain map?
[See here](https://gregbenzphotography.com/hdr-images/jpg-hdr-gain-maps-in-adobe-camera-raw/) for a detailed explanation, here are some relevant parts:
> A gain map is a single file with a second pseudo-image embedded in it to create an optimized result for a specific monitor. It can be used to generate the HDR version (which looks dramatically better where supported), the SDR version (without tone mapping to ensures great quality), or anything in between (to better support less capable HDR displays).
> Gain maps are not a new type of file, but rather a technology which can be embedded into a variety of image formats. There are reference specs already for the JPG, AVIF, JXL, and HEIF file formats. JPG is especially notable as it could not properly support HDR without gain maps and it offers a very useful bridge to the future (i.e. highly compatible with today’s software).
> A gain map includes:
>
> * A **base (default) image**. This can be an SDR or an HDR image (JPG gain maps are always encoded with SDR as the base). If the browser or viewing software does not understand gain maps, it will just the treat file as if it were just the base image.
> * The **gain map**. This is a secondary “image” embedded in the file. It is not a real image, but rather contains data to convert each pixel from the base image into the other (SDR or HDR) version of the image.
>* Gain map **metadata**. This tells the browser how the gain map is encoded as well as critical information to optimize rendering on any display.
Please note that Google [is adopting the gain map technology in Android 14](https://support.google.com/photos/answer/14159275) but its naming of the technology refers to it as **Ultra HDR Image Format** and a JPEG file with embedded gain map is [apparently called JPEGR](https://github.com/google/libultrahdr/blob/3a3a752a5da0b2304b1b6de0ef383bbe41256a67/lib/jpegr.h#L28C16-L28C21) in their terminology, we call it `HDRJPEG` for the moment.

## API
Refer to the [WIKI](https://github.com/MONOGRID/gainmap-js/wiki) for detailed documentation about the API.

## Decoding
The main use case of this library is to decode a JPEG file that contains gain map data
and use it instead of a traditional `.exr` or `.hdr` image.
> NOTE: Starting from v3.1.0 Decoding also works in a WebWorker, thanks to [Alejandro Romano](https://github.com/Arecsu) for the [contribution](https://github.com/MONOGRID/gainmap-js/pull/59)

## Using a single JPEG with embedded Gain map Metadata
This approach lets you load a single file with an embedded Gain Map.
The advantage is to have a single file to load.
The disadvantages are:
* No WEBP compression
* The JPEG cannot be manipulated in Photoshop, GIMP, or any other software that does not support the gain map technology (no photo editing software supports it at the time of writing 06-11-2023).
* Photo sharing websites and/or services (i.e. sharing with Slack) will likely strip the Gain map metadata and the HDR information will be lost, leaving you with only the SDR Representation.
```ts
import { HDRJPGLoader } from '@monogrid/gainmap-js'
import {
  EquirectangularReflectionMapping,
  Mesh,
  MeshBasicMaterial,
  PerspectiveCamera,
  PlaneGeometry,
  Scene,
  WebGLRenderer
} from 'three'

const renderer = new WebGLRenderer()

const loader = new HDRJPGLoader(renderer)
  .setRenderTargetOptions({ mapping: EquirectangularReflectionMapping })

const result = await loader.loadAsync('gainmap.jpeg')
// `result` can be used to populate a Texture

const scene = new Scene()
const mesh = new Mesh(
  new PlaneGeometry(),
  new MeshBasicMaterial({ map: result.renderTarget.texture })
)
scene.add(mesh)
renderer.render(scene, new PerspectiveCamera())

// Starting from three.js r159
// `result.renderTarget.texture` can
// also be used as Equirectangular scene background
//
// it was previously needed to convert it
// to a DataTexture with `result.toDataTexture()`
scene.background = result.renderTarget.texture

// result must be manually disposed
// when you are done using it
result.dispose()
```

## Using separate files
Using separate files will get rid of the limitations of using a single JPEG file but it will force to use three separate files
1. An SDR Representation file
2. A Gainmap file
3. A JSON containing the gainmap metadata used for decoding
```ts
import { GainMapLoader } from '@monogrid/gainmap-js'
import {
  EquirectangularReflectionMapping,
  Mesh,
  MeshBasicMaterial,
  PerspectiveCamera,
  PlaneGeometry,
  Scene,
  WebGLRenderer
} from 'three'

const renderer = new WebGLRenderer()

const loader = new GainMapLoader(renderer)
  .setRenderTargetOptions({ mapping: EquirectangularReflectionMapping })

const result = await loader.loadAsync(['sdr.jpeg', 'gainmap.jpeg', 'metadata.json'])
// `result` can be used to populate a Texture

const scene = new Scene()
const mesh = new Mesh(
  new PlaneGeometry(),
  new MeshBasicMaterial({ map: result.renderTarget.texture })
)
scene.add(mesh)
renderer.render(scene, new PerspectiveCamera())

// Starting from three.js r159
// `result.renderTarget.texture` can
// also be used as Equirectangular scene background
//
// it was previously needed to convert it
// to a DataTexture with `result.toDataTexture()`
scene.background = result.renderTarget.texture

// result must be manually disposed
// when you are done using it
result.dispose()
```

## Decoding with WebGPU
> NOTE: WebGPU decoding requires three.js r163 or higher and a browser that supports WebGPU
The library provides WebGPU-accelerated decoding through the `@monogrid/gainmap-js/webgpu` entry point. WebGPU decoding uses Three.js Shading Language (TSL) and offers improved performance and modern GPU architecture support.

## Using a single JPEG with embedded Gain map Metadata (WebGPU)
```ts
import { HDRJPGLoader } from '@monogrid/gainmap-js/webgpu'
import {
  EquirectangularReflectionMapping,
  Mesh,
  MeshBasicMaterial,
  PerspectiveCamera,
  PlaneGeometry,
  Scene,
  WebGPURenderer
} from 'three/webgpu'

const renderer = new WebGPURenderer()
await renderer.init()

const loader = new HDRJPGLoader(renderer)
  .setRenderTargetOptions({ mapping: EquirectangularReflectionMapping })

const result = await loader.loadAsync('gainmap.jpeg')
// `result` can be used to populate a Texture

const scene = new Scene()
const mesh = new Mesh(
  new PlaneGeometry(),
  new MeshBasicMaterial({ map: result.renderTarget.texture })
)
scene.add(mesh)
renderer.render(scene, new PerspectiveCamera())

// Starting from three.js r159
// `result.renderTarget.texture` can
// also be used as Equirectangular scene background
scene.background = result.renderTarget.texture

// result must be manually disposed
// when you are done using it
result.dispose()
```

## Using separate files (WebGPU)
```ts
import { GainMapLoader } from '@monogrid/gainmap-js/webgpu'
import {
  EquirectangularReflectionMapping,
  Mesh,
  MeshBasicMaterial,
  PerspectiveCamera,
  PlaneGeometry,
  Scene,
  WebGPURenderer
} from 'three/webgpu'

const renderer = new WebGPURenderer()
await renderer.init()

const loader = new GainMapLoader(renderer)
  .setRenderTargetOptions({ mapping: EquirectangularReflectionMapping })

const result = await loader.loadAsync(['sdr.jpeg', 'gainmap.jpeg', 'metadata.json'])
// `result` can be used to populate a Texture

const scene = new Scene()
const mesh = new Mesh(
  new PlaneGeometry(),
  new MeshBasicMaterial({ map: result.renderTarget.texture })
)
scene.add(mesh)
renderer.render(scene, new PerspectiveCamera())

// Starting from three.js r159
// `result.renderTarget.texture` can
// also be used as Equirectangular scene background
scene.background = result.renderTarget.texture

// result must be manually disposed
// when you are done using it
result.dispose()
```

## Key differences between WebGL and WebGPU
1. **Import path**: Use `@monogrid/gainmap-js/webgpu` instead of `@monogrid/gainmap-js`
2. **Three.js imports**: Use `three/webgpu` instead of `three`
3. **Renderer**: Use `WebGPURenderer` instead of `WebGLRenderer`
4. **Renderer initialization**: Call `await renderer.init()` before using WebGPU renderer
5. **Async decoding**: The `decode()` function is async in WebGPU

## Encoding
Encoding a Gain map starting from an EXR file.
This is generally not useful in a `three.js` site but this library exposes methods
that allow to encode an `.exr` or `hdr` file into a `jpeg` with an embedded gain map.
```ts
import { compress, encode, findTextureMinMax } from '@monogrid/gainmap-js/encode'
import { encodeJPEGMetadata } from '@monogrid/gainmap-js/libultrahdr'
import { EXRLoader } from 'three/examples/jsm/loaders/EXRLoader.js'

// load an HDR file
const loader = new EXRLoader()
const image = await loader.loadAsync('image.exr')

// find RAW RGB Max value of a texture
const textureMax = findTextureMinMax(image)

// Encode the gainmap
const encodingResult = encode({
  image,
  // this will encode the full HDR range
  maxContentBoost: Math.max.apply(this, textureMax)
})

// obtain the RAW RGBA SDR buffer and create an ImageData
const sdrImageData = new ImageData(encodingResult.sdr.toArray(), encodingResult.sdr.width, encodingResult.sdr.height)
// obtain the RAW RGBA Gain map buffer and create an ImageData
const gainMapImageData = new ImageData(encodingResult.gainMap.toArray(), encodingResult.gainMap.width, encodingResult.gainMap.height)

// parallel compress the RAW buffers into the specified mimeType
const mimeType = 'image/jpeg'
const quality = 0.9

const [sdr, gainMap] = await Promise.all([
  compress({
    source: sdrImageData,
    mimeType,
    quality,
    flipY: true // output needs to be flipped
  }),
  compress({
    source: gainMapImageData,
    mimeType,
    quality,
    flipY: true // output needs to be flipped
  })
])

// obtain the metadata which will be embedded into
// and XMP tag inside the final JPEG file
const metadata = encodingResult.getMetadata()

// embed the compressed images + metadata into a single
// JPEG file
const jpeg = encodeJPEGMetadata({
  ...encodingResult,
  ...metadata,
  sdr,
  gainMap
})

// `jpeg` will be an `Uint8Array` which can be saved somewhere

// encoder must be manually disposed
// when no longer needed
encodingResult.gainMap.dispose()
encodingResult.sdr.dispose()

```

## Libultrahdr in Vite
If you import `@monogrid/gainmap-js/libultrahdr`
You will need to exclude it from Vite optimizations.
```js
// vite.config.js

module.exports = defineConfig({
  ...
  optimizeDeps: {
    exclude: ['@monogrid/gainmap-js/libultrahdr']
  },
  ...
})
```

## Building
Clone the repository:
```bash
$ git clone git@github.com:MONOGRID/gainmap-js.git
$ cd gainmap-js
$ npm i
$ npm run build
```

## References
* [Adobe Gainmap Specification](https://helpx.adobe.com/camera-raw/using/gain-map.html)
* [Ultra HDR Image Format v1.0](https://developer.android.com/guide/topics/media/platform/hdr-image-format)

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FMONOGRID%2Fgainmap-js.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FMONOGRID%2Fgainmap-js?ref=badge_large)

---

# iCloud: web-app/node_modules/@modelcontextprotocol/server-sequential-thinking/README.md

> **Source:** icloud://web-app/node_modules/@modelcontextprotocol/server-sequential-thinking/README.md
> **Analyzed At:** 2026-06-13T06:32:46.464Z

## Sequential Thinking MCP Server
An MCP server implementation that provides a tool for dynamic and reflective problem-solving through a structured thinking process.

## Features
- Break down complex problems into manageable steps
- Revise and refine thoughts as understanding deepens
- Branch into alternative paths of reasoning
- Adjust the total number of thoughts dynamically
- Generate and verify solution hypotheses

## sequential_thinking
Facilitates a detailed, step-by-step thinking process for problem-solving and analysis.
**Inputs:**
- `thought` (string): The current thinking step
- `nextThoughtNeeded` (boolean): Whether another thought step is needed
- `thoughtNumber` (integer): Current thought number
- `totalThoughts` (integer): Estimated total thoughts needed
- `isRevision` (boolean, optional): Whether this revises previous thinking
- `revisesThought` (integer, optional): Which thought is being reconsidered
- `branchFromThought` (integer, optional): Branching point thought number
- `branchId` (string, optional): Branch identifier
- `needsMoreThoughts` (boolean, optional): If more thoughts are needed

## Usage
The Sequential Thinking tool is designed for:
- Breaking down complex problems into steps
- Planning and design with room for revision
- Analysis that might need course correction
- Problems where the full scope might not be clear initially
- Tasks that need to maintain context over multiple steps
- Situations where irrelevant information needs to be filtered out

## Usage with Claude Desktop
Add this to your `claude_desktop_config.json`:

## npx
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```

## docker
```json
{
  "mcpServers": {
    "sequentialthinking": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mcp/sequentialthinking"
      ]
    }
  }
}
```
To disable logging of thought information set env var: `DISABLE_THOUGHT_LOGGING` to `true`.

## Usage with VS Code
For quick installation, click one of the installation buttons below...
[![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-sequential-thinking%22%5D%7D) [![Install with NPX in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-sequential-thinking%22%5D%7D&quality=insiders)
[![Install with Docker in VS Code](https://img.shields.io/badge/VS_Code-Docker-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22--rm%22%2C%22-i%22%2C%22mcp%2Fsequentialthinking%22%5D%7D) [![Install with Docker in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Docker-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=sequentialthinking&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22--rm%22%2C%22-i%22%2C%22mcp%2Fsequentialthinking%22%5D%7D&quality=insiders)
For manual installation, you can configure the MCP server using one of these methods:
**Method 1: User Configuration (Recommended)**
Add the configuration to your user-level MCP configuration file. Open the Command Palette (`Ctrl + Shift + P`) and run `MCP: Open User Configuration`. This will open your user `mcp.json` file where you can add the server configuration.
**Method 2: Workspace Configuration**
Alternatively, you can add the configuration to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others.
> For more details about MCP configuration in VS Code, see the [official VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).
For NPX installation:
```json
{
  "servers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    }
  }
}
```
For Docker installation:
```json
{
  "servers": {
    "sequential-thinking": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mcp/sequentialthinking"
      ]
    }
  }
}
```

## Usage with Codex CLI
Run the following:

## npx
```bash
codex mcp add sequential-thinking npx -y @modelcontextprotocol/server-sequential-thinking
```

## Building
Docker:
```bash
docker build -t mcp/sequentialthinking -f src/sequentialthinking/Dockerfile .
```

## License
This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

---

# iCloud: web-app/node_modules/@modelcontextprotocol/server-sequential-thinking/node_modules/chalk/readme.md

> **Source:** icloud://web-app/node_modules/@modelcontextprotocol/server-sequential-thinking/node_modules/chalk/readme.md
> **Analyzed At:** 2026-06-13T06:32:46.467Z

## Info
- [Why not switch to a smaller coloring package?](https://github.com/chalk/chalk?tab=readme-ov-file#why-not-switch-to-a-smaller-coloring-package)
- See [yoctocolors](https://github.com/sindresorhus/yoctocolors) for a smaller alternative

## Highlights
- Expressive API
- Highly performant
- No dependencies
- Ability to nest styles
- [256/Truecolor color support](#256-and-truecolor-color-support)
- Auto-detects color support
- Doesn't extend `String.prototype`
- Clean and focused
- Actively maintained
- [Used by ~115,000 packages](https://www.npmjs.com/browse/depended/chalk) as of July 4, 2024

## Install
```sh
npm install chalk
```
**IMPORTANT:** Chalk 5 is ESM. If you want to use Chalk with TypeScript or a build tool, you will probably want to use Chalk 4 for now. [Read more.](https://github.com/chalk/chalk/releases/tag/v5.0.0)

## Usage
```js
import chalk from 'chalk';

console.log(chalk.blue('Hello world!'));
```
Chalk comes with an easy to use composable API where you just chain and nest the styles you want.
```js
import chalk from 'chalk';

const log = console.log;

// Combine styled and normal strings
log(chalk.blue('Hello') + ' World' + chalk.red('!'));

// Compose multiple styles using the chainable API
log(chalk.blue.bgRed.bold('Hello world!'));

// Pass in multiple arguments
log(chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz'));

// Nest styles
log(chalk.red('Hello', chalk.underline.bgBlue('world') + '!'));

// Nest styles of the same type even (color, underline, background)
log(chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
));

// ES2015 template literal
log(`
CPU: ${chalk.red('90%')}
RAM: ${chalk.green('40%')}
DISK: ${chalk.yellow('70%')}
`);

// Use RGB colors in terminal emulators that support it.
log(chalk.rgb(123, 45, 67).underline('Underlined reddish color'));
log(chalk.hex('#DEADED').bold('Bold gray!'));
```
Easily define your own themes:
```js
import chalk from 'chalk';

const error = chalk.bold.red;
const warning = chalk.hex('#FFA500'); // Orange color

console.log(error('Error!'));
console.log(warning('Warning!'));
```
Take advantage of console.log [string substitution](https://nodejs.org/docs/latest/api/console.html#console_console_log_data_args):
```js
import chalk from 'chalk';

const name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> 'Hello Sindre'
```

## chalk.`<style>[.<style>...](string, [string...])`
Example: `chalk.red.bold.underline('Hello', 'world');`
Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `chalk.red.yellow.green` is equivalent to `chalk.green`.
Multiple arguments will be separated by space.

## chalk.level
Specifies the level of color support.
Color support is automatically detected, but you can override it by setting the `level` property. You should however only do this in your own code as it applies globally to all Chalk consumers.
If you need to change this in a reusable module, create a new instance:
```js
import {Chalk} from 'chalk';

const customChalk = new Chalk({level: 0});
```
| Level | Description |
| :---: | :--- |
| `0` | All colors disabled |
| `1` | Basic color support (16 colors) |
| `2` | 256 color support |
| `3` | Truecolor support (16 million colors) |

## supportsColor
Detect whether the terminal [supports color](https://github.com/chalk/supports-color). Used internally and handled for you, but exposed for convenience.
Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, use the environment variable `FORCE_COLOR=1` (level 1), `FORCE_COLOR=2` (level 2), or `FORCE_COLOR=3` (level 3) to forcefully enable color, or `FORCE_COLOR=0` to forcefully disable. The use of `FORCE_COLOR` overrides all other color support checks.
Explicit 256/Truecolor mode can be enabled using the `--color=256` and `--color=16m` flags, respectively.

## chalkStderr and supportsColorStderr
`chalkStderr` contains a separate instance configured with color support detected for `stderr` stream instead of `stdout`. Override rules from `supportsColor` apply to this too. `supportsColorStderr` is exposed for convenience.

## modifierNames, foregroundColorNames, backgroundColorNames, and colorNames
All supported style strings are exposed as an array of strings for convenience. `colorNames` is the combination of `foregroundColorNames` and `backgroundColorNames`.
This can be useful if you wrap Chalk and need to validate input:
```js
import {modifierNames, foregroundColorNames} from 'chalk';

console.log(modifierNames.includes('bold'));
//=> true

console.log(foregroundColorNames.includes('pink'));
//=> false
```

## Modifiers
- `reset` - Reset the current style.
- `bold` - Make the text bold.
- `dim` - Make the text have lower opacity.
- `italic` - Make the text italic. *(Not widely supported)*
- `underline` - Put a horizontal line below the text. *(Not widely supported)*
- `overline` - Put a horizontal line above the text. *(Not widely supported)*
- `inverse`- Invert background and foreground colors.
- `hidden` - Print the text but make it invisible.
- `strikethrough` - Puts a horizontal line through the center of the text. *(Not widely supported)*
- `visible`- Print the text only when Chalk has a color level above zero. Can be useful for things that are purely cosmetic.

## Colors
- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `blackBright` (alias: `gray`, `grey`)
- `redBright`
- `greenBright`
- `yellowBright`
- `blueBright`
- `magentaBright`
- `cyanBright`
- `whiteBright`

## Background colors
- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`
- `bgBlackBright` (alias: `bgGray`, `bgGrey`)
- `bgRedBright`
- `bgGreenBright`
- `bgYellowBright`
- `bgBlueBright`
- `bgMagentaBright`
- `bgCyanBright`
- `bgWhiteBright`

## 256 and Truecolor color support
Chalk supports 256 colors and [Truecolor](https://github.com/termstandard/colors) (16 million colors) on supported terminal apps.
Examples:
- `chalk.hex('#DEADED').underline('Hello, world!')`
- `chalk.rgb(15, 100, 204).inverse('Hello!')`
Background versions of these models are prefixed with `bg` and the first level of the module capitalized (e.g. `hex` for foreground colors and `bgHex` for background colors).
- `chalk.bgHex('#DEADED').underline('Hello, world!')`
- `chalk.bgRgb(15, 100, 204).inverse('Hello!')`
The following color models can be used:
- [`rgb`](https://en.wikipedia.org/wiki/RGB_color_model) - Example: `chalk.rgb(255, 136, 0).bold('Orange!')`
- [`hex`](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) - Example: `chalk.hex('#FF8800').bold('Orange!')`
- [`ansi256`](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) - Example: `chalk.bgAnsi256(194)('Honeydew, more or less')`

## Browser support
Since Chrome 69, ANSI escape codes are natively supported in the developer console.

## Windows
If you're on Windows, do yourself a favor and use [Windows Terminal](https://github.com/microsoft/terminal) instead of `cmd.exe`.

## Why not switch to a smaller coloring package?
Chalk may be larger, but there is a reason for that. It offers a more user-friendly API, well-documented types, supports millions of colors, and covers edge cases that smaller alternatives miss. Chalk is mature, reliable, and built to last.
But beyond the technical aspects, there's something more critical: trust and long-term maintenance. I have been active in open source for over a decade, and I'm committed to keeping Chalk maintained. Smaller packages might seem appealing now, but there's no guarantee they will be around for the long term, or that they won't become malicious over time.
Chalk is also likely already in your dependency tree (since 100K+ packages depend on it), so switching won’t save space—in fact, it might increase it. npm deduplicates dependencies, so multiple Chalk instances turn into one, but adding another package alongside it will increase your overall size.
If the goal is to clean up the ecosystem, switching away from Chalk won’t even make a dent. The real problem lies with packages that have very deep dependency trees (for example, those including a lot of polyfills). Chalk has no dependencies. It's better to focus on impactful changes rather than minor optimizations.
If absolute package size is important to you, I also maintain [yoctocolors](https://github.com/sindresorhus/yoctocolors), one of the smallest color packages out there.
*\- [Sindre](https://github.com/sindresorhus)*

## But the smaller coloring package has benchmarks showing it is faster
[Micro-benchmarks are flawed](https://sindresorhus.com/blog/micro-benchmark-fallacy) because they measure performance in unrealistic, isolated scenarios, often giving a distorted view of real-world performance. Don't believe marketing fluff. All the coloring packages are more than fast enough.

## Related
- [chalk-template](https://github.com/chalk/chalk-template) - [Tagged template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates) support for this module
- [chalk-cli](https://github.com/chalk/chalk-cli) - CLI for this module
- [ansi-styles](https://github.com/chalk/ansi-styles) - ANSI escape codes for styling strings in the terminal
- [supports-color](https://github.com/chalk/supports-color) - Detect whether a terminal supports color
- [strip-ansi](https://github.com/chalk/strip-ansi) - Strip ANSI escape codes
- [strip-ansi-stream](https://github.com/chalk/strip-ansi-stream) - Strip ANSI escape codes from a stream
- [has-ansi](https://github.com/chalk/has-ansi) - Check if a string has ANSI escape codes
- [ansi-regex](https://github.com/chalk/ansi-regex) - Regular expression for matching ANSI escape codes
- [wrap-ansi](https://github.com/chalk/wrap-ansi) - Wordwrap a string with ANSI escape codes
- [slice-ansi](https://github.com/chalk/slice-ansi) - Slice a string with ANSI escape codes
- [color-convert](https://github.com/qix-/color-convert) - Converts colors between different models
- [chalk-animation](https://github.com/bokub/chalk-animation) - Animate strings in the terminal
- [gradient-string](https://github.com/bokub/gradient-string) - Apply color gradients to strings
- [chalk-pipe](https://github.com/LitoMore/chalk-pipe) - Create chalk style schemes with simpler style strings
- [terminal-link](https://github.com/sindresorhus/terminal-link) - Create clickable links in the terminal
*(Not accepting additional entries)*

## Maintainers
- [Sindre Sorhus](https://github.com/sindresorhus)
- [Josh Junon](https://github.com/qix-)

---

# iCloud: web-app/node_modules/@modelcontextprotocol/server-filesystem/README.md

> **Source:** icloud://web-app/node_modules/@modelcontextprotocol/server-filesystem/README.md
> **Analyzed At:** 2026-06-13T06:32:46.478Z

## Filesystem MCP Server
Node.js server implementing Model Context Protocol (MCP) for filesystem operations.

## Features
- Read/write files
- Create/list/delete directories
- Move files/directories
- Search files
- Get file metadata
- Dynamic directory access control via [Roots](https://modelcontextprotocol.io/docs/learn/client-concepts#roots)

## Directory Access Control
The server uses a flexible directory access control system. Directories can be specified via command-line arguments or dynamically via [Roots](https://modelcontextprotocol.io/docs/learn/client-concepts#roots).

## Method 1: Command-line Arguments
Specify Allowed directories when starting the server:
```bash
mcp-server-filesystem /path/to/dir1 /path/to/dir2
```

## Method 2: MCP Roots (Recommended)
MCP clients that support [Roots](https://modelcontextprotocol.io/docs/learn/client-concepts#roots) can dynamically update the Allowed directories.
Roots notified by Client to Server, completely replace any server-side Allowed directories when provided.
**Important**: If server starts without command-line arguments AND client doesn't support roots protocol (or provides empty roots), the server will throw an error during initialization.
This is the recommended method, as this enables runtime directory updates via `roots/list_changed` notifications without server restart, providing a more flexible and modern integration experience.

## How It Works
The server's directory access control follows this flow:
1. **Server Startup**
- Server starts with directories from command-line arguments (if provided)
- If no arguments provided, server starts with empty allowed directories
2. **Client Connection & Initialization**
- Client connects and sends `initialize` request with capabilities
- Server checks if client supports roots protocol (`capabilities.roots`)
3. **Roots Protocol Handling** (if client supports roots)
- **On initialization**: Server requests roots from client via `roots/list`
- Client responds with its configured roots
- Server replaces ALL allowed directories with client's roots
- **On runtime updates**: Client can send `notifications/roots/list_changed`
- Server requests updated roots and replaces allowed directories again
4. **Fallback Behavior** (if client doesn't support roots)
- Server continues using command-line directories only
- No dynamic updates possible
5. **Access Control**
- All filesystem operations are restricted to allowed directories
- Use `list_allowed_directories` tool to see current directories
- Server requires at least ONE allowed directory to operate
**Note**: The server will only allow operations within directories specified either via `args` or via Roots.

## Tools
- **read_text_file**
- Read complete contents of a file as text
- Inputs:
- `path` (string)
- `head` (number, optional): First N lines
- `tail` (number, optional): Last N lines
- Always treats the file as UTF-8 text regardless of extension
- Cannot specify both `head` and `tail` simultaneously
- **read_media_file**
- Read an image or audio file
- Inputs:
- `path` (string)
- Streams the file and returns base64 data with the corresponding MIME type
- **read_multiple_files**
- Read multiple files simultaneously
- Input: `paths` (string[])
- Failed reads won't stop the entire operation
- **write_file**
- Create new file or overwrite existing (exercise caution with this)
- Inputs:
- `path` (string): File location
- `content` (string): File content
- **edit_file**
- Make selective edits using advanced pattern matching and formatting
- Features:
- Line-based and multi-line content matching
- Whitespace normalization with indentation preservation
- Multiple simultaneous edits with correct positioning
- Indentation style detection and preservation
- Git-style diff output with context
- Preview changes with dry run mode
- Inputs:
- `path` (string): File to edit
- `edits` (array): List of edit operations
- `oldText` (string): Text to search for (can be substring)
- `newText` (string): Text to replace with
- `dryRun` (boolean): Preview changes without applying (default: false)
- Returns detailed diff and match information for dry runs, otherwise applies changes
- Best Practice: Always use dryRun first to preview changes before applying them
- **create_directory**
- Create new directory or ensure it exists
- Input: `path` (string)
- Creates parent directories if needed
- Succeeds silently if directory exists
- **list_directory**
- List directory contents with [FILE] or [DIR] prefixes
- Input: `path` (string)
- **list_directory_with_sizes**
- List directory contents with [FILE] or [DIR] prefixes, including file sizes
- Inputs:
- `path` (string): Directory path to list
- `sortBy` (string, optional): Sort entries by "name" or "size" (default: "name")
- Returns detailed listing with file sizes and summary statistics
- Shows total files, directories, and combined size
- **move_file**
- Move or rename files and directories
- Inputs:
- `source` (string)
- `destination` (string)
- Fails if destination exists
- **search_files**
- Recursively search for files/directories that match or do not match patterns
- Inputs:
- `path` (string): Starting directory
- `pattern` (string): Search pattern
- `excludePatterns` (string[]): Exclude any patterns.
- Glob-style pattern matching
- Returns full paths to matches
- **directory_tree**
- Get recursive JSON tree structure of directory contents
- Inputs:
- `path` (string): Starting directory
- `excludePatterns` (string[]): Exclude any patterns. Glob formats are supported.
- Returns:
- JSON array where each entry contains:
- `name` (string): File/directory name
- `type` ('file'|'directory'): Entry type
- `children` (array): Present only for directories
- Empty array for empty directories
- Omitted for files
- Output is formatted with 2-space indentation for readability
- **get_file_info**
- Get detailed file/directory metadata
- Input: `path` (string)
- Returns:
- Size
- Creation time
- Modified time
- Access time
- Type (file/directory)
- Permissions
- **list_allowed_directories**
- List all directories the server is allowed to access
- No input required
- Returns:
- Directories that this server can read/write from

## Tool annotations (MCP hints)
This server sets [MCP ToolAnnotations](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#toolannotations)
on each tool so clients can:
- Distinguish **read‑only** tools from write‑capable tools.
- Understand which write operations are **idempotent** (safe to retry with the same arguments).
- Highlight operations that may be **destructive** (overwriting or heavily mutating data).
The mapping for filesystem tools is:
| Tool                        | readOnlyHint | idempotentHint | destructiveHint | Notes                                            |
|-----------------------------|--------------|----------------|-----------------|--------------------------------------------------|
| `read_text_file`            | `true`       | –              | –               | Pure read                                       |
| `read_media_file`           | `true`       | –              | –               | Pure read                                       |
| `read_multiple_files`       | `true`       | –              | –               | Pure read                                       |
| `list_directory`            | `true`       | –              | –               | Pure read                                       |
| `list_directory_with_sizes` | `true`       | –              | –               | Pure read                                       |
| `directory_tree`            | `true`       | –              | –               | Pure read                                       |
| `search_files`              | `true`       | –              | –               | Pure read                                       |
| `get_file_info`             | `true`       | –              | –               | Pure read                                       |
| `list_allowed_directories`  | `true`       | –              | –               | Pure read                                       |
| `create_directory`          | `false`      | `true`         | `false`         | Re‑creating the same dir is a no‑op             |
| `write_file`                | `false`      | `true`         | `true`          | Overwrites existing files                       |
| `edit_file`                 | `false`      | `false`        | `true`          | Re‑applying edits can fail or double‑apply      |
| `move_file`                 | `false`      | `false`        | `false`         | Move/rename only; repeat usually errors         |
> Note: `idempotentHint` and `destructiveHint` are meaningful only when `readOnlyHint` is `false`, as defined by the MCP spec.

## Usage with Claude Desktop
Add this to your `claude_desktop_config.json`:
Note: you can provide sandboxed directories to the server by mounting them to `/projects`. Adding the `ro` flag will make the directory readonly by the server.

## Docker
Note: all directories must be mounted to `/projects` by default.
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--mount", "type=bind,src=/Users/username/Desktop,dst=/projects/Desktop",
        "--mount", "type=bind,src=/path/to/other/allowed/dir,dst=/projects/other/allowed/dir,ro",
        "--mount", "type=bind,src=/path/to/file.txt,dst=/projects/path/to/file.txt",
        "mcp/filesystem",
        "/projects"
      ]
    }
  }
}
```

## NPX
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Desktop",
        "/path/to/other/allowed/dir"
      ]
    }
  }
}
```

## Usage with VS Code
For quick installation, click the installation buttons below...
[![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-filesystem%22%2C%22%24%7BworkspaceFolder%7D%22%5D%7D) [![Install with NPX in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-NPM-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40modelcontextprotocol%2Fserver-filesystem%22%2C%22%24%7BworkspaceFolder%7D%22%5D%7D&quality=insiders)
[![Install with Docker in VS Code](https://img.shields.io/badge/VS_Code-Docker-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22--mount%22%2C%22type%3Dbind%2Csrc%3D%24%7BworkspaceFolder%7D%2Cdst%3D%2Fprojects%2Fworkspace%22%2C%22mcp%2Ffilesystem%22%2C%22%2Fprojects%22%5D%7D) [![Install with Docker in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Docker-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=filesystem&config=%7B%22command%22%3A%22docker%22%2C%22args%22%3A%5B%22run%22%2C%22-i%22%2C%22--rm%22%2C%22--mount%22%2C%22type%3Dbind%2Csrc%3D%24%7BworkspaceFolder%7D%2Cdst%3D%2Fprojects%2Fworkspace%22%2C%22mcp%2Ffilesystem%22%2C%22%2Fprojects%22%5D%7D&quality=insiders)
For manual installation, you can configure the MCP server using one of these methods:
**Method 1: User Configuration (Recommended)**
Add the configuration to your user-level MCP configuration file. Open the Command Palette (`Ctrl + Shift + P`) and run `MCP: Open User Configuration`. This will open your user `mcp.json` file where you can add the server configuration.
**Method 2: Workspace Configuration**
Alternatively, you can add the configuration to a file called `.vscode/mcp.json` in your workspace. This will allow you to share the configuration with others.
> For more details about MCP configuration in VS Code, see the [official VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).
You can provide sandboxed directories to the server by mounting them to `/projects`. Adding the `ro` flag will make the directory readonly by the server.

## Docker
Note: all directories must be mounted to `/projects` by default.
```json
{
  "servers": {
    "filesystem": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--mount", "type=bind,src=${workspaceFolder},dst=/projects/workspace",
        "mcp/filesystem",
        "/projects"
      ]
    }
  }
}
```

## NPX
```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${workspaceFolder}"
      ]
    }
  }
}
```

## Build
Docker build:
```bash
docker build -t mcp/filesystem -f src/filesystem/Dockerfile .
```

## License
This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

---

# iCloud: web-app/node_modules/@modelcontextprotocol/server-filesystem/node_modules/minimatch/LICENSE.md

> **Source:** icloud://web-app/node_modules/@modelcontextprotocol/server-filesystem/node_modules/minimatch/LICENSE.md
> **Analyzed At:** 2026-06-13T06:32:46.480Z

## Blue Oak Model License
Version 1.0.0

## Purpose
This license gives everyone as much permission to work with
this software as possible, while protecting contributors
from liability.

## Acceptance
In order to receive this license, you must agree to its
rules. The rules of this license are both obligations
under that agreement and conditions to your license.
You must not do anything with this software that triggers
a rule that you cannot or will not follow.

## Copyright
Each contributor licenses you to do everything with this
software that would otherwise infringe that contributor's
copyright in it.

## Notices
You must ensure that everyone who gets a copy of
any part of this software from you, with or without
changes, also gets the text of this license or a link to
.

## Excuse
If anyone notifies you in writing that you have not
complied with [Notices](#notices), you can keep your
license by taking all practical steps to comply within 30
days after the notice. If you do not do so, your license
ends immediately.

## Patent
Each contributor licenses you to do everything with this
software that would otherwise infringe any patent claims
they can license or become able to license.

## Reliability
No contributor can revoke this license.

## No Liability
**_As far as the law allows, this software comes as is,
without any warranty or condition, and no contributor
will be liable to anyone for any damages related to this
software or this license, under any kind of legal claim._**

---

# iCloud: web-app/node_modules/@modelcontextprotocol/server-filesystem/node_modules/brace-expansion/README.md

> **Source:** icloud://web-app/node_modules/@modelcontextprotocol/server-filesystem/node_modules/brace-expansion/README.md
> **Analyzed At:** 2026-06-13T06:32:46.490Z

## brace-expansion
[Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html),
as known from sh/bash, in JavaScript.
[![CI](https://github.com/juliangruber/brace-expansion/actions/workflows/ci.yml/badge.svg)](https://github.com/juliangruber/brace-expansion/actions/workflows/ci.yml)
[![downloads](https://img.shields.io/npm/dm/brace-expansion.svg)](https://www.npmjs.org/package/brace-expansion)

## Example
```js
import { expand } from 'brace-expansion'

expand('file-{a,b,c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('-v{,,}')
// => ['-v', '-v', '-v']

expand('file{0..2}.jpg')
// => ['file0.jpg', 'file1.jpg', 'file2.jpg']

expand('file-{a..c}.jpg')
// => ['file-a.jpg', 'file-b.jpg', 'file-c.jpg']

expand('file{2..0}.jpg')
// => ['file2.jpg', 'file1.jpg', 'file0.jpg']

expand('file{0..4..2}.jpg')
// => ['file0.jpg', 'file2.jpg', 'file4.jpg']

expand('file-{a..e..2}.jpg')
// => ['file-a.jpg', 'file-c.jpg', 'file-e.jpg']

expand('file{00..10..5}.jpg')
// => ['file00.jpg', 'file05.jpg', 'file10.jpg']

expand('{{A..C},{a..c}}')
// => ['A', 'B', 'C', 'a', 'b', 'c']

expand('ppp{,config,oe{,conf}}')
// => ['ppp', 'pppconfig', 'pppoe', 'pppoeconf']
```

## API
```js
import { expand } from 'brace-expansion'
```

## const expanded = expand(str, [options])
Return an array of all possible and valid expansions of `str`. If
none are found, `[str]` is returned.
The `options` object can provide a `max` value to cap the number
of expansions allowed. This is limited to `100_000` by default,
to prevent DoS attacks.
```js
const expansions = expand('{1..100}'.repeat(5), {
  max: 100,
})
// expansions.length will be 100, not 100^5
```
Valid expansions are:
```js
;/^(.*,)+(.+)?$/
// {a,b,...}
```
```js
;/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```
A numeric sequence from `x` to `y` inclusive, with optional increment.
If `x` or `y` start with a leading `0`, all the numbers will be padded
to have equal length. Negative numbers and backwards iteration work too.
```js
;/^-?\d+\.\.-?\d+(\.\.-?\d+)?$/
// {x..y[..incr]}
```
An alphabetic sequence from `x` to `y` inclusive, with optional increment.
`x` and `y` must be exactly one character, and if given, `incr` must be a
number.
For compatibility reasons, the string `${` is not eligible for brace expansion.

---

# iCloud: web-app/node_modules/@modelcontextprotocol/server-filesystem/node_modules/balanced-match/README.md

> **Source:** icloud://web-app/node_modules/@modelcontextprotocol/server-filesystem/node_modules/balanced-match/README.md
> **Analyzed At:** 2026-06-13T06:32:46.495Z

## balanced-match
``. Supports regular expressions as well!

## Example
Get the first matching pair of braces:
```js
import { balanced } from 'balanced-match'

console.log(balanced('{', '}', 'pre{in{nested}}post'))
console.log(balanced('{', '}', 'pre{first}between{second}post'))
console.log(
  balanced(/\s+\{\s+/, /\s+\}\s+/, 'pre  {   in{nest}   }  post'),
)
```
The matches are:
```bash
$ node example.js
{ start: 3, end: 14, pre: 'pre', body: 'in{nested}', post: 'post' }
{ start: 3,
  end: 9,
  pre: 'pre',
  body: 'first',
  post: 'between{second}post' }
{ start: 3, end: 17, pre: 'pre', body: 'in{nest}', post: 'post' }
```

## const m = balanced(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
object with those keys:
- **start** the index of the first match of `a`
- **end** the index of the matching `b`
- **pre** the preamble, `a` and `b` not included
- **body** the match, `a` and `b` not included
- **post** the postscript, `a` and `b` not included
If there's no match, `undefined` will be returned.

## const r = balanced.range(a, b, str)
For the first non-nested matching pair of `a` and `b` in `str`, return an
array with indexes: `[ ,  ]`.
If there's no match, `undefined` will be returned.

---

# iCloud: web-app/node_modules/@modelcontextprotocol/sdk/README.md

> **Source:** icloud://web-app/node_modules/@modelcontextprotocol/sdk/README.md
> **Analyzed At:** 2026-06-13T06:32:46.499Z

## MCP TypeScript SDK [![NPM Version](https://img.shields.io/npm/v/%40modelcontextprotocol%2Fsdk)](https://www.npmjs.com/package/@modelcontextprotocol/sdk) [![MIT licensed](https://img.shields.io/npm/l/%40modelcontextprotocol%2Fsdk)](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/LICENSE)
Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
- [Examples](#examples)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Model Context Protocol allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction. This TypeScript SDK implements
[the full MCP specification](https://modelcontextprotocol.io/specification/draft), making it easy to:
- Create MCP servers that expose resources, prompts and tools
- Build MCP clients that can connect to any MCP server
- Use standard transports like stdio and Streamable HTTP

## Installation
```bash
npm install @modelcontextprotocol/sdk zod
```
This SDK has a **required peer dependency** on `zod` for schema validation. The SDK internally imports from `zod/v4`, but maintains backwards compatibility with projects using Zod v3.25 or later. You can use either API in your code by importing from `zod/v3` or `zod/v4`:

## Quick Start
To see the SDK in action end-to-end, start from the runnable examples in `src/examples`:
1. **Install dependencies** (from the SDK repo root):
    ```bash
    npm install
```
2. **Run the example Streamable HTTP server**:
    ```bash
    npx tsx src/examples/server/simpleStreamableHttp.ts
```
3. **Run the interactive client in another terminal**:
    ```bash
    npx tsx src/examples/client/simpleStreamableHttp.ts
```
This pair of examples demonstrates tools, resources, prompts, sampling, elicitation, tasks and logging. For a guided walkthrough and variations (stateless servers, JSON-only responses, SSE compatibility, OAuth, etc.), see [docs/server.md](docs/server.md) and
[docs/client.md](docs/client.md).

## Servers and transports
An MCP server is typically created with `McpServer` and connected to a transport such as Streamable HTTP or stdio. The SDK supports:
- **Streamable HTTP** for remote servers (recommended).
- **HTTP + SSE** for backwards compatibility only.
- **stdio** for local, process-spawned integrations.
Runnable server examples live under `src/examples/server` and are documented in [docs/server.md](docs/server.md).

## Tools, resources, prompts
- **Tools** let LLMs ask your server to take actions (computation, side effects, network calls).
- **Resources** expose read-only data that clients can surface to users or models.
- **Prompts** are reusable templates that help users talk to models in a consistent way.
The detailed APIs, including `ResourceTemplate`, completions, and display-name metadata, are covered in [docs/server.md](docs/server.md#tools-resources-and-prompts), with runnable implementations in [`simpleStreamableHttp.ts`](src/examples/server/simpleStreamableHttp.ts).

## Capabilities: sampling, elicitation, and tasks
The SDK includes higher-level capabilities for richer workflows:
- **Sampling**: server-side tools can ask connected clients to run LLM completions.
- **Form elicitation**: tools can request non-sensitive input via structured forms.
- **URL elicitation**: servers can ask users to complete secure flows in a browser (e.g., API key entry, payments, OAuth).
- **Tasks (experimental)**: long-running tool calls can be turned into tasks that you poll or resume later.
Conceptual overviews and links to runnable examples are in:
- [docs/capabilities.md](docs/capabilities.md)
Key example servers include:
- [`toolWithSampleServer.ts`](src/examples/server/toolWithSampleServer.ts)
- [`elicitationFormExample.ts`](src/examples/server/elicitationFormExample.ts)
- [`elicitationUrlExample.ts`](src/examples/server/elicitationUrlExample.ts)

## Clients
The high-level `Client` class connects to MCP servers over different transports and exposes helpers like `listTools`, `callTool`, `listResources`, `readResource`, `listPrompts`, and `getPrompt`.
Runnable clients live under `src/examples/client` and are described in [docs/client.md](docs/client.md), including:
- Interactive Streamable HTTP client ([`simpleStreamableHttp.ts`](src/examples/client/simpleStreamableHttp.ts))
- Streamable HTTP client with SSE fallback ([`streamableHttpWithSseFallbackClient.ts`](src/examples/client/streamableHttpWithSseFallbackClient.ts))
- OAuth-enabled clients and polling/parallel examples

## Node.js Web Crypto (globalThis.crypto) compatibility
Some parts of the SDK (for example, JWT-based client authentication in `auth-extensions.ts` via `jose`) rely on the Web Crypto API exposed as `globalThis.crypto`.
See [docs/faq.md](docs/faq.md) for details on supported Node.js versions and how to polyfill `globalThis.crypto` when running on older Node.js runtimes.

## Examples
The SDK ships runnable examples under `src/examples`. Use these tables to find the scenario you care about and jump straight to the corresponding code and docs.

## Server examples
| Scenario                                            | Description                                                                                       | Example file(s)                                                                                          | Related docs                                                             |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Streamable HTTP server (stateful)                   | Feature-rich server with tools, resources, prompts, logging, tasks, sampling, and optional OAuth. | [`simpleStreamableHttp.ts`](src/examples/server/simpleStreamableHttp.ts)                                 | [`server.md`](docs/server.md), [`capabilities.md`](docs/capabilities.md) |
| Streamable HTTP server (stateless)                  | No session tracking; good for simple API-style servers.                                           | [`simpleStatelessStreamableHttp.ts`](src/examples/server/simpleStatelessStreamableHttp.ts)               | [`server.md`](docs/server.md)                                            |
| JSON response mode (no SSE)                         | Streamable HTTP with JSON responses only and limited notifications.                               | [`jsonResponseStreamableHttp.ts`](src/examples/server/jsonResponseStreamableHttp.ts)                     | [`server.md`](docs/server.md)                                            |
| Server notifications over Streamable HTTP           | Demonstrates server-initiated notifications using SSE with Streamable HTTP.                       | [`standaloneSseWithGetStreamableHttp.ts`](src/examples/server/standaloneSseWithGetStreamableHttp.ts)     | [`server.md`](docs/server.md)                                            |
| Deprecated HTTP+SSE server                          | Legacy HTTP+SSE transport for backwards-compatibility testing.                                    | [`simpleSseServer.ts`](src/examples/server/simpleSseServer.ts)                                           | [`server.md`](docs/server.md)                                            |
| Backwards-compatible server (Streamable HTTP + SSE) | Single server that supports both Streamable HTTP and legacy SSE clients.                          | [`sseAndStreamableHttpCompatibleServer.ts`](src/examples/server/sseAndStreamableHttpCompatibleServer.ts) | [`server.md`](docs/server.md)                                            |
| Form elicitation server                             | Uses form elicitation to collect non-sensitive user input.                                        | [`elicitationFormExample.ts`](src/examples/server/elicitationFormExample.ts)                             | [`capabilities.md`](docs/capabilities.md#elicitation)                    |
| URL elicitation server                              | Demonstrates URL-mode elicitation in an OAuth-protected server.                                   | [`elicitationUrlExample.ts`](src/examples/server/elicitationUrlExample.ts)                               | [`capabilities.md`](docs/capabilities.md#elicitation)                    |
| Sampling and tasks server                           | Combines tools, logging, sampling, and experimental task-based execution.                         | [`toolWithSampleServer.ts`](src/examples/server/toolWithSampleServer.ts)                                 | [`capabilities.md`](docs/capabilities.md)                                |
| OAuth demo authorization server                     | In-memory OAuth provider used with the example servers.                                           | [`demoInMemoryOAuthProvider.ts`](src/examples/server/demoInMemoryOAuthProvider.ts)                       | [`server.md`](docs/server.md)                                            |

## Client examples
| Scenario                                            | Description                                                                        | Example file(s)                                                                                                                                                                                                                        | Related docs                                                 |
| --------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Interactive Streamable HTTP client                  | CLI client that exercises tools, resources, prompts, elicitation, and tasks.       | [`simpleStreamableHttp.ts`](src/examples/client/simpleStreamableHttp.ts)                                                                                                                                                               | [`client.md`](docs/client.md)                                |
| Backwards-compatible client (Streamable HTTP → SSE) | Tries Streamable HTTP first, then falls back to SSE on 4xx responses.              | [`streamableHttpWithSseFallbackClient.ts`](src/examples/client/streamableHttpWithSseFallbackClient.ts)                                                                                                                                 | [`client.md`](docs/client.md), [`server.md`](docs/server.md) |
| SSE polling client                                  | Polls a legacy SSE server and demonstrates notification handling.                  | [`ssePollingClient.ts`](src/examples/client/ssePollingClient.ts)                                                                                                                                                                       | [`client.md`](docs/client.md)                                |
| Parallel tool calls client                          | Shows how to run multiple tool calls in parallel.                                  | [`parallelToolCallsClient.ts`](src/examples/client/parallelToolCallsClient.ts)                                                                                                                                                         | [`client.md`](docs/client.md)                                |
| Multiple clients in parallel                        | Demonstrates connecting multiple clients concurrently to the same server.          | [`multipleClientsParallel.ts`](src/examples/client/multipleClientsParallel.ts)                                                                                                                                                         | [`client.md`](docs/client.md)                                |
| OAuth clients                                       | Examples of client_credentials (basic and private_key_jwt) and reusable providers. | [`simpleOAuthClient.ts`](src/examples/client/simpleOAuthClient.ts), [`simpleOAuthClientProvider.ts`](src/examples/client/simpleOAuthClientProvider.ts), [`simpleClientCredentials.ts`](src/examples/client/simpleClientCredentials.ts) | [`client.md`](docs/client.md)                                |
| URL elicitation client                              | Works with the URL elicitation server to drive secure browser flows.               | [`elicitationUrlExample.ts`](src/examples/client/elicitationUrlExample.ts)                                                                                                                                                             | [`capabilities.md`](docs/capabilities.md#elicitation)        |
Shared utilities:
- In-memory event store for resumability: [`inMemoryEventStore.ts`](src/examples/shared/inMemoryEventStore.ts) (see [`server.md`](docs/server.md)).
For more details on how to run these examples (including recommended commands and deployment diagrams), see `src/examples/README.md`.

## Documentation
- Local SDK docs:
- [docs/server.md](docs/server.md) – building and running MCP servers, transports, tools/resources/prompts, CORS, DNS rebinding, and multi-node deployment.
- [docs/client.md](docs/client.md) – using the high-level client, transports, backwards compatibility, and OAuth helpers.
- [docs/capabilities.md](docs/capabilities.md) – sampling, elicitation (form and URL), and experimental task-based execution.
- [docs/protocol.md](docs/protocol.md) – protocol features: ping, progress, cancellation, pagination, capability negotiation, and JSON Schema.
- [docs/faq.md](docs/faq.md) – environment and troubleshooting FAQs (including Node.js Web Crypto support).
- External references:
- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP Specification](https://spec.modelcontextprotocol.io)
- [Example Servers](https://github.com/modelcontextprotocol/servers)

## Contributing
Issues and pull requests are welcome on GitHub at .

## License
This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

---

# iCloud: web-app/node_modules/@mikro-orm/reflection/README.md

> **Source:** icloud://web-app/node_modules/@mikro-orm/reflection/README.md
> **Analyzed At:** 2026-06-13T06:32:46.548Z

## 🤔 Unit of What?
You might be asking: _What the hell is Unit of Work and why should I care about it?_
> Unit of Work maintains a list of objects (_entities_) affected by a business transaction
> and coordinates the writing out of changes. [(Martin Fowler)](https://www.martinfowler.com/eaaCatalog/unitOfWork.html)
> Identity Map ensures that each object (_entity_) gets loaded only once by keeping every
> loaded object in a map. Looks up objects using the map when referring to them.
> [(Martin Fowler)](https://www.martinfowler.com/eaaCatalog/identityMap.html)
So what benefits does it bring to us?

## Implicit Transactions
First and most important implication of having Unit of Work is that it allows handling transactions automatically.
When you call `em.flush()`, all computed changes are queried inside a database transaction (if supported by given driver). This means that you can control the boundaries of transactions simply by calling `em.persistLater()` and once all your changes are ready, calling `flush()` will run them inside a transaction.
> You can also control the transaction boundaries manually via `em.transactional(cb)`.
```typescript
const user = await em.findOneOrFail(User, 1);
user.email = 'foo@bar.com';
const car = new Car();
user.cars.add(car);

// thanks to bi-directional cascading we only need to persist user entity
// flushing will create a transaction, insert new car and update user with new email
// as user entity is managed, calling flush() is enough
await em.flush();
```

## ChangeSet based persistence
MikroORM allows you to implement your domain/business logic directly in the entities. To maintain always valid entities, you can use constructors to mark required properties. Let's define the `User` entity used in previous example:
```typescript
@Entity()
export class User {

  @PrimaryKey()
  id!: number;

  @Property()
  name!: string;

  @OneToOne(() => Address)
  address?: Address;

  @ManyToMany(() => Car)
  cars = new Collection<Car>(this);

  constructor(name: string) {
    this.name = name;
  }

}
```
Now to create new instance of the `User` entity, we are forced to provide the `name`:
```typescript
const user = new User('John Doe'); // name is required to create new user instance
user.address = new Address('10 Downing Street'); // address is optional
```
Once your entities are loaded, make a number of synchronous actions on your entities,
then call `em.flush()`. This will trigger computing of change sets. Only entities
(and properties) that were changed will generate database queries, if there are no changes,
no transaction will be started.
```typescript
const user = await em.findOneOrFail(User, 1, {
  populate: ['cars', 'address.city'],
});
user.title = 'Mr.';
user.address.street = '10 Downing Street'; // address is 1:1 relation of Address entity
user.cars.getItems().forEach(car => car.forSale = true); // cars is 1:m collection of Car entities
const car = new Car('VW');
user.cars.add(car);

// now we can flush all changes done to managed entities
await em.flush();
```
`em.flush()` will then execute these queries from the example above:
```sql
begin;
update "user" set "title" = 'Mr.' where "id" = 1;
update "user_address" set "street" = '10 Downing Street' where "id" = 123;
update "car"
  set "for_sale" = case
    when ("id" = 1) then true
    when ("id" = 2) then true
    when ("id" = 3) then true
    else "for_sale" end
  where "id" in (1, 2, 3)
insert into "car" ("brand", "owner") values ('VW', 1);
commit;
```

## Identity Map
Thanks to Identity Map, you will always have only one instance of given entity in one context. This allows for some optimizations (skipping loading of already loaded entities), as well as comparison by identity (`ent1 === ent2`).

## 📖 Documentation
MikroORM documentation, included in this repo in the root directory, is built with [Docusaurus](https://docusaurus.io) and publicly hosted on GitHub Pages at https://mikro-orm.io.
There is also auto-generated [CHANGELOG.md](CHANGELOG.md) file based on commit messages (via `semantic-release`).

## ✨ Core Features
- [Clean and Simple Entity Definition](https://mikro-orm.io/docs/defining-entities)
- [Identity Map](https://mikro-orm.io/docs/identity-map)
- [Entity References](https://mikro-orm.io/docs/entity-references)
- [Using Entity Constructors](https://mikro-orm.io/docs/entity-constructors)
- [Modelling Relationships](https://mikro-orm.io/docs/relationships)
- [Collections](https://mikro-orm.io/docs/collections)
- [Unit of Work](https://mikro-orm.io/docs/unit-of-work)
- [Transactions](https://mikro-orm.io/docs/transactions)
- [Cascading persist and remove](https://mikro-orm.io/docs/cascading)
- [Composite and Foreign Keys as Primary Key](https://mikro-orm.io/docs/composite-keys)
- [Filters](https://mikro-orm.io/docs/filters)
- [Using `QueryBuilder`](https://mikro-orm.io/docs/query-builder)
- [Populating relations](https://mikro-orm.io/docs/populating-relations)
- [Property Validation](https://mikro-orm.io/docs/property-validation)
- [Lifecycle Hooks](https://mikro-orm.io/docs/events#hooks)
- [Vanilla JS Support](https://mikro-orm.io/docs/usage-with-js)
- [Schema Generator](https://mikro-orm.io/docs/schema-generator)
- [Entity Generator](https://mikro-orm.io/docs/entity-generator)

## 📦 Example Integrations
You can find example integrations for some popular frameworks in the [`mikro-orm-examples` repository](https://github.com/mikro-orm/mikro-orm-examples):

## TypeScript Examples
- [Express + MongoDB](https://github.com/mikro-orm/express-ts-example-app)
- [Nest + MySQL](https://github.com/mikro-orm/nestjs-example-app)
- [RealWorld example app (Nest + MySQL)](https://github.com/mikro-orm/nestjs-realworld-example-app)
- [Koa + SQLite](https://github.com/mikro-orm/koa-ts-example-app)
- [GraphQL + PostgreSQL](https://github.com/driescroons/mikro-orm-graphql-example)
- [Inversify + PostgreSQL](https://github.com/PodaruDragos/inversify-example-app)
- [NextJS + MySQL](https://github.com/jonahallibone/mikro-orm-nextjs)
- [Accounts.js REST and GraphQL authentication + SQLite](https://github.com/darkbasic/mikro-orm-accounts-example)
- [Nest + Shopify + PostgreSQL + GraphQL](https://github.com/Cloudshelf/Shopify_CSConnector)
- [Elysia.js + libSQL + Bun](https://github.com/mikro-orm/elysia-bun-example-app)
- [Electron.js + PostgreSQL](https://github.com/adnanlah/electron-mikro-orm-example-app)

## JavaScript Examples
- [Express + SQLite](https://github.com/mikro-orm/express-js-example-app)

## 🚀 Quick Start
First install the module via `yarn` or `npm` and do not forget to install the database driver as well:
> Since v4, you should install the driver package, but not the db connector itself, e.g. install `@mikro-orm/sqlite`, but not `sqlite3` as that is already included in the driver package.
```sh
yarn add @mikro-orm/core @mikro-orm/mongodb       # for mongo
yarn add @mikro-orm/core @mikro-orm/mysql         # for mysql/mariadb
yarn add @mikro-orm/core @mikro-orm/mariadb       # for mysql/mariadb
yarn add @mikro-orm/core @mikro-orm/postgresql    # for postgresql
yarn add @mikro-orm/core @mikro-orm/mssql         # for mssql
yarn add @mikro-orm/core @mikro-orm/sqlite        # for sqlite
yarn add @mikro-orm/core @mikro-orm/better-sqlite # for better-sqlite
yarn add @mikro-orm/core @mikro-orm/libsql        # for libsql
```
or
```sh
npm i -s @mikro-orm/core @mikro-orm/mongodb       # for mongo
npm i -s @mikro-orm/core @mikro-orm/mysql         # for mysql/mariadb
npm i -s @mikro-orm/core @mikro-orm/mariadb       # for mysql/mariadb
npm i -s @mikro-orm/core @mikro-orm/postgresql    # for postgresql
npm i -s @mikro-orm/core @mikro-orm/mssql         # for mssql
npm i -s @mikro-orm/core @mikro-orm/sqlite        # for sqlite
npm i -s @mikro-orm/core @mikro-orm/better-sqlite # for better-sqlite
npm i -s @mikro-orm/core @mikro-orm/libsql        # for libsql
```
Next, if you want to use decorators for your entity definition, you will need to enable support for [decorators](https://www.typescriptlang.org/docs/handbook/decorators.html) as well as `esModuleInterop` in `tsconfig.json` via:
```json
"experimentalDecorators": true,
"emitDecoratorMetadata": true,
"esModuleInterop": true,
```
Alternatively, you can use [`EntitySchema`](https://mikro-orm.io/docs/entity-schema).
Then call `MikroORM.init` as part of bootstrapping your app:
> To access driver specific methods like `em.createQueryBuilder()` we need to specify the driver type when calling `MikroORM.init()`. Alternatively we can cast the `orm.em` to `EntityManager` exported from the driver package:
>
> ```ts
> const em = orm.em as EntityManager;
> const qb = em.createQueryBuilder(...);
> ```
```typescript
import type { PostgreSqlDriver } from '@mikro-orm/postgresql'; // or any other SQL driver package

const orm = await MikroORM.init<PostgreSqlDriver>({
  entities: ['./dist/entities'], // path to your JS entities (dist), relative to `baseDir`
  dbName: 'my-db-name',
  type: 'postgresql',
});
console.log(orm.em); // access EntityManager via `em` property
```
There are more ways to configure your entities, take a look at [installation page](https://mikro-orm.io/docs/installation/).
> Read more about all the possible configuration options in [Advanced Configuration](https://mikro-orm.io/docs/configuration) section.
Then you will need to fork entity manager for each request so their [identity maps](https://mikro-orm.io/docs/identity-map/) will not collide. To do so, use the `RequestContext` helper:
```typescript
const app = express();

app.use((req, res, next) => {
  RequestContext.create(orm.em, next);
});
```
> You should register this middleware as the last one just before request handlers and before any of your custom middleware that is using the ORM. There might be issues when you register it before request processing middleware like `queryParser` or `bodyParser`, so definitely register the context after them.
More info about `RequestContext` is described [here](https://mikro-orm.io/docs/identity-map/#request-context).
Now you can start defining your entities (in one of the `entities` folders). This is how simple entity can look like in mongo driver:
**`./entities/MongoBook.ts`**
```typescript
@Entity()
export class MongoBook {

  @PrimaryKey()
  _id: ObjectID;

  @SerializedPrimaryKey()
  id: string;

  @Property()
  title: string;

  @ManyToOne(() => Author)
  author: Author;

  @ManyToMany(() => BookTag)
  tags = new Collection<BookTag>(this);

  constructor(title: string, author: Author) {
    this.title = title;
    this.author = author;
  }

}
```
For SQL drivers, you can use `id: number` PK:
**`./entities/SqlBook.ts`**
```typescript
@Entity()
export class SqlBook {

  @PrimaryKey()
  id: number;

}
```
Or if you want to use UUID primary keys:
**`./entities/UuidBook.ts`**
```typescript
import { randomUUID } from 'node:crypto';

@Entity()
export class UuidBook {

  @PrimaryKey()
  uuid = randomUUID();

}
```
More information can be found in [defining entities section](https://mikro-orm.io/docs/defining-entities/) in docs.
When you have your entities defined, you can start using ORM either via `EntityManager` or via `EntityRepository`s.
To save entity state to database, you need to persist it. Persist takes care or deciding whether to use `insert` or `update` and computes appropriate change-set. Entity references that are not persisted yet (does not have identifier) will be cascade persisted automatically.
```typescript
// use constructors in your entities for required parameters
const author = new Author('Jon Snow', 'snow@wall.st');
author.born = new Date();

const publisher = new Publisher('7K publisher');

const book1 = new Book('My Life on The Wall, part 1', author);
book1.publisher = publisher;
const book2 = new Book('My Life on The Wall, part 2', author);
book2.publisher = publisher;
const book3 = new Book('My Life on The Wall, part 3', author);
book3.publisher = publisher;

// just persist books, author and publisher will be automatically cascade persisted
await em.persistAndFlush([book1, book2, book3]);
```
To fetch entities from database you can use `find()` and `findOne()` of `EntityManager`:
```typescript
const authors = em.find(Author, {}, { populate: ['books'] });

for (const author of authors) {
  console.log(author); // instance of Author entity
  console.log(author.name); // Jon Snow

  for (const book of author.books) { // iterating books collection
    console.log(book); // instance of Book entity
    console.log(book.title); // My Life on The Wall, part 1/2/3
  }
}
```
More convenient way of fetching entities from database is by using `EntityRepository`, that carries the entity name, so you do not have to pass it to every `find` and `findOne` calls:
```typescript
const booksRepository = em.getRepository(Book);

const books = await booksRepository.find({ author: '...' }, { 
  populate: ['author'],
  limit: 1,
  offset: 2,
  orderBy: { title: QueryOrder.DESC },
});

console.log(books); // Loaded<Book, 'author'>[]
```
Take a look at docs about [working with `EntityManager`](https://mikro-orm.io/docs/entity-manager/) or [using `EntityRepository` instead](https://mikro-orm.io/docs/repositories/).

## 🤝 Contributing
Contributions, issues and feature requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on the process for submitting pull requests to us.

## Authors
👤 **Martin Adámek**
- Twitter: [@B4nan](https://twitter.com/B4nan)
- Github: [@b4nan](https://github.com/b4nan)
See also the list of contributors who [participated](https://github.com/mikro-orm/mikro-orm/contributors) in this project.

## Show Your Support
Please ⭐️ this repository if this project helped you!
> If you'd like to support my open-source work, consider sponsoring me directly at [github.com/sponsors/b4nan](https://github.com/sponsors/b4nan).

## 📝 License
Copyright © 2018 [Martin Adámek](https://github.com/b4nan).
This project is licensed under the MIT License - see the [LICENSE file](LICENSE) for details.

---

# iCloud: web-app/node_modules/@mikro-orm/core/README.md

> **Source:** icloud://web-app/node_modules/@mikro-orm/core/README.md
> **Analyzed At:** 2026-06-13T06:32:46.552Z

## 🤔 Unit of What?
You might be asking: _What the hell is Unit of Work and why should I care about it?_
> Unit of Work maintains a list of objects (_entities_) affected by a business transaction
> and coordinates the writing out of changes. [(Martin Fowler)](https://www.martinfowler.com/eaaCatalog/unitOfWork.html)
> Identity Map ensures that each object (_entity_) gets loaded only once by keeping every
> loaded object in a map. Looks up objects using the map when referring to them.
> [(Martin Fowler)](https://www.martinfowler.com/eaaCatalog/identityMap.html)
So what benefits does it bring to us?

## Implicit Transactions
First and most important implication of having Unit of Work is that it allows handling transactions automatically.
When you call `em.flush()`, all computed changes are queried inside a database transaction (if supported by given driver). This means that you can control the boundaries of transactions simply by calling `em.persistLater()` and once all your changes are ready, calling `flush()` will run them inside a transaction.
> You can also control the transaction boundaries manually via `em.transactional(cb)`.
```typescript
const user = await em.findOneOrFail(User, 1);
user.email = 'foo@bar.com';
const car = new Car();
user.cars.add(car);

// thanks to bi-directional cascading we only need to persist user entity
// flushing will create a transaction, insert new car and update user with new email
// as user entity is managed, calling flush() is enough
await em.flush();
```

## ChangeSet based persistence
MikroORM allows you to implement your domain/business logic directly in the entities. To maintain always valid entities, you can use constructors to mark required properties. Let's define the `User` entity used in previous example:
```typescript
@Entity()
export class User {

  @PrimaryKey()
  id!: number;

  @Property()
  name!: string;

  @OneToOne(() => Address)
  address?: Address;

  @ManyToMany(() => Car)
  cars = new Collection<Car>(this);

  constructor(name: string) {
    this.name = name;
  }

}
```
Now to create new instance of the `User` entity, we are forced to provide the `name`:
```typescript
const user = new User('John Doe'); // name is required to create new user instance
user.address = new Address('10 Downing Street'); // address is optional
```
Once your entities are loaded, make a number of synchronous actions on your entities,
then call `em.flush()`. This will trigger computing of change sets. Only entities
(and properties) that were changed will generate database queries, if there are no changes,
no transaction will be started.
```typescript
const user = await em.findOneOrFail(User, 1, {
  populate: ['cars', 'address.city'],
});
user.title = 'Mr.';
user.address.street = '10 Downing Street'; // address is 1:1 relation of Address entity
user.cars.getItems().forEach(car => car.forSale = true); // cars is 1:m collection of Car entities
const car = new Car('VW');
user.cars.add(car);

// now we can flush all changes done to managed entities
await em.flush();
```
`em.flush()` will then execute these queries from the example above:
```sql
begin;
update "user" set "title" = 'Mr.' where "id" = 1;
update "user_address" set "street" = '10 Downing Street' where "id" = 123;
update "car"
  set "for_sale" = case
    when ("id" = 1) then true
    when ("id" = 2) then true
    when ("id" = 3) then true
    else "for_sale" end
  where "id" in (1, 2, 3)
insert into "car" ("brand", "owner") values ('VW', 1);
commit;
```

## Identity Map
Thanks to Identity Map, you will always have only one instance of given entity in one context. This allows for some optimizations (skipping loading of already loaded entities), as well as comparison by identity (`ent1 === ent2`).

## 📖 Documentation
MikroORM documentation, included in this repo in the root directory, is built with [Docusaurus](https://docusaurus.io) and publicly hosted on GitHub Pages at https://mikro-orm.io.
There is also auto-generated [CHANGELOG.md](CHANGELOG.md) file based on commit messages (via `semantic-release`).

## ✨ Core Features
- [Clean and Simple Entity Definition](https://mikro-orm.io/docs/defining-entities)
- [Identity Map](https://mikro-orm.io/docs/identity-map)
- [Entity References](https://mikro-orm.io/docs/entity-references)
- [Using Entity Constructors](https://mikro-orm.io/docs/entity-constructors)
- [Modelling Relationships](https://mikro-orm.io/docs/relationships)
- [Collections](https://mikro-orm.io/docs/collections)
- [Unit of Work](https://mikro-orm.io/docs/unit-of-work)
- [Transactions](https://mikro-orm.io/docs/transactions)
- [Cascading persist and remove](https://mikro-orm.io/docs/cascading)
- [Composite and Foreign Keys as Primary Key](https://mikro-orm.io/docs/composite-keys)
- [Filters](https://mikro-orm.io/docs/filters)
- [Using `QueryBuilder`](https://mikro-orm.io/docs/query-builder)
- [Populating relations](https://mikro-orm.io/docs/populating-relations)
- [Property Validation](https://mikro-orm.io/docs/property-validation)
- [Lifecycle Hooks](https://mikro-orm.io/docs/events#hooks)
- [Vanilla JS Support](https://mikro-orm.io/docs/usage-with-js)
- [Schema Generator](https://mikro-orm.io/docs/schema-generator)
- [Entity Generator](https://mikro-orm.io/docs/entity-generator)

## 📦 Example Integrations
You can find example integrations for some popular frameworks in the [`mikro-orm-examples` repository](https://github.com/mikro-orm/mikro-orm-examples):

## TypeScript Examples
- [Express + MongoDB](https://github.com/mikro-orm/express-ts-example-app)
- [Nest + MySQL](https://github.com/mikro-orm/nestjs-example-app)
- [RealWorld example app (Nest + MySQL)](https://github.com/mikro-orm/nestjs-realworld-example-app)
- [Koa + SQLite](https://github.com/mikro-orm/koa-ts-example-app)
- [GraphQL + PostgreSQL](https://github.com/driescroons/mikro-orm-graphql-example)
- [Inversify + PostgreSQL](https://github.com/PodaruDragos/inversify-example-app)
- [NextJS + MySQL](https://github.com/jonahallibone/mikro-orm-nextjs)
- [Accounts.js REST and GraphQL authentication + SQLite](https://github.com/darkbasic/mikro-orm-accounts-example)
- [Nest + Shopify + PostgreSQL + GraphQL](https://github.com/Cloudshelf/Shopify_CSConnector)
- [Elysia.js + libSQL + Bun](https://github.com/mikro-orm/elysia-bun-example-app)
- [Electron.js + PostgreSQL](https://github.com/adnanlah/electron-mikro-orm-example-app)

## JavaScript Examples
- [Express + SQLite](https://github.com/mikro-orm/express-js-example-app)

## 🚀 Quick Start
First install the module via `yarn` or `npm` and do not forget to install the database driver as well:
> Since v4, you should install the driver package, but not the db connector itself, e.g. install `@mikro-orm/sqlite`, but not `sqlite3` as that is already included in the driver package.
```sh
yarn add @mikro-orm/core @mikro-orm/mongodb       # for mongo
yarn add @mikro-orm/core @mikro-orm/mysql         # for mysql/mariadb
yarn add @mikro-orm/core @mikro-orm/mariadb       # for mysql/mariadb
yarn add @mikro-orm/core @mikro-orm/postgresql    # for postgresql
yarn add @mikro-orm/core @mikro-orm/mssql         # for mssql
yarn add @mikro-orm/core @mikro-orm/sqlite        # for sqlite
yarn add @mikro-orm/core @mikro-orm/better-sqlite # for better-sqlite
yarn add @mikro-orm/core @mikro-orm/libsql        # for libsql
```
or
```sh
npm i -s @mikro-orm/core @mikro-orm/mongodb       # for mongo
npm i -s @mikro-orm/core @mikro-orm/mysql         # for mysql/mariadb
npm i -s @mikro-orm/core @mikro-orm/mariadb       # for mysql/mariadb
npm i -s @mikro-orm/core @mikro-orm/postgresql    # for postgresql
npm i -s @mikro-orm/core @mikro-orm/mssql         # for mssql
npm i -s @mikro-orm/core @mikro-orm/sqlite        # for sqlite
npm i -s @mikro-orm/core @mikro-orm/better-sqlite # for better-sqlite
npm i -s @mikro-orm/core @mikro-orm/libsql        # for libsql
```
Next, if you want to use decorators for your entity definition, you will need to enable support for [decorators](https://www.typescriptlang.org/docs/handbook/decorators.html) as well as `esModuleInterop` in `tsconfig.json` via:
```json
"experimentalDecorators": true,
"emitDecoratorMetadata": true,
"esModuleInterop": true,
```
Alternatively, you can use [`EntitySchema`](https://mikro-orm.io/docs/entity-schema).
Then call `MikroORM.init` as part of bootstrapping your app:
> To access driver specific methods like `em.createQueryBuilder()` we need to specify the driver type when calling `MikroORM.init()`. Alternatively we can cast the `orm.em` to `EntityManager` exported from the driver package:
>
> ```ts
> const em = orm.em as EntityManager;
> const qb = em.createQueryBuilder(...);
> ```
```typescript
import type { PostgreSqlDriver } from '@mikro-orm/postgresql'; // or any other SQL driver package

const orm = await MikroORM.init<PostgreSqlDriver>({
  entities: ['./dist/entities'], // path to your JS entities (dist), relative to `baseDir`
  dbName: 'my-db-name',
  type: 'postgresql',
});
console.log(orm.em); // access EntityManager via `em` property
```
There are more ways to configure your entities, take a look at [installation page](https://mikro-orm.io/docs/installation/).
> Read more about all the possible configuration options in [Advanced Configuration](https://mikro-orm.io/docs/configuration) section.
Then you will need to fork entity manager for each request so their [identity maps](https://mikro-orm.io/docs/identity-map/) will not collide. To do so, use the `RequestContext` helper:
```typescript
const app = express();

app.use((req, res, next) => {
  RequestContext.create(orm.em, next);
});
```
> You should register this middleware as the last one just before request handlers and before any of your custom middleware that is using the ORM. There might be issues when you register it before request processing middleware like `queryParser` or `bodyParser`, so definitely register the context after them.
More info about `RequestContext` is described [here](https://mikro-orm.io/docs/identity-map/#request-context).
Now you can start defining your entities (in one of the `entities` folders). This is how simple entity can look like in mongo driver:
**`./entities/MongoBook.ts`**
```typescript
@Entity()
export class MongoBook {

  @PrimaryKey()
  _id: ObjectID;

  @SerializedPrimaryKey()
  id: string;

  @Property()
  title: string;

  @ManyToOne(() => Author)
  author: Author;

  @ManyToMany(() => BookTag)
  tags = new Collection<BookTag>(this);

  constructor(title: string, author: Author) {
    this.title = title;
    this.author = author;
  }

}
```
For SQL drivers, you can use `id: number` PK:
**`./entities/SqlBook.ts`**
```typescript
@Entity()
export class SqlBook {

  @PrimaryKey()
  id: number;

}
```
Or if you want to use UUID primary keys:
**`./entities/UuidBook.ts`**
```typescript
import { randomUUID } from 'node:crypto';

@Entity()
export class UuidBook {

  @PrimaryKey()
  uuid = randomUUID();

}
```
More information can be found in [defining entities section](https://mikro-orm.io/docs/defining-entities/) in docs.
When you have your entities defined, you can start using ORM either via `EntityManager` or via `EntityRepository`s.
To save entity state to database, you need to persist it. Persist takes care or deciding whether to use `insert` or `update` and computes appropriate change-set. Entity references that are not persisted yet (does not have identifier) will be cascade persisted automatically.
```typescript
// use constructors in your entities for required parameters
const author = new Author('Jon Snow', 'snow@wall.st');
author.born = new Date();

const publisher = new Publisher('7K publisher');

const book1 = new Book('My Life on The Wall, part 1', author);
book1.publisher = publisher;
const book2 = new Book('My Life on The Wall, part 2', author);
book2.publisher = publisher;
const book3 = new Book('My Life on The Wall, part 3', author);
book3.publisher = publisher;

// just persist books, author and publisher will be automatically cascade persisted
await em.persistAndFlush([book1, book2, book3]);
```
To fetch entities from database you can use `find()` and `findOne()` of `EntityManager`:
```typescript
const authors = em.find(Author, {}, { populate: ['books'] });

for (const author of authors) {
  console.log(author); // instance of Author entity
  console.log(author.name); // Jon Snow

  for (const book of author.books) { // iterating books collection
    console.log(book); // instance of Book entity
    console.log(book.title); // My Life on The Wall, part 1/2/3
  }
}
```
More convenient way of fetching entities from database is by using `EntityRepository`, that carries the entity name, so you do not have to pass it to every `find` and `findOne` calls:
```typescript
const booksRepository = em.getRepository(Book);

const books = await booksRepository.find({ author: '...' }, { 
  populate: ['author'],
  limit: 1,
  offset: 2,
  orderBy: { title: QueryOrder.DESC },
});

console.log(books); // Loaded<Book, 'author'>[]
```
Take a look at docs about [working with `EntityManager`](https://mikro-orm.io/docs/entity-manager/) or [using `EntityRepository` instead](https://mikro-orm.io/docs/repositories/).

## 🤝 Contributing
Contributions, issues and feature requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on the process for submitting pull requests to us.

## Authors
👤 **Martin Adámek**
- Twitter: [@B4nan](https://twitter.com/B4nan)
- Github: [@b4nan](https://github.com/b4nan)
See also the list of contributors who [participated](https://github.com/mikro-orm/mikro-orm/contributors) in this project.

## Show Your Support
Please ⭐️ this repository if this project helped you!
> If you'd like to support my open-source work, consider sponsoring me directly at [github.com/sponsors/b4nan](https://github.com/sponsors/b4nan).

## 📝 License
Copyright © 2018 [Martin Adámek](https://github.com/b4nan).
This project is licensed under the MIT License - see the [LICENSE file](LICENSE) for details.

---

# iCloud: web-app/node_modules/@mediapipe/tasks-vision/README.md

> **Source:** icloud://web-app/node_modules/@mediapipe/tasks-vision/README.md
> **Analyzed At:** 2026-06-13T06:32:46.563Z

## MediaPipe Tasks Vision Package
This package contains the vision tasks for MediaPipe.

## Face Detector
The MediaPipe Face Detector task lets you detect the presence and location of
faces within images or videos.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const faceDetector = await FaceDetector.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite"
);
const image = document.getElementById("image") as HTMLImageElement;
const detections = faceDetector.detect(image);
```
For more information, refer to the [Face Detector](https://developers.google.com/mediapipe/solutions/vision/face_detector/web_js) documentation.

## Face Landmarker
The MediaPipe Face Landmarker task lets you detect the landmarks of faces in
an image. You can use this Task to localize key points of a face and render
visual effects over the faces.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const faceLandmarker = await FaceLandmarker.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
);
const image = document.getElementById("image") as HTMLImageElement;
const landmarks = faceLandmarker.detect(image);
```
For more information, refer to the [Face Landmarker](https://developers.google.com/mediapipe/solutions/vision/face_landmarker/web_js) documentation.

## Face Stylizer
The MediaPipe Face Stylizer lets you perform face stylization on images.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const faceStylizer = await FaceStylizer.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/face_stylizer/blaze_face_stylizer/float32/1/blaze_face_stylizer.task"
);
const image = document.getElementById("image") as HTMLImageElement;
const stylizedImage = faceStylizer.stylize(image);
```

## Gesture Recognizer
The MediaPipe Gesture Recognizer task lets you recognize hand gestures in real
time, and provides the recognized hand gesture results along with the landmarks
of the detected hands. You can use this task to recognize specific hand gestures
from a user, and invoke application features that correspond to those gestures.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const gestureRecognizer = await GestureRecognizer.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task"
);
const image = document.getElementById("image") as HTMLImageElement;
const recognitions = gestureRecognizer.recognize(image);
```
For more information, refer to the [Gesture Recognizer](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/web_js) documentation.

## Hand Landmarker
The MediaPipe Hand Landmarker task lets you detect the landmarks of the hands in
an image. You can use this Task to localize key points of the hands and render
visual effects over the hands.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const handLandmarker = await HandLandmarker.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
);
const image = document.getElementById("image") as HTMLImageElement;
const landmarks = handLandmarker.detect(image);
```
For more information, refer to the [Hand Landmarker](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/web_js) documentation.

## Holistic Landmarker
The MediaPipe Holistic Landmarker task task lets you combine components of the
pose, face, and hand landmarkers to create a complete landmarker for the human
body.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const holisticLandmarker = await HolisticLandmarker.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/holistic_landmarker/holistic_landmarker/float16/1/hand_landmark.task"
);
const image = document.getElementById("image") as HTMLImageElement;
const landmarks = holisticLandmarker.detect(image);
```

## Image Classifier
The MediaPipe Image Classifier task lets you perform classification on images.
You can use this task to identify what an image represents among a set of
categories defined at training time.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const imageClassifier = await ImageClassifier.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/image_classifier/efficientnet_lite0/float32/1/efficientnet_lite0.tflite"
);
const image = document.getElementById("image") as HTMLImageElement;
const classifications = imageClassifier.classify(image);
```
For more information, refer to the [Image Classifier](https://developers.google.com/mediapipe/solutions/vision/image_classifier/web_js) documentation.

## Image Embedder
The MediaPipe Image Embedder extracts embeddings from an image.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const imageEmbedder = await ImageEmbedder.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/image_embedder/mobilenet_v3_small/float32/1/mobilenet_v3_small.tflite"
);
const image = document.getElementById("image") as HTMLImageElement;
const embeddings = imageSegmenter.embed(image);
```

## Image Segmenter
The MediaPipe Image Segmenter lets you segment an image into categories.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const imageSegmenter = await ImageSegmenter.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/image_segmenter/deeplab_v3/float32/1/deeplab_v3.tflite"
);
const image = document.getElementById("image") as HTMLImageElement;
imageSegmenter.segment(image, (masks, width, height) => {
  ...
});
```
For more information, refer to the [Image Segmenter](https://developers.google.com/mediapipe/solutions/vision/image_segmenter/web_js) documentation.

## Interactive Segmenter
The MediaPipe Interactive Segmenter lets you select a region of interest to
segment an image by.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const interactiveSegmenter = await InteractiveSegmenter.createFromModelPath(
    vision,
    "https://storage.googleapis.com/mediapipe-models/interactive_segmenter/magic_touch/float32/1/magic_touch.tflite"
);
const image = document.getElementById("image") as HTMLImageElement;
interactiveSegmenter.segment(image, { keypoint: { x: 0.1, y: 0.2 } },
    (masks, width, height) => { ... }
);
```
For more information, refer to the [Interactive Segmenter](https://developers.google.com/mediapipe/solutions/vision/interactive_segmenter/web_js) documentation.

## Object Detector
The MediaPipe Object Detector task lets you detect the presence and location of
multiple classes of objects within images or videos.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const objectDetector = await ObjectDetector.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/float16/1/efficientdet_lite0.tflite"
);
const image = document.getElementById("image") as HTMLImageElement;
const detections = objectDetector.detect(image);
```
For more information, refer to the [Object Detector](https://developers.google.com/mediapipe/solutions/vision/object_detector/web_js) documentation.

## Pose Landmarker
The MediaPipe Pose Landmarker task lets you detect the landmarks of body poses
in an image. You can use this Task to localize key points of a pose and render
visual effects over the body.
```
const vision = await FilesetResolver.forVisionTasks(
    "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm"
);
const poseLandmarker = await PoseLandmarker.createFromModelPath(vision,
    "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task
);
const image = document.getElementById("image") as HTMLImageElement;
const landmarks = poseLandmarker.detect(image);
```
For more information, refer to the [Pose Landmarker](https://developers.google.com/mediapipe/solutions/vision/pose_landmarker/web_js) documentation.

---

# iCloud: web-app/node_modules/@langchain/langgraph-checkpoint/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@langchain/langgraph-checkpoint/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.566Z

## Major Changes
- 1e1ecbb: This release updates the package for compatibility with LangGraph v1.0. See the [v1.0 release notes](https://docs.langchain.com/oss/javascript/releases/langgraph-v1) for details on what's new.

## Patch Changes
- 11c7807: Add support for @langchain/core 1.0.0-alpha

## Minor Changes
- 10f292a: Remove pending_sends from parent checkpoints in favour of TASKS channel
- 3fd7f73: Allow asynchronous serialization and deserialization
- 773ec0d: Remove Checkpoint.writes

## Patch Changes
- ccbcbc1: Add delete thread method to checkpointers

---

# iCloud: web-app/node_modules/@langchain/langgraph-checkpoint/README.md

> **Source:** icloud://web-app/node_modules/@langchain/langgraph-checkpoint/README.md
> **Analyzed At:** 2026-06-13T06:32:46.569Z

## @langchain/langgraph-checkpoint
This library defines the base interface for [LangGraph.js](https://github.com/langchain-ai/langgraphjs) checkpointers. Checkpointers provide persistence layer for LangGraph. They allow you to interact with and manage the graph's state. When you use a graph with a checkpointer, the checkpointer saves a _checkpoint_ of the graph state at every superstep, enabling several powerful capabilities like human-in-the-loop, "memory" between interactions and more.

## Checkpoint
Checkpoint is a snapshot of the graph state at a given point in time. Checkpoint tuple refers to an object containing checkpoint and the associated config, metadata and pending writes.

## Thread
Threads enable the checkpointing of multiple different runs, making them essential for multi-tenant chat applications and other scenarios where maintaining separate states is necessary. A thread is a unique ID assigned to a series of checkpoints saved by a checkpointer. When using a checkpointer, you must specify a `thread_id` and optionally `checkpoint_id` when running the graph.
- `thread_id` is simply the ID of a thread. This is always required
- `checkpoint_id` can optionally be passed. This identifier refers to a specific checkpoint within a thread. This can be used to kick of a run of a graph from some point halfway through a thread.
You must pass these when invoking the graph as part of the configurable part of the config, e.g.
```ts
{ configurable: { thread_id: "1" } }  // valid config
{ configurable: { thread_id: "1", checkpoint_id: "0c62ca34-ac19-445d-bbb0-5b4984975b2a" } }  // also valid config
```

## Serde
`@langchain/langgraph-checkpoint` also defines protocol for serialization/deserialization (serde) and provides an default implementation that handles a range of types.

## Pending writes
When a graph node fails mid-execution at a given superstep, LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that superstep, so that whenever we resume graph execution from that superstep we don't re-run the successful nodes.

## Interface
Each checkpointer should conform to `BaseCheckpointSaver` interface and must implement the following methods:
- `.put` - Store a checkpoint with its configuration and metadata.
- `.putWrites` - Store intermediate writes linked to a checkpoint (i.e. pending writes).
- `.getTuple` - Fetch a checkpoint tuple using for a given configuration (`thread_id` and `thread_ts`).
- `.list` - List checkpoints that match a given configuration and filter criteria.

## Usage
```ts
import { MemorySaver } from "@langchain/langgraph-checkpoint";

const writeConfig = {
  configurable: {
    thread_id: "1",
    checkpoint_ns: ""
  }
};
const readConfig = {
  configurable: {
    thread_id: "1"
  }
};

const checkpointer = new MemorySaver();
const checkpoint = {
  v: 1,
  ts: "2024-07-31T20:14:19.804150+00:00",
  id: "1ef4f797-8335-6428-8001-8a1503f9b875",
  channel_values: {
    my_key: "meow",
    node: "node"
  },
  channel_versions: {
    __start__: 2,
    my_key: 3,
    "start:node": 3,
    node: 3
  },
  versions_seen: {
    __input__: {},
    __start__: {
      __start__: 1
    },
    node: {
      "start:node": 2
    }
  },
  pending_sends: [],
}

// store checkpoint
await checkpointer.put(writeConfig, checkpoint, {}, {})

// load checkpoint
await checkpointer.get(readConfig)

// list checkpoints
for await (const checkpoint of checkpointer.list(readConfig)) {
  console.log(checkpoint);
}
```

---

# iCloud: web-app/node_modules/@langchain/langgraph-checkpoint/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@langchain/langgraph-checkpoint/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.574Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@langchain/langgraph/README.md

> **Source:** icloud://web-app/node_modules/@langchain/langgraph/README.md
> **Analyzed At:** 2026-06-13T06:32:46.596Z

## 🦜🕸️LangGraph.js
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://langchain-ai.github.io/langgraphjs/)
![Version](https://img.shields.io/npm/v/@langchain/langgraph?logo=npm)
[![Downloads](https://img.shields.io/npm/dm/@langchain/langgraph)](https://www.npmjs.com/package/@langchain/langgraph)
[![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langgraphjs)](https://github.com/langchain-ai/langgraphjs/issues)
> [!NOTE]
> Looking for the Python version? See the [Python repo](https://github.com/langchain-ai/langgraph) and the [Python docs](https://docs.langchain.com/oss/python/langgraph/overview).
LangGraph — used by Replit, Uber, LinkedIn, GitLab and more — is a low-level orchestration framework for building controllable agents. While langchain provides integrations and composable components to streamline LLM application development, the LangGraph library enables agent orchestration — offering customizable architectures, long-term memory, and human-in-the-loop to reliably handle complex tasks.
```bash
npm install @langchain/langgraph @langchain/core
```
To learn more about how to use LangGraph, check out [the docs](https://langchain-ai.github.io/langgraphjs/). We show a simple example below of how to create a ReAct agent.
```ts
// npm install @langchain-anthropic
import { createReactAgent, tool } from "langchain";
import { ChatAnthropic } from "@langchain/anthropic";

import { z } from "zod";

const search = tool(
  async ({ query }) => {
    if (
      query.toLowerCase().includes("sf") ||
      query.toLowerCase().includes("san francisco")
    ) {
      return "It's 60 degrees and foggy.";
    }
    return "It's 90 degrees and sunny.";
  },
  {
    name: "search",
    description: "Call to surf the web.",
    schema: z.object({
      query: z.string().describe("The query to use in your search."),
    }),
  }
);

const model = new ChatAnthropic({
  model: "claude-3-7-sonnet-latest",
});

const agent = createReactAgent({
  llm: model,
  tools: [search],
});

const result = await agent.invoke({
  messages: [
    {
      role: "user",
      content: "what is the weather in sf",
    },
  ],
});
```

## Full-stack Quickstart
Get started quickly by building a full-stack LangGraph application using the [`create-agent-chat-app`](https://www.npmjs.com/package/create-agent-chat-app) CLI:
```bash
npx create-agent-chat-app@latest
```
The CLI sets up a chat interface and helps you configure your application, including:
- 🧠 Choice of 4 prebuilt agents (ReAct, Memory, Research, Retrieval)
- 🌐 Frontend framework (Next.js or Vite)
- 📦 Package manager (`npm`, `yarn`, or `pnpm`)

## Why use LangGraph?
LangGraph is built for developers who want to build powerful, adaptable AI agents. Developers choose LangGraph for:
- **Reliability and controllability.** Steer agent actions with moderation checks and human-in-the-loop approvals. LangGraph persists context for long-running workflows, keeping your agents on course.
- **Low-level and extensible.** Build custom agents with fully descriptive, low-level primitives – free from rigid abstractions that limit customization. Design scalable multi-agent systems, with each agent serving a specific role tailored to your use case.
- **First-class streaming support.** With token-by-token streaming and streaming of intermediate steps, LangGraph gives users clear visibility into agent reasoning and actions as they unfold in real time.
LangGraph is trusted in production and powering agents for companies like:
- [Klarna](https://blog.langchain.dev/customers-klarna/): Customer support bot for 85 million active users
- [Elastic](https://www.elastic.co/blog/elastic-security-generative-ai-features): Security AI assistant for threat detection
- [Uber](https://dpe.org/sessions/ty-smith-adam-huda/this-year-in-ubers-ai-driven-developer-productivity-revolution/): Automated unit test generation
- [Replit](https://www.langchain.com/breakoutagents/replit): Code generation
- And many more ([see list here](https://www.langchain.com/built-with-langgraph))

## LangGraph’s ecosystem
While LangGraph can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools for building agents. To improve your LLM application development, pair LangGraph with:
- [LangSmith](http://www.langchain.com/langsmith) — Helpful for agent evals and observability. Debug poor-performing LLM app runs, evaluate agent trajectories, gain visibility in production, and improve performance over time.
- [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/#langgraph-platform) — Deploy and scale agents effortlessly with a purpose-built deployment platform for long running, stateful workflows. Discover, reuse, configure, and share agents across teams — and iterate quickly with visual prototyping in [LangGraph Studio](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio/).

## Pairing with LangGraph Platform
While LangGraph is our open-source agent orchestration framework, enterprises that need scalable agent deployment can benefit from [LangGraph Platform](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_platform/).
LangGraph Platform can help engineering teams:
- **Accelerate agent development**: Quickly create agent UXs with configurable templates and [LangGraph Studio](https://langchain-ai.github.io/langgraphjs/concepts/langgraph_studio/) for visualizing and debugging agent interactions.
- **Deploy seamlessly**: We handle the complexity of deploying your agent. LangGraph Platform includes robust APIs for memory, threads, and cron jobs plus auto-scaling task queues & servers.
- **Centralize agent management & reusability**: Discover, reuse, and manage agents across the organization. Business users can also modify agents without coding.

## Additional resources
- [LangChain Forum](https://forum.langchain.com/): Connect with the community and share all of your technical questions, ideas, and feedback.
- [LangChain Academy](https://academy.langchain.com/courses/intro-to-langgraph): Learn the basics of LangGraph in our free, structured course.
- [Tutorials](https://langchain-ai.github.io/langgraphjs/tutorials/): Simple walkthroughs with guided examples on getting started with LangGraph.
- [Templates](https://langchain-ai.github.io/langgraphjs/concepts/template_applications/): Pre-built reference apps for common agentic workflows (e.g. ReAct agent, memory, retrieval etc.) that can be cloned and adapted.
- [How-to Guides](https://langchain-ai.github.io/langgraphjs/how-tos/): Quick, actionable code snippets for topics such as streaming, adding memory & persistence, and design patterns (e.g. branching, subgraphs, etc.).
- [API Reference](https://langchain-ai.github.io/langgraphjs/reference/): Detailed reference on core classes, methods, how to use the graph and checkpointing APIs, and higher-level prebuilt components.
- [Built with LangGraph](https://www.langchain.com/built-with-langgraph): Hear how industry leaders use LangGraph to ship powerful, production-ready AI applications.

## Acknowledgements
LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) and [Apache Beam](https://beam.apache.org/). The public interface draws inspiration from [NetworkX](https://networkx.org/documentation/latest/). LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

---

# iCloud: web-app/node_modules/@langchain/langgraph/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@langchain/langgraph/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.599Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@langchain/langgraph/node_modules/@langchain/langgraph-sdk/README.md

> **Source:** icloud://web-app/node_modules/@langchain/langgraph/node_modules/@langchain/langgraph-sdk/README.md
> **Analyzed At:** 2026-06-13T06:32:46.608Z

## LangGraph JS/TS SDK
This repository contains the JS/TS SDK for interacting with the LangGraph REST API.

## Quick Start
To get started with the JS/TS SDK, [install the package](https://www.npmjs.com/package/@langchain/langgraph-sdk)
```bash
pnpm add @langchain/langgraph-sdk
```
You will need a running LangGraph API server. If you're running a server locally using `langgraph-cli`, SDK will automatically point at `http://localhost:8123`, otherwise
you would need to specify the server URL when creating a client.
```js
import { Client } from "@langchain/langgraph-sdk";

const client = new Client();

// List all assistants
const assistants = await client.assistants.search({
  metadata: null,
  offset: 0,
  limit: 10,
});

// We auto-create an assistant for each graph you register in config.
const agent = assistants[0];

// Start a new thread
const thread = await client.threads.create();

// Start a streaming run
const messages = [{ role: "human", content: "what's the weather in la" }];

const streamResponse = client.runs.stream(
  thread["thread_id"],
  agent["assistant_id"],
  {
    input: { messages },
  }
);

for await (const chunk of streamResponse) {
  console.log(chunk);
}
```

## Documentation
To generate documentation, run the following commands:
1. Generate docs.
pnpm typedoc
1. Consolidate doc files into one markdown file.
npx concat-md --decrease-title-levels --ignore=js_ts_sdk_ref.md --start-title-level-at 2 docs > docs/js_ts_sdk_ref.md
1. Copy `js_ts_sdk_ref.md` to MkDocs directory.
cp docs/js_ts_sdk_ref.md ../../docs/docs/cloud/reference/sdk/js_ts_sdk_ref.md

## Reference Documentation
The reference documentation is available [here](https://reference.langchain.com/javascript/modules/_langchain_langgraph-sdk.html).
More usage examples can be found [here](https://docs.langchain.com/langsmith/sdk#js).

## Change Log
The change log for new versions can be found [here](https://github.com/langchain-ai/langgraphjs/blob/main/libs/sdk/CHANGELOG.md).

---

# iCloud: web-app/node_modules/@langchain/google-vertexai/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@langchain/google-vertexai/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.646Z

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.25

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.24

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.23

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.22

## Patch Changes
- [#10106](https://github.com/langchain-ai/langchainjs/pull/10106) [`9f30267`](https://github.com/langchain-ai/langchainjs/commit/9f30267e95a2a42fac71f1d3674b84c5a190dbbc) Thanks [@hntrl](https://github.com/hntrl)! - Add package version metadata to runnable traces. Each package now stamps its version in `this.metadata.versions` at construction time, making version info available in LangSmith trace metadata.
- Updated dependencies [[`9f30267`](https://github.com/langchain-ai/langchainjs/commit/9f30267e95a2a42fac71f1d3674b84c5a190dbbc)]:
- @langchain/google-gauth@2.1.21

## Patch Changes
- [#10080](https://github.com/langchain-ai/langchainjs/pull/10080) [`b583729`](https://github.com/langchain-ai/langchainjs/commit/b583729e99cf0c035630f6b311c4d069a1980cca) Thanks [@hntrl](https://github.com/hntrl)! - Add string-model constructor overloads for chat models (with supporting tests where applicable).
- Updated dependencies [[`b583729`](https://github.com/langchain-ai/langchainjs/commit/b583729e99cf0c035630f6b311c4d069a1980cca)]:
- @langchain/google-gauth@2.1.20

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.19

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.18

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.17

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.16

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.15

## Patch Changes
- [#9900](https://github.com/langchain-ai/langchainjs/pull/9900) [`a9b5059`](https://github.com/langchain-ai/langchainjs/commit/a9b50597186002221aaa4585246e569fa44c27c8) Thanks [@hntrl](https://github.com/hntrl)! - Improved abort signal handling for chat models:
- Added `ModelAbortError` class in `@langchain/core/errors` that contains partial output when a model invocation is aborted mid-stream
- `invoke()` now throws `ModelAbortError` with accumulated `partialOutput` when aborted during streaming (when using streaming callback handlers)
- `stream()` throws a regular `AbortError` when aborted (since chunks are already yielded to the caller)
- All provider implementations now properly check and propagate abort signals in both `_generate()` and `_streamResponseChunks()` methods
- Added standard tests for abort signal behavior
- Updated dependencies []:
- @langchain/google-gauth@2.1.14

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.13

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.12

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.11

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.10

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.9

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.8

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.7

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.6

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.5

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.4

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.3

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.2

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.1.1

## Patch Changes
- [#8951](https://github.com/langchain-ai/langchainjs/pull/8951) [`a2a0088`](https://github.com/langchain-ai/langchainjs/commit/a2a00880b80119eb926de05e9c556a44fd56632e) Thanks [@christian-bromann](https://github.com/christian-bromann)! - fix(google-common): handle unsupported Zod schema features for Gemini tools
- Updated dependencies []:
- @langchain/google-gauth@2.1.0

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.0.4

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.0.3

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.0.2

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@2.0.1

## Patch Changes
- [#9416](https://github.com/langchain-ai/langchainjs/pull/9416) [`0fe9beb`](https://github.com/langchain-ai/langchainjs/commit/0fe9bebee6710f719e47f913eec1ec4f638e4de4) Thanks [@hntrl](https://github.com/hntrl)! - fix 'moduleResultion: "node"' compatibility
- Updated dependencies [[`0fe9beb`](https://github.com/langchain-ai/langchainjs/commit/0fe9bebee6710f719e47f913eec1ec4f638e4de4)]:
- @langchain/google-gauth@2.0.0

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@1.0.3

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@1.0.2

## Patch Changes
- Updated dependencies []:
- @langchain/google-gauth@1.0.1

## 1.0.0
This release updates the package for compatibility with LangChain v1.0. See the v1.0 [release notes](https://docs.langchain.com/oss/javascript/releases/langchain-v1) for details on what's new.

## Patch Changes
- @langchain/google-gauth@0.2.18

## Patch Changes
- @langchain/google-gauth@0.2.17

---

# iCloud: web-app/node_modules/@langchain/google-vertexai/README.md

> **Source:** icloud://web-app/node_modules/@langchain/google-vertexai/README.md
> **Analyzed At:** 2026-06-13T06:32:46.649Z

## LangChain google-vertexai
This package contains resources to access Google AI/ML models
and other Google services via Vertex AI. Authorization to these
services use service account credentials stored on the local
file system or provided through the Google Cloud Platform
environment it is running on.
If you are running this on a platform where the credentials cannot
be provided this way, consider using the @langchain/google-vertexai-web
package _instead_. You do not need to use both packages. See the
section on **Authorization** below.

## Installation
```bash
$ pnpm install @langchain/google-vertexai
```

## Authorization
Authorization is done through a Google Cloud Service Account.
To handle service accounts, this package uses the `google-auth-library`
package, and you may wish to consult the documentation for that library
about how it does so. But in short, classes in this package will use
credentials from the first of the following that apply:
1. An API Key that is passed to the constructor using the `apiKey` attribute
2. Credentials that are passed to the constructor using the `authInfo` attribute
3. An API Key that is set in the environment variable `API_KEY`
4. The Service Account credentials that are saved in a file. The path to
this file is set in the `GOOGLE_APPLICATION_CREDENTIALS` environment
variable.
5. If you are running on a Google Cloud Platform resource, or if you have
logged in using `gcloud auth application-default login`, then the
default credentials.

## Tool Schema Limitations
When using tools with Gemini models through Vertex AI, be aware of the following Zod schema limitations:

## Unsupported Schema Features
1. **Discriminated Unions** - `.discriminatedUnion()` is not supported
   ```typescript
   // ❌ This will throw an error
   z.discriminatedUnion("type", [
     z.object({ type: z.literal("a"), value: z.string() }),
     z.object({ type: z.literal("b"), value: z.number() }),
   ]);

   // ✅ Use a flat object with optional fields instead
   z.object({
     type: z.enum(["a", "b"]),
     stringValue: z.string().optional(),
     numberValue: z.number().optional(),
   });
```
2. **Union Types** - `z.union()` is not supported
   ```typescript
   // ❌ This will throw an error
   z.union([z.string(), z.number()]);

   // ✅ Consider using separate optional fields
   z.object({
     stringValue: z.string().optional(),
     numberValue: z.number().optional(),
   });
```
3. **Positive Refinement** - `.positive()` is automatically converted
   ```typescript
   // ⚠️ This is automatically converted to .min(0.01)
   z.number().positive();

   // ✅ Prefer using .min() directly
   z.number().min(0.01);
```

## Error Messages
If you use unsupported schema features, you'll receive descriptive error messages:
- For union types: `"Gemini cannot handle union types (discriminatedUnion, anyOf, oneOf)"`
- For tool conversion failures: `"Failed to convert tool '[toolName]' schema for Gemini"`

## Best Practices
1. Use simple, flat object structures when possible
2. Replace discriminated unions with enums and optional fields
3. Use `.min()` instead of `.positive()` for number constraints
4. Test your tool schemas before deploying to production

---

# iCloud: web-app/node_modules/@langchain/google-gauth/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@langchain/google-gauth/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.654Z

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.25

## Patch Changes
- Updated dependencies [[`745b09a`](https://github.com/langchain-ai/langchainjs/commit/745b09a1b0c92643cbc99e773012924948438629)]:
- @langchain/google-common@2.1.24

## Patch Changes
- Updated dependencies [[`d43194b`](https://github.com/langchain-ai/langchainjs/commit/d43194b625f19acf79cbe958300dadb7b0a6a89d)]:
- @langchain/google-common@2.1.23

## Patch Changes
- Updated dependencies [[`3590ee3`](https://github.com/langchain-ai/langchainjs/commit/3590ee3229a9a55b0c818c1e396f6445b2368103)]:
- @langchain/google-common@2.1.22

## Patch Changes
- [#10106](https://github.com/langchain-ai/langchainjs/pull/10106) [`9f30267`](https://github.com/langchain-ai/langchainjs/commit/9f30267e95a2a42fac71f1d3674b84c5a190dbbc) Thanks [@hntrl](https://github.com/hntrl)! - Add package version metadata to runnable traces. Each package now stamps its version in `this.metadata.versions` at construction time, making version info available in LangSmith trace metadata.
- Updated dependencies [[`9f30267`](https://github.com/langchain-ai/langchainjs/commit/9f30267e95a2a42fac71f1d3674b84c5a190dbbc), [`e0e5a02`](https://github.com/langchain-ai/langchainjs/commit/e0e5a02ea1b855ad7b8d562d1c7770f984100a5d)]:
- @langchain/google-common@2.1.21

## Patch Changes
- [#10080](https://github.com/langchain-ai/langchainjs/pull/10080) [`b583729`](https://github.com/langchain-ai/langchainjs/commit/b583729e99cf0c035630f6b311c4d069a1980cca) Thanks [@hntrl](https://github.com/hntrl)! - Add string-model constructor overloads for chat models (with supporting tests where applicable).
- Updated dependencies []:
- @langchain/google-common@2.1.20

## Patch Changes
- Updated dependencies [[`7be50a7`](https://github.com/langchain-ai/langchainjs/commit/7be50a7014d7622e0ab8d303dfc9c633ebc96333)]:
- @langchain/google-common@2.1.19

## Patch Changes
- Updated dependencies [[`58c00aa`](https://github.com/langchain-ai/langchainjs/commit/58c00aa51994e421741c88f51f6e9d2726433a03)]:
- @langchain/google-common@2.1.18

## Patch Changes
- Updated dependencies [[`e2ed407`](https://github.com/langchain-ai/langchainjs/commit/e2ed40729c54d132b91b7abecfb787fe5f09461e)]:
- @langchain/google-common@2.1.17

## Patch Changes
- Updated dependencies [[`5681181`](https://github.com/langchain-ai/langchainjs/commit/568118119f44cc4509a2c04dff2891230e874f46)]:
- @langchain/google-common@2.1.16

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.15

## Patch Changes
- Updated dependencies [[`a9b5059`](https://github.com/langchain-ai/langchainjs/commit/a9b50597186002221aaa4585246e569fa44c27c8), [`a9b5059`](https://github.com/langchain-ai/langchainjs/commit/a9b50597186002221aaa4585246e569fa44c27c8), [`e10c6cb`](https://github.com/langchain-ai/langchainjs/commit/e10c6cb9cbbf420c95855225f4872c2e738bbd92)]:
- @langchain/google-common@2.1.14

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.13

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.12

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.11

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.10

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.9

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.8

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.7

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.6

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.5

## Patch Changes
- Updated dependencies [[`8ef1525`](https://github.com/langchain-ai/langchainjs/commit/8ef152555a945c95322f28209957b69605c04c91)]:
- @langchain/google-common@2.1.4

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.3

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.2

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.1.1

## Patch Changes
- Updated dependencies [[`cc7051b`](https://github.com/langchain-ai/langchainjs/commit/cc7051b61503cdae91a2b74b41889d8d0f26a6e9), [`a2a0088`](https://github.com/langchain-ai/langchainjs/commit/a2a00880b80119eb926de05e9c556a44fd56632e)]:
- @langchain/google-common@2.1.0

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.0.4

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.0.3

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.0.2

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@2.0.1

## Patch Changes
- [#9416](https://github.com/langchain-ai/langchainjs/pull/9416) [`0fe9beb`](https://github.com/langchain-ai/langchainjs/commit/0fe9bebee6710f719e47f913eec1ec4f638e4de4) Thanks [@hntrl](https://github.com/hntrl)! - fix 'moduleResultion: "node"' compatibility
- Updated dependencies [[`0fe9beb`](https://github.com/langchain-ai/langchainjs/commit/0fe9bebee6710f719e47f913eec1ec4f638e4de4), [`21a8374`](https://github.com/langchain-ai/langchainjs/commit/21a83742af89e6a7f29d303f63729d0e31b59fdd)]:
- @langchain/google-common@2.0.0

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@1.0.3

## Patch Changes
- Updated dependencies []:
- @langchain/google-common@1.0.2

## Patch Changes
- Updated dependencies [[`ac0d4fe`](https://github.com/langchain-ai/langchainjs/commit/ac0d4fe3807e05eb2185ae8a36da69498e6163d4)]:
- @langchain/google-common@1.0.1

## 1.0.0
This release updates the package for compatibility with LangChain v1.0. See the v1.0 [release notes](https://docs.langchain.com/oss/javascript/releases/langchain-v1) for details on what's new.

## Patch Changes
- @langchain/google-common@0.2.18

## Patch Changes
- Updated dependencies [4a3f5af]
- @langchain/google-common@0.2.17

---

# iCloud: web-app/node_modules/@langchain/google-gauth/README.md

> **Source:** icloud://web-app/node_modules/@langchain/google-gauth/README.md
> **Analyzed At:** 2026-06-13T06:32:46.657Z

## LangChain google-gauth
This package contains resources to access Google AI/ML models
and other Google services. Authorization to these services use
either an API Key or service account credentials that are either
stored on the local file system or are provided through the
Google Cloud Platform environment it is running on.
If you are running this on a platform where the credentials cannot
be provided this way, consider using the @langchain/google-webauth
package *instead*. You do not need to use both packages. See the
section on **Authorization** below.

## Installation
```bash
$ pnpm install @langchain/google-gauth
```

## Authorization
Authorization is either done through the use of an API Key, if it is
supported for the service you're using, or a Google Cloud Service
Account.
To handle service accounts, this package uses the `google-auth-library`
package, and you may wish to consult the documentation for that library
about how it does so. But in short, classes in this package will use
credentials from the first of the following that apply:
1. An API Key that is passed to the constructor using the `apiKey` attribute
2. Credentials that are passed to the constructor using the `authInfo` attribute
3. An API Key that is set in the environment variable `API_KEY`
4. The Service Account credentials that are saved in a file. The path to
this file is set in the `GOOGLE_APPLICATION_CREDENTIALS` environment
variable.
5. If you are running on a Google Cloud Platform resource, or if you have
logged in using `gcloud auth application-default login`, then the
default credentials.

---

# iCloud: web-app/node_modules/@langchain/google-gauth/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@langchain/google-gauth/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.661Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@langchain/google-gauth/node_modules/@langchain/google-common/README.md

> **Source:** icloud://web-app/node_modules/@langchain/google-gauth/node_modules/@langchain/google-common/README.md
> **Analyzed At:** 2026-06-13T06:32:46.670Z

## LangChain google-common
This package contains common resources to access Google AI/ML models
and other Google services in an auth-independent way.
AI/ML models are supported using the same interface no matter if
you are using the Google AI Studio-based version of the model or
the Google Cloud Vertex AI version of the model.

## Installation
This is **not** a stand-alone package since it does not contain code to do
authorization.
Instead, you should install _one_ of the following packages:
- @langchain/google-gauth
- @langchain/google-webauth
See those packages for details about installation.
This package does **not** depend on any Google library. Instead, it relies on
REST calls to Google endpoints. This is deliberate to reduce (sometimes
conflicting) dependencies and make it usable on platforms that do not include
file storage.

## Google services supported
- Gemini model through LLM and Chat classes (both through Google AI Studio and
Google Cloud Vertex AI). Including:
- Function/Tool support

## Tool/Function Schema Limitations
When using tools or functions with Gemini models, the following Zod schema features are not supported:
- **Discriminated Unions** (`z.discriminatedUnion()`) - Use flat objects with optional fields instead
- **Union Types** (`z.union()`) - Use separate optional fields
- **Positive Refinement** (`z.number().positive()`) - Automatically converted to `z.number().min(0.01)`
For detailed examples and workarounds, see the Tool Schema Limitations section in the @langchain/google-vertexai or @langchain/google-genai package documentation.

## TODO
Tasks and services still to be implemented:
- PaLM Vertex AI support and backwards compatibility
- PaLM MakerSuite support and backwards compatibility
- Semantic Retrieval / AQA model
- PaLM embeddings
- Gemini embeddings
- Multimodal embeddings
- Vertex AI Search
- Vertex AI Model Garden
- Online prediction endpoints
- Gemma
- Google managed models
- Claude
- AI Studio Tuned Models
- MakerSuite / Google Drive Hub
- Google Cloud Vector Store

---

# iCloud: web-app/node_modules/@jridgewell/trace-mapping/README.md

> **Source:** icloud://web-app/node_modules/@jridgewell/trace-mapping/README.md
> **Analyzed At:** 2026-06-13T06:32:46.678Z

## @jridgewell/trace-mapping
> Trace the original position through a source map
`trace-mapping` allows you to take the line and column of an output file and trace it to the
original location in the source file through a source map.
You may already be familiar with the [`source-map`][source-map] package's `SourceMapConsumer`. This
provides the same `originalPositionFor` and `generatedPositionFor` API, without requiring WASM.

## Installation
```sh
npm install @jridgewell/trace-mapping
```

## Usage
```typescript
import {
  TraceMap,
  originalPositionFor,
  generatedPositionFor,
  sourceContentFor,
  isIgnored,
} from '@jridgewell/trace-mapping';

const tracer = new TraceMap({
  version: 3,
  sources: ['input.js'],
  sourcesContent: ['content of input.js'],
  names: ['foo'],
  mappings: 'KAyCIA',
  ignoreList: [],
});

// Lines start at line 1, columns at column 0.
const traced = originalPositionFor(tracer, { line: 1, column: 5 });
assert.deepEqual(traced, {
  source: 'input.js',
  line: 42,
  column: 4,
  name: 'foo',
});

const content = sourceContentFor(tracer, traced.source);
assert.strictEqual(content, 'content for input.js');

const generated = generatedPositionFor(tracer, {
  source: 'input.js',
  line: 42,
  column: 4,
});
assert.deepEqual(generated, {
  line: 1,
  column: 5,
});

const ignored = isIgnored(tracer, 'input.js');
assert.equal(ignored, false);
```
We also provide a lower level API to get the actual segment that matches our line and column. Unlike
`originalPositionFor`, `traceSegment` uses a 0-base for `line`:
```typescript
import { traceSegment } from '@jridgewell/trace-mapping';

// line is 0-base.
const traced = traceSegment(tracer, /* line */ 0, /* column */ 5);

// Segments are [outputColumn, sourcesIndex, sourceLine, sourceColumn, namesIndex]
// Again, line is 0-base and so is sourceLine
assert.deepEqual(traced, [5, 0, 41, 4, 0]);
```

## SectionedSourceMaps
The sourcemap spec defines a special `sections` field that's designed to handle concatenation of
output code with associated sourcemaps. This type of sourcemap is rarely used (no major build tool
produces it), but if you are hand coding a concatenation you may need it. We provide an `AnyMap`
helper that can receive either a regular sourcemap or a `SectionedSourceMap` and returns a
`TraceMap` instance:
```typescript
import { AnyMap } from '@jridgewell/trace-mapping';
const fooOutput = 'foo';
const barOutput = 'bar';
const output = [fooOutput, barOutput].join('\n');

const sectioned = new AnyMap({
  version: 3,
  sections: [
    {
      // 0-base line and column
      offset: { line: 0, column: 0 },
      // fooOutput's sourcemap
      map: {
        version: 3,
        sources: ['foo.js'],
        names: ['foo'],
        mappings: 'AAAAA',
      },
    },
    {
      // barOutput's sourcemap will not affect the first line, only the second
      offset: { line: 1, column: 0 },
      map: {
        version: 3,
        sources: ['bar.js'],
        names: ['bar'],
        mappings: 'AAAAA',
      },
    },
  ],
});

const traced = originalPositionFor(sectioned, {
  line: 2,
  column: 0,
});

assert.deepEqual(traced, {
  source: 'bar.js',
  line: 1,
  column: 0,
  name: 'bar',
});
```

## Benchmarks
```
node v20.10.0

amp.js.map - 45120 segments

Memory Usage:
trace-mapping decoded         414164 bytes
trace-mapping encoded        6274352 bytes
source-map-js               10968904 bytes
source-map-0.6.1            17587160 bytes
source-map-0.8.0             8812155 bytes
Chrome dev tools             8672912 bytes
Smallest memory usage is trace-mapping decoded

Init speed:
trace-mapping:    decoded JSON input x 205 ops/sec ±0.19% (88 runs sampled)
trace-mapping:    encoded JSON input x 405 ops/sec ±1.47% (88 runs sampled)
trace-mapping:    decoded Object input x 4,645 ops/sec ±0.15% (98 runs sampled)
trace-mapping:    encoded Object input x 458 ops/sec ±1.63% (91 runs sampled)
source-map-js:    encoded Object input x 75.48 ops/sec ±1.64% (67 runs sampled)
source-map-0.6.1: encoded Object input x 39.37 ops/sec ±1.44% (53 runs sampled)
Chrome dev tools: encoded Object input x 150 ops/sec ±1.76% (79 runs sampled)
Fastest is trace-mapping:    decoded Object input

Trace speed (random):
trace-mapping:    decoded originalPositionFor x 44,946 ops/sec ±0.16% (99 runs sampled)
trace-mapping:    encoded originalPositionFor x 37,995 ops/sec ±1.81% (89 runs sampled)
source-map-js:    encoded originalPositionFor x 9,230 ops/sec ±1.36% (93 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 8,057 ops/sec ±0.84% (96 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 28,198 ops/sec ±1.12% (91 runs sampled)
Chrome dev tools: encoded originalPositionFor x 46,276 ops/sec ±1.35% (95 runs sampled)
Fastest is Chrome dev tools: encoded originalPositionFor

Trace speed (ascending):
trace-mapping:    decoded originalPositionFor x 204,406 ops/sec ±0.19% (97 runs sampled)
trace-mapping:    encoded originalPositionFor x 196,695 ops/sec ±0.24% (99 runs sampled)
source-map-js:    encoded originalPositionFor x 11,948 ops/sec ±0.94% (99 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 10,730 ops/sec ±0.36% (100 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 51,427 ops/sec ±0.21% (98 runs sampled)
Chrome dev tools: encoded originalPositionFor x 162,615 ops/sec ±0.18% (98 runs sampled)
Fastest is trace-mapping:    decoded originalPositionFor


***


babel.min.js.map - 347793 segments

Memory Usage:
trace-mapping decoded          18504 bytes
trace-mapping encoded       35428008 bytes
source-map-js               51676808 bytes
source-map-0.6.1            63367136 bytes
source-map-0.8.0            43158400 bytes
Chrome dev tools            50721552 bytes
Smallest memory usage is trace-mapping decoded

Init speed:
trace-mapping:    decoded JSON input x 17.82 ops/sec ±6.35% (35 runs sampled)
trace-mapping:    encoded JSON input x 31.57 ops/sec ±7.50% (43 runs sampled)
trace-mapping:    decoded Object input x 867 ops/sec ±0.74% (94 runs sampled)
trace-mapping:    encoded Object input x 33.83 ops/sec ±7.66% (46 runs sampled)
source-map-js:    encoded Object input x 6.58 ops/sec ±3.31% (20 runs sampled)
source-map-0.6.1: encoded Object input x 4.23 ops/sec ±3.43% (15 runs sampled)
Chrome dev tools: encoded Object input x 22.14 ops/sec ±3.79% (41 runs sampled)
Fastest is trace-mapping:    decoded Object input

Trace speed (random):
trace-mapping:    decoded originalPositionFor x 78,234 ops/sec ±1.48% (29 runs sampled)
trace-mapping:    encoded originalPositionFor x 60,761 ops/sec ±1.35% (21 runs sampled)
source-map-js:    encoded originalPositionFor x 51,448 ops/sec ±2.17% (89 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 47,221 ops/sec ±1.99% (15 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 84,002 ops/sec ±1.45% (27 runs sampled)
Chrome dev tools: encoded originalPositionFor x 106,457 ops/sec ±1.38% (37 runs sampled)
Fastest is Chrome dev tools: encoded originalPositionFor

Trace speed (ascending):
trace-mapping:    decoded originalPositionFor x 930,943 ops/sec ±0.25% (99 runs sampled)
trace-mapping:    encoded originalPositionFor x 843,545 ops/sec ±0.34% (97 runs sampled)
source-map-js:    encoded originalPositionFor x 114,510 ops/sec ±1.37% (36 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 87,412 ops/sec ±0.72% (92 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 197,709 ops/sec ±0.89% (59 runs sampled)
Chrome dev tools: encoded originalPositionFor x 688,983 ops/sec ±0.33% (98 runs sampled)
Fastest is trace-mapping:    decoded originalPositionFor


***


preact.js.map - 1992 segments

Memory Usage:
trace-mapping decoded          33136 bytes
trace-mapping encoded         254240 bytes
source-map-js                 837488 bytes
source-map-0.6.1              961928 bytes
source-map-0.8.0               54384 bytes
Chrome dev tools              709680 bytes
Smallest memory usage is trace-mapping decoded

Init speed:
trace-mapping:    decoded JSON input x 3,709 ops/sec ±0.13% (99 runs sampled)
trace-mapping:    encoded JSON input x 6,447 ops/sec ±0.22% (101 runs sampled)
trace-mapping:    decoded Object input x 83,062 ops/sec ±0.23% (100 runs sampled)
trace-mapping:    encoded Object input x 14,980 ops/sec ±0.28% (100 runs sampled)
source-map-js:    encoded Object input x 2,544 ops/sec ±0.16% (99 runs sampled)
source-map-0.6.1: encoded Object input x 1,221 ops/sec ±0.37% (97 runs sampled)
Chrome dev tools: encoded Object input x 4,241 ops/sec ±0.39% (93 runs sampled)
Fastest is trace-mapping:    decoded Object input

Trace speed (random):
trace-mapping:    decoded originalPositionFor x 91,028 ops/sec ±0.14% (94 runs sampled)
trace-mapping:    encoded originalPositionFor x 84,348 ops/sec ±0.26% (98 runs sampled)
source-map-js:    encoded originalPositionFor x 26,998 ops/sec ±0.23% (98 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 18,049 ops/sec ±0.26% (100 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 41,916 ops/sec ±0.28% (98 runs sampled)
Chrome dev tools: encoded originalPositionFor x 88,616 ops/sec ±0.14% (98 runs sampled)
Fastest is trace-mapping:    decoded originalPositionFor

Trace speed (ascending):
trace-mapping:    decoded originalPositionFor x 319,960 ops/sec ±0.16% (100 runs sampled)
trace-mapping:    encoded originalPositionFor x 302,153 ops/sec ±0.18% (100 runs sampled)
source-map-js:    encoded originalPositionFor x 35,574 ops/sec ±0.19% (100 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 19,943 ops/sec ±0.12% (101 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 54,648 ops/sec ±0.20% (99 runs sampled)
Chrome dev tools: encoded originalPositionFor x 278,319 ops/sec ±0.17% (102 runs sampled)
Fastest is trace-mapping:    decoded originalPositionFor


***


react.js.map - 5726 segments

Memory Usage:
trace-mapping decoded          10872 bytes
trace-mapping encoded         681512 bytes
source-map-js                2563944 bytes
source-map-0.6.1             2150864 bytes
source-map-0.8.0               88680 bytes
Chrome dev tools             1149576 bytes
Smallest memory usage is trace-mapping decoded

Init speed:
trace-mapping:    decoded JSON input x 1,887 ops/sec ±0.28% (99 runs sampled)
trace-mapping:    encoded JSON input x 4,749 ops/sec ±0.48% (97 runs sampled)
trace-mapping:    decoded Object input x 74,236 ops/sec ±0.11% (99 runs sampled)
trace-mapping:    encoded Object input x 5,752 ops/sec ±0.38% (100 runs sampled)
source-map-js:    encoded Object input x 806 ops/sec ±0.19% (97 runs sampled)
source-map-0.6.1: encoded Object input x 418 ops/sec ±0.33% (94 runs sampled)
Chrome dev tools: encoded Object input x 1,524 ops/sec ±0.57% (92 runs sampled)
Fastest is trace-mapping:    decoded Object input

Trace speed (random):
trace-mapping:    decoded originalPositionFor x 620,201 ops/sec ±0.33% (96 runs sampled)
trace-mapping:    encoded originalPositionFor x 579,548 ops/sec ±0.35% (97 runs sampled)
source-map-js:    encoded originalPositionFor x 230,983 ops/sec ±0.62% (54 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 158,145 ops/sec ±0.80% (46 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 343,801 ops/sec ±0.55% (96 runs sampled)
Chrome dev tools: encoded originalPositionFor x 659,649 ops/sec ±0.49% (98 runs sampled)
Fastest is Chrome dev tools: encoded originalPositionFor

Trace speed (ascending):
trace-mapping:    decoded originalPositionFor x 2,368,079 ops/sec ±0.32% (98 runs sampled)
trace-mapping:    encoded originalPositionFor x 2,134,039 ops/sec ±2.72% (87 runs sampled)
source-map-js:    encoded originalPositionFor x 290,120 ops/sec ±2.49% (82 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 187,613 ops/sec ±0.86% (49 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 479,569 ops/sec ±0.65% (96 runs sampled)
Chrome dev tools: encoded originalPositionFor x 2,048,414 ops/sec ±0.24% (98 runs sampled)
Fastest is trace-mapping:    decoded originalPositionFor


***


vscode.map - 2141001 segments

Memory Usage:
trace-mapping decoded        5206584 bytes
trace-mapping encoded      208370336 bytes
source-map-js              278493008 bytes
source-map-0.6.1           391564048 bytes
source-map-0.8.0           257508787 bytes
Chrome dev tools           291053000 bytes
Smallest memory usage is trace-mapping decoded

Init speed:
trace-mapping:    decoded JSON input x 1.63 ops/sec ±33.88% (9 runs sampled)
trace-mapping:    encoded JSON input x 3.29 ops/sec ±36.13% (13 runs sampled)
trace-mapping:    decoded Object input x 103 ops/sec ±0.93% (77 runs sampled)
trace-mapping:    encoded Object input x 5.42 ops/sec ±28.54% (19 runs sampled)
source-map-js:    encoded Object input x 1.07 ops/sec ±13.84% (7 runs sampled)
source-map-0.6.1: encoded Object input x 0.60 ops/sec ±2.43% (6 runs sampled)
Chrome dev tools: encoded Object input x 2.61 ops/sec ±22.00% (11 runs sampled)
Fastest is trace-mapping:    decoded Object input

Trace speed (random):
trace-mapping:    decoded originalPositionFor x 257,019 ops/sec ±0.97% (93 runs sampled)
trace-mapping:    encoded originalPositionFor x 179,163 ops/sec ±0.83% (92 runs sampled)
source-map-js:    encoded originalPositionFor x 73,337 ops/sec ±1.35% (87 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 38,797 ops/sec ±1.66% (88 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 107,758 ops/sec ±1.94% (45 runs sampled)
Chrome dev tools: encoded originalPositionFor x 188,550 ops/sec ±1.85% (79 runs sampled)
Fastest is trace-mapping:    decoded originalPositionFor

Trace speed (ascending):
trace-mapping:    decoded originalPositionFor x 447,621 ops/sec ±3.64% (94 runs sampled)
trace-mapping:    encoded originalPositionFor x 323,698 ops/sec ±5.20% (88 runs sampled)
source-map-js:    encoded originalPositionFor x 78,387 ops/sec ±1.69% (89 runs sampled)
source-map-0.6.1: encoded originalPositionFor x 41,016 ops/sec ±3.01% (25 runs sampled)
source-map-0.8.0: encoded originalPositionFor x 124,204 ops/sec ±0.90% (92 runs sampled)
Chrome dev tools: encoded originalPositionFor x 230,087 ops/sec ±2.61% (93 runs sampled)
Fastest is trace-mapping:    decoded originalPositionFor
```
[source-map]: https://www.npmjs.com/package/source-map

---

# iCloud: web-app/node_modules/@jridgewell/sourcemap-codec/README.md

> **Source:** icloud://web-app/node_modules/@jridgewell/sourcemap-codec/README.md
> **Analyzed At:** 2026-06-13T06:32:46.682Z

## @jridgewell/sourcemap-codec
Encode/decode the `mappings` property of a [sourcemap](https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRlpiOFze0b-_2gc6fAH0KY0k/edit).

## Why?
Sourcemaps are difficult to generate and manipulate, because the `mappings` property – the part that actually links the generated code back to the original source – is encoded using an obscure method called [Variable-length quantity](https://en.wikipedia.org/wiki/Variable-length_quantity). On top of that, each segment in the mapping contains offsets rather than absolute indices, which means that you can't look at a segment in isolation – you have to understand the whole sourcemap.
This package makes the process slightly easier.

## Installation
```bash
npm install @jridgewell/sourcemap-codec
```

## Usage
```js
import { encode, decode } from '@jridgewell/sourcemap-codec';

var decoded = decode( ';EAEEA,EAAE,EAAC,CAAE;ECQY,UACC' );

assert.deepEqual( decoded, [
	// the first line (of the generated code) has no mappings,
	// as shown by the starting semi-colon (which separates lines)
	[],

	// the second line contains four (comma-separated) segments
	[
		// segments are encoded as you'd expect:
		// [ generatedCodeColumn, sourceIndex, sourceCodeLine, sourceCodeColumn, nameIndex ]

		// i.e. the first segment begins at column 2, and maps back to the second column
		// of the second line (both zero-based) of the 0th source, and uses the 0th
		// name in the `map.names` array
		[ 2, 0, 2, 2, 0 ],

		// the remaining segments are 4-length rather than 5-length,
		// because they don't map a name
		[ 4, 0, 2, 4 ],
		[ 6, 0, 2, 5 ],
		[ 7, 0, 2, 7 ]
	],

	// the final line contains two segments
	[
		[ 2, 1, 10, 19 ],
		[ 12, 1, 11, 20 ]
	]
]);

var encoded = encode( decoded );
assert.equal( encoded, ';EAEEA,EAAE,EAAC,CAAE;ECQY,UACC' );
```

## Benchmarks
```
node v20.10.0

amp.js.map - 45120 segments

Decode Memory Usage:
local code                             5815135 bytes
@jridgewell/sourcemap-codec 1.4.15     5868160 bytes
sourcemap-codec                        5492584 bytes
source-map-0.6.1                      13569984 bytes
source-map-0.8.0                       6390584 bytes
chrome dev tools                       8011136 bytes
Smallest memory usage is sourcemap-codec

Decode speed:
decode: local code x 492 ops/sec ±1.22% (90 runs sampled)
decode: @jridgewell/sourcemap-codec 1.4.15 x 499 ops/sec ±1.16% (89 runs sampled)
decode: sourcemap-codec x 376 ops/sec ±1.66% (89 runs sampled)
decode: source-map-0.6.1 x 34.99 ops/sec ±0.94% (48 runs sampled)
decode: source-map-0.8.0 x 351 ops/sec ±0.07% (95 runs sampled)
chrome dev tools x 165 ops/sec ±0.91% (86 runs sampled)
Fastest is decode: @jridgewell/sourcemap-codec 1.4.15

Encode Memory Usage:
local code                              444248 bytes
@jridgewell/sourcemap-codec 1.4.15      623024 bytes
sourcemap-codec                        8696280 bytes
source-map-0.6.1                       8745176 bytes
source-map-0.8.0                       8736624 bytes
Smallest memory usage is local code

Encode speed:
encode: local code x 796 ops/sec ±0.11% (97 runs sampled)
encode: @jridgewell/sourcemap-codec 1.4.15 x 795 ops/sec ±0.25% (98 runs sampled)
encode: sourcemap-codec x 231 ops/sec ±0.83% (86 runs sampled)
encode: source-map-0.6.1 x 166 ops/sec ±0.57% (86 runs sampled)
encode: source-map-0.8.0 x 203 ops/sec ±0.45% (88 runs sampled)
Fastest is encode: local code,encode: @jridgewell/sourcemap-codec 1.4.15


***


babel.min.js.map - 347793 segments

Decode Memory Usage:
local code                            35424960 bytes
@jridgewell/sourcemap-codec 1.4.15    35424696 bytes
sourcemap-codec                       36033464 bytes
source-map-0.6.1                      62253704 bytes
source-map-0.8.0                      43843920 bytes
chrome dev tools                      45111400 bytes
Smallest memory usage is @jridgewell/sourcemap-codec 1.4.15

Decode speed:
decode: local code x 38.18 ops/sec ±5.44% (52 runs sampled)
decode: @jridgewell/sourcemap-codec 1.4.15 x 38.36 ops/sec ±5.02% (52 runs sampled)
decode: sourcemap-codec x 34.05 ops/sec ±4.45% (47 runs sampled)
decode: source-map-0.6.1 x 4.31 ops/sec ±2.76% (15 runs sampled)
decode: source-map-0.8.0 x 55.60 ops/sec ±0.13% (73 runs sampled)
chrome dev tools x 16.94 ops/sec ±3.78% (46 runs sampled)
Fastest is decode: source-map-0.8.0

Encode Memory Usage:
local code                             2606016 bytes
@jridgewell/sourcemap-codec 1.4.15     2626440 bytes
sourcemap-codec                       21152576 bytes
source-map-0.6.1                      25023928 bytes
source-map-0.8.0                      25256448 bytes
Smallest memory usage is local code

Encode speed:
encode: local code x 127 ops/sec ±0.18% (83 runs sampled)
encode: @jridgewell/sourcemap-codec 1.4.15 x 128 ops/sec ±0.26% (83 runs sampled)
encode: sourcemap-codec x 29.31 ops/sec ±2.55% (53 runs sampled)
encode: source-map-0.6.1 x 18.85 ops/sec ±3.19% (36 runs sampled)
encode: source-map-0.8.0 x 19.34 ops/sec ±1.97% (36 runs sampled)
Fastest is encode: @jridgewell/sourcemap-codec 1.4.15


***


preact.js.map - 1992 segments

Decode Memory Usage:
local code                              261696 bytes
@jridgewell/sourcemap-codec 1.4.15      244296 bytes
sourcemap-codec                         302816 bytes
source-map-0.6.1                        939176 bytes
source-map-0.8.0                           336 bytes
chrome dev tools                        587368 bytes
Smallest memory usage is source-map-0.8.0

Decode speed:
decode: local code x 17,782 ops/sec ±0.32% (97 runs sampled)
decode: @jridgewell/sourcemap-codec 1.4.15 x 17,863 ops/sec ±0.40% (100 runs sampled)
decode: sourcemap-codec x 12,453 ops/sec ±0.27% (101 runs sampled)
decode: source-map-0.6.1 x 1,288 ops/sec ±1.05% (96 runs sampled)
decode: source-map-0.8.0 x 9,289 ops/sec ±0.27% (101 runs sampled)
chrome dev tools x 4,769 ops/sec ±0.18% (100 runs sampled)
Fastest is decode: @jridgewell/sourcemap-codec 1.4.15

Encode Memory Usage:
local code                              262944 bytes
@jridgewell/sourcemap-codec 1.4.15       25544 bytes
sourcemap-codec                         323048 bytes
source-map-0.6.1                        507808 bytes
source-map-0.8.0                        507480 bytes
Smallest memory usage is @jridgewell/sourcemap-codec 1.4.15

Encode speed:
encode: local code x 24,207 ops/sec ±0.79% (95 runs sampled)
encode: @jridgewell/sourcemap-codec 1.4.15 x 24,288 ops/sec ±0.48% (96 runs sampled)
encode: sourcemap-codec x 6,761 ops/sec ±0.21% (100 runs sampled)
encode: source-map-0.6.1 x 5,374 ops/sec ±0.17% (99 runs sampled)
encode: source-map-0.8.0 x 5,633 ops/sec ±0.32% (99 runs sampled)
Fastest is encode: @jridgewell/sourcemap-codec 1.4.15,encode: local code


***


react.js.map - 5726 segments

Decode Memory Usage:
local code                              678816 bytes
@jridgewell/sourcemap-codec 1.4.15      678816 bytes
sourcemap-codec                         816400 bytes
source-map-0.6.1                       2288864 bytes
source-map-0.8.0                        721360 bytes
chrome dev tools                       1012512 bytes
Smallest memory usage is local code

Decode speed:
decode: local code x 6,178 ops/sec ±0.19% (98 runs sampled)
decode: @jridgewell/sourcemap-codec 1.4.15 x 6,261 ops/sec ±0.22% (100 runs sampled)
decode: sourcemap-codec x 4,472 ops/sec ±0.90% (99 runs sampled)
decode: source-map-0.6.1 x 449 ops/sec ±0.31% (95 runs sampled)
decode: source-map-0.8.0 x 3,219 ops/sec ±0.13% (100 runs sampled)
chrome dev tools x 1,743 ops/sec ±0.20% (99 runs sampled)
Fastest is decode: @jridgewell/sourcemap-codec 1.4.15

Encode Memory Usage:
local code                              140960 bytes
@jridgewell/sourcemap-codec 1.4.15      159808 bytes
sourcemap-codec                         969304 bytes
source-map-0.6.1                        930520 bytes
source-map-0.8.0                        930248 bytes
Smallest memory usage is local code

Encode speed:
encode: local code x 8,013 ops/sec ±0.19% (100 runs sampled)
encode: @jridgewell/sourcemap-codec 1.4.15 x 7,989 ops/sec ±0.20% (101 runs sampled)
encode: sourcemap-codec x 2,472 ops/sec ±0.21% (99 runs sampled)
encode: source-map-0.6.1 x 2,200 ops/sec ±0.17% (99 runs sampled)
encode: source-map-0.8.0 x 2,220 ops/sec ±0.37% (99 runs sampled)
Fastest is encode: local code


***


vscode.map - 2141001 segments

Decode Memory Usage:
local code                           198955264 bytes
@jridgewell/sourcemap-codec 1.4.15   199175352 bytes
sourcemap-codec                      199102688 bytes
source-map-0.6.1                     386323432 bytes
source-map-0.8.0                     244116432 bytes
chrome dev tools                     293734280 bytes
Smallest memory usage is local code

Decode speed:
decode: local code x 3.90 ops/sec ±22.21% (15 runs sampled)
decode: @jridgewell/sourcemap-codec 1.4.15 x 3.95 ops/sec ±23.53% (15 runs sampled)
decode: sourcemap-codec x 3.82 ops/sec ±17.94% (14 runs sampled)
decode: source-map-0.6.1 x 0.61 ops/sec ±7.81% (6 runs sampled)
decode: source-map-0.8.0 x 9.54 ops/sec ±0.28% (28 runs sampled)
chrome dev tools x 2.18 ops/sec ±10.58% (10 runs sampled)
Fastest is decode: source-map-0.8.0

Encode Memory Usage:
local code                            13509880 bytes
@jridgewell/sourcemap-codec 1.4.15    13537648 bytes
sourcemap-codec                       32540104 bytes
source-map-0.6.1                     127531040 bytes
source-map-0.8.0                     127535312 bytes
Smallest memory usage is local code

Encode speed:
encode: local code x 20.10 ops/sec ±0.19% (38 runs sampled)
encode: @jridgewell/sourcemap-codec 1.4.15 x 20.26 ops/sec ±0.32% (38 runs sampled)
encode: sourcemap-codec x 5.44 ops/sec ±1.64% (18 runs sampled)
encode: source-map-0.6.1 x 2.30 ops/sec ±4.79% (10 runs sampled)
encode: source-map-0.8.0 x 2.46 ops/sec ±6.53% (10 runs sampled)
Fastest is encode: @jridgewell/sourcemap-codec 1.4.15
```

---

# iCloud: web-app/node_modules/@jridgewell/resolve-uri/README.md

> **Source:** icloud://web-app/node_modules/@jridgewell/resolve-uri/README.md
> **Analyzed At:** 2026-06-13T06:32:46.686Z

## @jridgewell/resolve-uri
> Resolve a URI relative to an optional base URI
Resolve any combination of absolute URIs, protocol-realtive URIs, absolute paths, or relative paths.

## Installation
```sh
npm install @jridgewell/resolve-uri
```

## Usage
```typescript
function resolve(input: string, base?: string): string;
```
```js
import resolve from '@jridgewell/resolve-uri';

resolve('foo', 'https://example.com'); // => 'https://example.com/foo'
```
| Input                 | Base                    | Resolution                     | Explanation                                                  |
|-----------------------|-------------------------|--------------------------------|--------------------------------------------------------------|
| `https://example.com` | _any_                   | `https://example.com/`         | Input is normalized only                                     |
| `//example.com`       | `https://base.com/`     | `https://example.com/`         | Input inherits the base's protocol                           |
| `//example.com`       | _rest_                  | `//example.com/`               | Input is normalized only                                     |
| `/example`            | `https://base.com/`     | `https://base.com/example`     | Input inherits the base's origin                             |
| `/example`            | `//base.com/`           | `//base.com/example`           | Input inherits the base's host and remains protocol relative |
| `/example`            | _rest_                  | `/example`                     | Input is normalized only                                     |
| `example`             | `https://base.com/dir/` | `https://base.com/dir/example` | Input is joined with the base                                |
| `example`             | `https://base.com/file` | `https://base.com/example`     | Input is joined with the base without its file               |
| `example`             | `//base.com/dir/`       | `//base.com/dir/example`       | Input is joined with the base's last directory               |
| `example`             | `//base.com/file`       | `//base.com/example`           | Input is joined with the base without its file               |
| `example`             | `/base/dir/`            | `/base/dir/example`            | Input is joined with the base's last directory               |
| `example`             | `/base/file`            | `/base/example`                | Input is joined with the base without its file               |
| `example`             | `base/dir/`             | `base/dir/example`             | Input is joined with the base's last directory               |
| `example`             | `base/file`             | `base/example`                 | Input is joined with the base without its file               |

---

# iCloud: web-app/node_modules/@jridgewell/remapping/README.md

> **Source:** icloud://web-app/node_modules/@jridgewell/remapping/README.md
> **Analyzed At:** 2026-06-13T06:32:46.690Z

## @jridgewell/remapping
> Remap sequential sourcemaps through transformations to point at the original source code
Remapping allows you to take the sourcemaps generated through transforming your code and "remap"
them to the original source locations. Think "my minified code, transformed with babel and bundled
with webpack", all pointing to the correct location in your original source code.
With remapping, none of your source code transformations need to be aware of the input's sourcemap,
they only need to generate an output sourcemap. This greatly simplifies building custom
transformations (think a find-and-replace).

## Installation
```sh
npm install @jridgewell/remapping
```

## Usage
```typescript
function remapping(
  map: SourceMap | SourceMap[],
  loader: (file: string, ctx: LoaderContext) => (SourceMap | null | undefined),
  options?: { excludeContent: boolean, decodedMappings: boolean }
): SourceMap;

// LoaderContext gives the loader the importing sourcemap, tree depth, the ability to override the
// "source" location (where child sources are resolved relative to, or the location of original
// source), and the ability to override the "content" of an original source for inclusion in the
// output sourcemap.
type LoaderContext = {
 readonly importer: string;
 readonly depth: number;
 source: string;
 content: string | null | undefined;
}
```
`remapping` takes the final output sourcemap, and a `loader` function. For every source file pointer
in the sourcemap, the `loader` will be called with the resolved path. If the path itself represents
a transformed file (it has a sourcmap associated with it), then the `loader` should return that
sourcemap. If not, the path will be treated as an original, untransformed source code.
```js
// Babel transformed "helloworld.js" into "transformed.js"
const transformedMap = JSON.stringify({
  file: 'transformed.js',
  // 1st column of 2nd line of output file translates into the 1st source
  // file, line 3, column 2
  mappings: ';CAEE',
  sources: ['helloworld.js'],
  version: 3,
});

// Uglify minified "transformed.js" into "transformed.min.js"
const minifiedTransformedMap = JSON.stringify({
  file: 'transformed.min.js',
  // 0th column of 1st line of output file translates into the 1st source
  // file, line 2, column 1.
  mappings: 'AACC',
  names: [],
  sources: ['transformed.js'],
  version: 3,
});

const remapped = remapping(
  minifiedTransformedMap,
  (file, ctx) => {

    // The "transformed.js" file is an transformed file.
    if (file === 'transformed.js') {
      // The root importer is empty.
      console.assert(ctx.importer === '');
      // The depth in the sourcemap tree we're currently loading.
      // The root `minifiedTransformedMap` is depth 0, and its source children are depth 1, etc.
      console.assert(ctx.depth === 1);

      return transformedMap;
    }

    // Loader will be called to load transformedMap's source file pointers as well.
    console.assert(file === 'helloworld.js');
    // `transformed.js`'s sourcemap points into `helloworld.js`.
    console.assert(ctx.importer === 'transformed.js');
    // This is a source child of `transformed`, which is a source child of `minifiedTransformedMap`.
    console.assert(ctx.depth === 2);
    return null;
  }
);

console.log(remapped);
// {
//   file: 'transpiled.min.js',
//   mappings: 'AAEE',
//   sources: ['helloworld.js'],
//   version: 3,
// };
```
In this example, `loader` will be called twice:
1. `"transformed.js"`, the first source file pointer in the `minifiedTransformedMap`. We return the
associated sourcemap for it (its a transformed file, after all) so that sourcemap locations can
be traced through it into the source files it represents.
2. `"helloworld.js"`, our original, unmodified source code. This file does not have a sourcemap, so
we return `null`.
The `remapped` sourcemap now points from `transformed.min.js` into locations in `helloworld.js`. If
you were to read the `mappings`, it says "0th column of the first line output line points to the 1st
column of the 2nd line of the file `helloworld.js`".

## Multiple transformations of a file
As a convenience, if you have multiple single-source transformations of a file, you may pass an
array of sourcemap files in the order of most-recent transformation sourcemap first. Note that this
changes the `importer` and `depth` of each call to our loader. So our above example could have been
written as:
```js
const remapped = remapping(
  [minifiedTransformedMap, transformedMap],
  () => null
);

console.log(remapped);
// {
//   file: 'transpiled.min.js',
//   mappings: 'AAEE',
//   sources: ['helloworld.js'],
//   version: 3,
// };
```

## `source`
The `source` property can overridden to any value to change the location of the current load. Eg,
for an original source file, it allows us to change the location to the original source regardless
of what the sourcemap source entry says. And for transformed files, it allows us to change the
relative resolving location for child sources of the loaded sourcemap.
```js
const remapped = remapping(
  minifiedTransformedMap,
  (file, ctx) => {

    if (file === 'transformed.js') {
      // We pretend the transformed.js file actually exists in the 'src/' directory. When the nested
      // source files are loaded, they will now be relative to `src/`.
      ctx.source = 'src/transformed.js';
      return transformedMap;
    }

    console.assert(file === 'src/helloworld.js');
    // We could futher change the source of this original file, eg, to be inside a nested directory
    // itself. This will be reflected in the remapped sourcemap.
    ctx.source = 'src/nested/transformed.js';
    return null;
  }
);

console.log(remapped);
// {
//   …,
//   sources: ['src/nested/helloworld.js'],
// };
```

## `content`
The `content` property can be overridden when we encounter an original source file. Eg, this allows
you to manually provide the source content of the original file regardless of whether the
`sourcesContent` field is present in the parent sourcemap. It can also be set to `null` to remove
the source content.
```js
const remapped = remapping(
  minifiedTransformedMap,
  (file, ctx) => {

    if (file === 'transformed.js') {
      // transformedMap does not include a `sourcesContent` field, so usually the remapped sourcemap
      // would not include any `sourcesContent` values.
      return transformedMap;
    }

    console.assert(file === 'helloworld.js');
    // We can read the file to provide the source content.
    ctx.content = fs.readFileSync(file, 'utf8');
    return null;
  }
);

console.log(remapped);
// {
//   …,
//   sourcesContent: [
//     'console.log("Hello world!")',
//   ],
// };
```

## excludeContent
`sourcesContent` field from the returned sourcemap. This is mainly useful when you want to reduce
the size out the sourcemap.

## decodedMappings
`mappings` field in a [decoded state](https://github.com/rich-harris/sourcemap-codec) instead of
encoding into a VLQ string.

---

# iCloud: web-app/node_modules/@jridgewell/gen-mapping/README.md

> **Source:** icloud://web-app/node_modules/@jridgewell/gen-mapping/README.md
> **Analyzed At:** 2026-06-13T06:32:46.695Z

## @jridgewell/gen-mapping
> Generate source maps
`gen-mapping` allows you to generate a source map during transpilation or minification.
With a source map, you're able to trace the original location in the source file, either in Chrome's
DevTools or using a library like [`@jridgewell/trace-mapping`][trace-mapping].
You may already be familiar with the [`source-map`][source-map] package's `SourceMapGenerator`. This
provides the same `addMapping` and `setSourceContent` API.

## Installation
```sh
npm install @jridgewell/gen-mapping
```

## Usage
```typescript
import { GenMapping, addMapping, setSourceContent, toEncodedMap, toDecodedMap } from '@jridgewell/gen-mapping';

const map = new GenMapping({
  file: 'output.js',
  sourceRoot: 'https://example.com/',
});

setSourceContent(map, 'input.js', `function foo() {}`);

addMapping(map, {
  // Lines start at line 1, columns at column 0.
  generated: { line: 1, column: 0 },
  source: 'input.js',
  original: { line: 1, column: 0 },
});

addMapping(map, {
  generated: { line: 1, column: 9 },
  source: 'input.js',
  original: { line: 1, column: 9 },
  name: 'foo',
});

assert.deepEqual(toDecodedMap(map), {
  version: 3,
  file: 'output.js',
  names: ['foo'],
  sourceRoot: 'https://example.com/',
  sources: ['input.js'],
  sourcesContent: ['function foo() {}'],
  mappings: [
    [ [0, 0, 0, 0], [9, 0, 0, 9, 0] ]
  ],
});

assert.deepEqual(toEncodedMap(map), {
  version: 3,
  file: 'output.js',
  names: ['foo'],
  sourceRoot: 'https://example.com/',
  sources: ['input.js'],
  sourcesContent: ['function foo() {}'],
  mappings: 'AAAA,SAASA',
});
```

## Smaller Sourcemaps
Not everything needs to be added to a sourcemap, and needless markings can cause signficantly
larger file sizes. `gen-mapping` exposes `maybeAddSegment`/`maybeAddMapping` APIs that will
intelligently determine if this marking adds useful information. If not, the marking will be
skipped.
```typescript
import { maybeAddMapping } from '@jridgewell/gen-mapping';

const map = new GenMapping();

// Adding a sourceless marking at the beginning of a line isn't useful.
maybeAddMapping(map, {
  generated: { line: 1, column: 0 },
});

// Adding a new source marking is useful.
maybeAddMapping(map, {
  generated: { line: 1, column: 0 },
  source: 'input.js',
  original: { line: 1, column: 0 },
});

// But adding another marking pointing to the exact same original location isn't, even if the
// generated column changed.
maybeAddMapping(map, {
  generated: { line: 1, column: 9 },
  source: 'input.js',
  original: { line: 1, column: 0 },
});

assert.deepEqual(toEncodedMap(map), {
  version: 3,
  names: [],
  sources: ['input.js'],
  sourcesContent: [null],
  mappings: 'AAAA',
});
```

## Benchmarks
```
node v18.0.0

amp.js.map
Memory Usage:
gen-mapping: addSegment      5852872 bytes
gen-mapping: addMapping      7716042 bytes
source-map-js                6143250 bytes
source-map-0.6.1             6124102 bytes
source-map-0.8.0             6121173 bytes
Smallest memory usage is gen-mapping: addSegment

Adding speed:
gen-mapping:      addSegment x 441 ops/sec ±2.07% (90 runs sampled)
gen-mapping:      addMapping x 350 ops/sec ±2.40% (86 runs sampled)
source-map-js:    addMapping x 169 ops/sec ±2.42% (80 runs sampled)
source-map-0.6.1: addMapping x 167 ops/sec ±2.56% (80 runs sampled)
source-map-0.8.0: addMapping x 168 ops/sec ±2.52% (80 runs sampled)
Fastest is gen-mapping:      addSegment

Generate speed:
gen-mapping:      decoded output x 150,824,370 ops/sec ±0.07% (102 runs sampled)
gen-mapping:      encoded output x 663 ops/sec ±0.22% (98 runs sampled)
source-map-js:    encoded output x 197 ops/sec ±0.45% (84 runs sampled)
source-map-0.6.1: encoded output x 198 ops/sec ±0.33% (85 runs sampled)
source-map-0.8.0: encoded output x 197 ops/sec ±0.06% (93 runs sampled)
Fastest is gen-mapping:      decoded output


***


babel.min.js.map
Memory Usage:
gen-mapping: addSegment     37578063 bytes
gen-mapping: addMapping     37212897 bytes
source-map-js               47638527 bytes
source-map-0.6.1            47690503 bytes
source-map-0.8.0            47470188 bytes
Smallest memory usage is gen-mapping: addMapping

Adding speed:
gen-mapping:      addSegment x 31.05 ops/sec ±8.31% (43 runs sampled)
gen-mapping:      addMapping x 29.83 ops/sec ±7.36% (51 runs sampled)
source-map-js:    addMapping x 20.73 ops/sec ±6.22% (38 runs sampled)
source-map-0.6.1: addMapping x 20.03 ops/sec ±10.51% (38 runs sampled)
source-map-0.8.0: addMapping x 19.30 ops/sec ±8.27% (37 runs sampled)
Fastest is gen-mapping:      addSegment

Generate speed:
gen-mapping:      decoded output x 381,379,234 ops/sec ±0.29% (96 runs sampled)
gen-mapping:      encoded output x 95.15 ops/sec ±2.98% (72 runs sampled)
source-map-js:    encoded output x 15.20 ops/sec ±7.41% (33 runs sampled)
source-map-0.6.1: encoded output x 16.36 ops/sec ±10.46% (31 runs sampled)
source-map-0.8.0: encoded output x 16.06 ops/sec ±6.45% (31 runs sampled)
Fastest is gen-mapping:      decoded output


***


preact.js.map
Memory Usage:
gen-mapping: addSegment       416247 bytes
gen-mapping: addMapping       419824 bytes
source-map-js                1024619 bytes
source-map-0.6.1             1146004 bytes
source-map-0.8.0             1113250 bytes
Smallest memory usage is gen-mapping: addSegment

Adding speed:
gen-mapping:      addSegment x 13,755 ops/sec ±0.15% (98 runs sampled)
gen-mapping:      addMapping x 13,013 ops/sec ±0.11% (101 runs sampled)
source-map-js:    addMapping x 4,564 ops/sec ±0.21% (98 runs sampled)
source-map-0.6.1: addMapping x 4,562 ops/sec ±0.11% (99 runs sampled)
source-map-0.8.0: addMapping x 4,593 ops/sec ±0.11% (100 runs sampled)
Fastest is gen-mapping:      addSegment

Generate speed:
gen-mapping:      decoded output x 379,864,020 ops/sec ±0.23% (93 runs sampled)
gen-mapping:      encoded output x 14,368 ops/sec ±4.07% (82 runs sampled)
source-map-js:    encoded output x 5,261 ops/sec ±0.21% (99 runs sampled)
source-map-0.6.1: encoded output x 5,124 ops/sec ±0.58% (99 runs sampled)
source-map-0.8.0: encoded output x 5,434 ops/sec ±0.33% (96 runs sampled)
Fastest is gen-mapping:      decoded output


***


react.js.map
Memory Usage:
gen-mapping: addSegment       975096 bytes
gen-mapping: addMapping      1102981 bytes
source-map-js                2918836 bytes
source-map-0.6.1             2885435 bytes
source-map-0.8.0             2874336 bytes
Smallest memory usage is gen-mapping: addSegment

Adding speed:
gen-mapping:      addSegment x 4,772 ops/sec ±0.15% (100 runs sampled)
gen-mapping:      addMapping x 4,456 ops/sec ±0.13% (97 runs sampled)
source-map-js:    addMapping x 1,618 ops/sec ±0.24% (97 runs sampled)
source-map-0.6.1: addMapping x 1,622 ops/sec ±0.12% (99 runs sampled)
source-map-0.8.0: addMapping x 1,631 ops/sec ±0.12% (100 runs sampled)
Fastest is gen-mapping:      addSegment

Generate speed:
gen-mapping:      decoded output x 379,107,695 ops/sec ±0.07% (99 runs sampled)
gen-mapping:      encoded output x 5,421 ops/sec ±1.60% (89 runs sampled)
source-map-js:    encoded output x 2,113 ops/sec ±1.81% (98 runs sampled)
source-map-0.6.1: encoded output x 2,126 ops/sec ±0.10% (100 runs sampled)
source-map-0.8.0: encoded output x 2,176 ops/sec ±0.39% (98 runs sampled)
Fastest is gen-mapping:      decoded output
```
[source-map]: https://www.npmjs.com/package/source-map
[trace-mapping]: https://github.com/jridgewell/sourcemaps/tree/main/packages/trace-mapping

---

# iCloud: web-app/node_modules/@isaacs/cliui/README.md

> **Source:** icloud://web-app/node_modules/@isaacs/cliui/README.md
> **Analyzed At:** 2026-06-13T06:32:46.700Z

## @isaacs/cliui
Temporary fork of [cliui](http://npm.im/cliui).
![ci](https://github.com/yargs/cliui/workflows/ci/badge.svg)
[![NPM version](https://img.shields.io/npm/v/cliui.svg)](https://www.npmjs.com/package/cliui)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
![nycrc config on GitHub](https://img.shields.io/nycrc/yargs/cliui)
easily create complex multi-column command-line-interfaces.

## Example
```js
const ui = require('cliui')()

ui.div('Usage: $0 [command] [options]')

ui.div({
  text: 'Options:',
  padding: [2, 0, 1, 0]
})

ui.div(
  {
    text: "-f, --file",
    width: 20,
    padding: [0, 4, 0, 4]
  },
  {
    text: "the file to load." +
      chalk.green("(if this description is long it wraps).")
    ,
    width: 20
  },
  {
    text: chalk.red("[required]"),
    align: 'right'
  }
)

console.log(ui.toString())
```

## Deno/ESM Support
As of `v7` `cliui` supports [Deno](https://github.com/denoland/deno) and
[ESM](https://nodejs.org/api/esm.html#esm_ecmascript_modules):
```typescript
import cliui from "https://deno.land/x/cliui/deno.ts";

const ui = cliui({})

ui.div('Usage: $0 [command] [options]')

ui.div({
  text: 'Options:',
  padding: [2, 0, 1, 0]
})

ui.div({
  text: "-f, --file",
  width: 20,
  padding: [0, 4, 0, 4]
})

console.log(ui.toString())
```

## Layout DSL
cliui exposes a simple layout DSL:
If you create a single `ui.div`, passing a string rather than an
object:
* `\n`: characters will be interpreted as new rows.
* `\t`: characters will be interpreted as new columns.
* `\s`: characters will be interpreted as padding.
**as an example...**
```js
var ui = require('./')({
  width: 60
})

ui.div(
  'Usage: node ./bin/foo.js\n' +
  '  <regex>\t  provide a regex\n' +
  '  <glob>\t  provide a glob\t [required]'
)

console.log(ui.toString())
```
**will output:**
```shell
Usage: node ./bin/foo.js
  <regex>  provide a regex
  <glob>   provide a glob          [required]
```

## Methods
```js
cliui = require('cliui')
```

## cliui({width: integer})
Specify the maximum width of the UI being generated.
If no width is provided, cliui will try to get the current window's width and use it, and if that doesn't work, width will be set to `80`.

## cliui({wrap: boolean})
Enable or disable the wrapping of text in a column.

## cliui.div(column, column, column)
Create a row with any number of columns, a column
can either be a string, or an object with the following
options:
* **text:** some text to place in the column.
* **width:** the width of a column.
* **align:** alignment, `right` or `center`.
* **padding:** `[top, right, bottom, left]`.
* **border:** should a border be placed around the div?

## cliui.span(column, column, column)
Similar to `div`, except the next row will be appended without
a new line being created.

## cliui.resetOutput()
Resets the UI elements of the current cliui instance, maintaining the values
set for `width` and `wrap`.

---

# iCloud: web-app/node_modules/@img/sharp-darwin-arm64/README.md

> **Source:** icloud://web-app/node_modules/@img/sharp-darwin-arm64/README.md
> **Analyzed At:** 2026-06-13T06:32:46.704Z

## `@img/sharp-darwin-arm64`
Prebuilt sharp for use with macOS 64-bit ARM.

## Licensing
Copyright 2013 Lovell Fuller and others.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
[https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---

# iCloud: web-app/node_modules/@img/sharp-darwin-arm64/node_modules/@img/sharp-libvips-darwin-arm64/README.md

> **Source:** icloud://web-app/node_modules/@img/sharp-darwin-arm64/node_modules/@img/sharp-libvips-darwin-arm64/README.md
> **Analyzed At:** 2026-06-13T06:32:46.708Z

## `@img/sharp-libvips-darwin-arm64`
Prebuilt libvips and dependencies for use with sharp on macOS 64-bit ARM.

## Licensing
This software contains third-party libraries
used under the terms of the following licences:
| Library       | Used under the terms of                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------|
| aom           | BSD 2-Clause + [Alliance for Open Media Patent License 1.0](https://aomedia.org/license/patent-license/)  |
| cairo         | Mozilla Public License 2.0                                                                                |
| cgif          | MIT Licence                                                                                               |
| expat         | MIT Licence                                                                                               |
| fontconfig    | [fontconfig Licence](https://gitlab.freedesktop.org/fontconfig/fontconfig/blob/main/COPYING) (BSD-like)   |
| freetype      | [freetype Licence](https://git.savannah.gnu.org/cgit/freetype/freetype2.git/tree/docs/FTL.TXT) (BSD-like) |
| fribidi       | LGPLv3                                                                                                    |
| glib          | LGPLv3                                                                                                    |
| harfbuzz      | MIT Licence                                                                                               |
| highway       | Apache-2.0 License, BSD 3-Clause                                                                          |
| lcms          | MIT Licence                                                                                               |
| libarchive    | BSD 2-Clause                                                                                              |
| libexif       | LGPLv3                                                                                                    |
| libffi        | MIT Licence                                                                                               |
| libheif       | LGPLv3                                                                                                    |
| libimagequant | [BSD 2-Clause](https://github.com/lovell/libimagequant/blob/main/COPYRIGHT)                               |
| libnsgif      | MIT Licence                                                                                               |
| libpng        | [libpng License](https://github.com/pnggroup/libpng/blob/master/LICENSE)                                  |
| librsvg       | LGPLv3                                                                                                    |
| libspng       | [BSD 2-Clause, libpng License](https://github.com/randy408/libspng/blob/master/LICENSE)                   |
| libtiff       | [libtiff License](https://gitlab.com/libtiff/libtiff/blob/master/LICENSE.md) (BSD-like)                   |
| libvips       | LGPLv3                                                                                                    |
| libwebp       | New BSD License                                                                                           |
| libxml2       | MIT Licence                                                                                               |
| mozjpeg       | [zlib License, IJG License, BSD-3-Clause](https://github.com/mozilla/mozjpeg/blob/master/LICENSE.md)      |
| pango         | LGPLv3                                                                                                    |
| pixman        | MIT Licence                                                                                               |
| proxy-libintl | LGPLv3                                                                                                    |
| zlib-ng       | [zlib Licence](https://github.com/zlib-ng/zlib-ng/blob/develop/LICENSE.md)                                |
Use of libraries under the terms of the LGPLv3 is via the
"any later version" clause of the LGPLv2 or LGPLv2.1.
Please report any errors or omissions via
https://github.com/lovell/sharp-libvips/issues/new

---

# iCloud: web-app/node_modules/@img/colour/LICENSE.md

> **Source:** icloud://web-app/node_modules/@img/colour/LICENSE.md
> **Analyzed At:** 2026-06-13T06:32:46.711Z

## color
Copyright (c) 2012 Heather Arthur
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## color-convert
Copyright (c) 2011-2016 Heather Arthur .
Copyright (c) 2016-2021 Josh Junon .
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## color-string
Copyright (c) 2011 Heather Arthur 
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## color-name
The MIT License (MIT)
Copyright (c) 2015 Dmitry Ivanov
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

# iCloud: web-app/node_modules/@img/colour/README.md

> **Source:** icloud://web-app/node_modules/@img/colour/README.md
> **Analyzed At:** 2026-06-13T06:32:46.715Z

## `@img/colour`
The latest version of the
[color](https://www.npmjs.com/package/color)
package is now ESM-only,
however some JavaScript runtimes do not yet support this,
which includes versions of Node.js prior to 20.19.0.
This package converts the `color` package and its dependencies,
all of which are MIT-licensed, to CommonJS.
- [color](https://www.npmjs.com/package/color)
- [color-convert](https://www.npmjs.com/package/color-convert)
- [color-string](https://www.npmjs.com/package/color-string)
- [color-name](https://www.npmjs.com/package/color-name)

---

# iCloud: web-app/node_modules/@humanwhocodes/retry/README.md

> **Source:** icloud://web-app/node_modules/@humanwhocodes/retry/README.md
> **Analyzed At:** 2026-06-13T06:32:46.718Z

## Retry utility
by [Nicholas C. Zakas](https://humanwhocodes.com)
If you find this useful, please consider supporting my work with a [donation](https://humanwhocodes.com/donate) or [nominate me](https://stars.github.com/nominate/) for a GitHub Star.

## Description
A utility for retrying failed async JavaScript calls based on the error returned.

## Node.js
Install using [npm][npm] or [yarn][yarn]:
```
npm install @humanwhocodes/retry

# or

yarn add @humanwhocodes/retry
```
Import into your Node.js project:
```js
// CommonJS
const { Retrier } = require("@humanwhocodes/retry");

// ESM
import { Retrier } from "@humanwhocodes/retry";
```

## Deno
Install using [JSR](https://jsr.io):
```shell
deno add @humanwhocodes/retry

#or

jsr add @humanwhocodes/retry
```
Then import into your Deno project:
```js
import { Retrier } from "@humanwhocodes/retry";
```

## Bun
Install using this command:
```
bun add @humanwhocodes/retry
```
Import into your Bun project:
```js
import { Retrier } from "@humanwhocodes/retry";
```

## Browser
It's recommended to import the minified version to save bandwidth:
```js
import { Retrier } from "https://cdn.skypack.dev/@humanwhocodes/retry?min";
```
However, you can also import the unminified version for debugging purposes:
```js
import { Retrier } from "https://cdn.skypack.dev/@humanwhocodes/retry";
```

## API
After importing, create a new instance of `Retrier` and specify the function to run on the error. This function should return `true` if you want the call retried and `false` if not.
```js
// this instance will retry if the specific error code is found
const retrier = new Retrier(error => {
    return error.code === "ENFILE" || error.code === "EMFILE";
});
```
Then, call the `retry()` method around the function you'd like to retry, such as:
```js
import fs from "fs/promises";

const retrier = new Retrier(error => {
    return error.code === "ENFILE" || error.code === "EMFILE";
});

const text = await retrier.retry(() => fs.readFile("README.md", "utf8"));
```
The `retry()` method will either pass through the result on success or wait and retry on failure. Any error that isn't caught by the retrier is automatically rejected so the end result is a transparent passing through of both success and failure.

## Setting a Timeout
You can control how long a task will attempt to retry before giving up by passing the `timeout` option to the `Retrier` constructor. By default, the timeout is one minute.
```js
import fs from "fs/promises";

const retrier = new Retrier(error => {
    return error.code === "ENFILE" || error.code === "EMFILE";
}, { timeout: 100_000 });

const text = await retrier.retry(() => fs.readFile("README.md", "utf8"));
```
When a call times out, it rejects the first error that was received from calling the function.

## Setting a Concurrency Limit
When processing a large number of function calls, you can limit the number of concurrent function calls by passing the `concurrency` option to the `Retrier` constructor. By default, `concurrency` is 1000.
```js
import fs from "fs/promises";

const retrier = new Retrier(error => {
    return error.code === "ENFILE" || error.code === "EMFILE";
}, { concurrency: 100 });

const filenames = getFilenames();
const contents = await Promise.all(
    filenames.map(filename => retrier.retry(() => fs.readFile(filename, "utf8"))
);
```

## Aborting with `AbortSignal`
You can also pass an `AbortSignal` to cancel a retry:
```js
import fs from "fs/promises";

const controller = new AbortController();
const retrier = new Retrier(error => {
    return error.code === "ENFILE" || error.code === "EMFILE";
});

const text = await retrier.retry(
    () => fs.readFile("README.md", "utf8"),
    { signal: controller.signal }
);
```

## Developer Setup
1. Fork the repository
2. Clone your fork
3. Run `npm install` to setup dependencies
4. Run `npm test` to run tests

## Debug Output
Enable debugging output by setting the `DEBUG` environment variable to `"@hwc/retry"` before running.

## License
Apache 2.0

## Prior Art
This utility is inspired by, and contains code from [`graceful-fs`](https://github.com/isaacs/node-graceful-fs).
[npm]: https://npmjs.com/
[yarn]: https://yarnpkg.com/

---

# iCloud: web-app/node_modules/@humanwhocodes/module-importer/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@humanwhocodes/module-importer/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.722Z

## Bug Fixes
* Ensure CommonJS mode works correctly. ([cf54a0b](https://github.com/humanwhocodes/module-importer/commit/cf54a0b998085066fbe1776dd0b4cacd808cc192)), closes [#6](https://github.com/humanwhocodes/module-importer/issues/6)

## Features
* Implement ModuleImporter ([3ce4e82](https://www.github.com/humanwhocodes/module-importer/commit/3ce4e820c30c114e787bfed00a0966ac4772f563))

---

# iCloud: web-app/node_modules/@humanwhocodes/module-importer/README.md

> **Source:** icloud://web-app/node_modules/@humanwhocodes/module-importer/README.md
> **Analyzed At:** 2026-06-13T06:32:46.726Z

## ModuleImporter
by [Nicholas C. Zakas](https://humanwhocodes.com)
If you find this useful, please consider supporting my work with a [donation](https://humanwhocodes.com/donate).

## Description
A utility for seamlessly importing modules in Node.js regardless if they are CommonJS or ESM format. Under the hood, this uses `import()` and relies on Node.js's CommonJS compatibility to work correctly. This ensures that the correct locations and formats are used for CommonJS so you can call one method and not worry about any compatibility issues.
The problem with the default `import()` is that it always resolves relative to the file location in which it is called. If you want to resolve from a different location, you need to jump through a few hoops to achieve that. This package makes it easy to both resolve and import modules from any directory.

## Node.js
Install using [npm][npm] or [yarn][yarn]:
```
npm install @humanwhocodes/module-importer

# or

yarn add @humanwhocodes/module-importer
```
Import into your Node.js project:
```js
// CommonJS
const { ModuleImporter } = require("@humanwhocodes/module-importer");

// ESM
import { ModuleImporter } from "@humanwhocodes/module-importer";
```

## Bun
Install using this command:
```
bun add @humanwhocodes/module-importer
```
Import into your Bun project:
```js
import { ModuleImporter } from "@humanwhocodes/module-importer";
```

## API
After importing, create a new instance of `ModuleImporter` to start emitting events:
```js
// cwd can be omitted to use process.cwd()
const importer = new ModuleImporter(cwd);

// you can resolve the location of any package
const location = importer.resolve("./some-file.cjs");

// you can also import directly
const module = importer.import("./some-file.cjs");
```
For both `resolve()` and `import()`, you can pass in package names and filenames.

## Developer Setup
1. Fork the repository
2. Clone your fork
3. Run `npm install` to setup dependencies
4. Run `npm test` to run tests

## License
Apache 2.0
[npm]: https://npmjs.com/
[yarn]: https://yarnpkg.com/

---

# iCloud: web-app/node_modules/@humanfs/node/README.md

> **Source:** icloud://web-app/node_modules/@humanfs/node/README.md
> **Analyzed At:** 2026-06-13T06:32:46.730Z

## `@humanfs/node`
by [Nicholas C. Zakas](https://humanwhocodes.com)
If you find this useful, please consider supporting my work with a [donation](https://humanwhocodes.com/donate) or [nominate me](https://stars.github.com/nominate/) for a GitHub Star.

## Description
The `hfs` bindings for use in Node.js and Node.js-compatible runtimes.
> [!WARNING]
> This project is **experimental** and may change significantly before v1.0.0. Use at your own caution and definitely not in production!

## Installation
Install using your favorite package manager:
```shell
npm install @humanfs/node

# or

pnpm install @humanfs/node

# or

yarn add @humanfs/node

# or

bun install @humanfs/node
```

## Usage
The easiest way to use hfs in your project is to import the `hfs` object:
```js
import { hfs } from "@humanfs/node";
```
Then, you can use the API methods:
```js
// 1. Files

// read from a text file
const text = await hfs.text("file.txt");

// read from a JSON file
const json = await hfs.json("file.json");

// read raw bytes from a text file
const arrayBuffer = await hfs.arrayBuffer("file.txt");

// write text to a file
await hfs.write("file.txt", "Hello world!");

// write bytes to a file
await hfs.write("file.txt", new TextEncoder().encode("Hello world!"));

// append text to a file
await hfs.append("file.txt", "Hello world!");

// append bytes to a file
await hfs.append("file.txt", new TextEncoder().encode("Hello world!"));

// does the file exist?
const found = await hfs.isFile("file.txt");

// how big is the file?
const size = await hfs.size("file.txt");

// when was the file modified?
const mtime = await hfs.lastModified("file.txt");

// copy a file from one location to another
await hfs.copy("file.txt", "file-copy.txt");

// move a file from one location to another
await hfs.move("file.txt", "renamed.txt");

// delete a file
await hfs.delete("file.txt");

// 2. Directories

// create a directory
await hfs.createDirectory("dir");

// create a directory recursively
await hfs.createDirectory("dir/subdir");

// does the directory exist?
const dirFound = await hfs.isDirectory("dir");

// copy the entire directory
hfs.copyAll("from-dir", "to-dir");

// move the entire directory
hfs.moveAll("from-dir", "to-dir");

// delete a directory
await hfs.delete("dir");

// delete a non-empty directory
await hfs.deleteAll("dir");
```
If you'd like to create your own instance, import the `NodeHfs` constructor:
```js
import { NodeHfs } from "@humanfs/node";
import fsp from "fs/promises";

const hfs = new NodeHfs();

// optionally specify the fs/promises object to use
const hfs = new NodeHfs({ fsp });
```
If you'd like to use just the impl, import the `NodeHfsImpl` constructor:
```js
import { NodeHfsImpl } from "@humanfs/node";
import fsp from "fs/promises";

const hfs = new NodeHfsImpl();

// optionally specify the fs/promises object to use
const hfs = new NodeHfsImpl({ fsp });
```

## Errors Handled
* `ENOENT` - in most cases, these errors are handled silently.
* `ENFILE` and `EMFILE` - calls that result in these errors are retried for up to 60 seconds before giving up for good.

## License
Apache 2.0

---

# iCloud: web-app/node_modules/@humanfs/core/README.md

> **Source:** icloud://web-app/node_modules/@humanfs/core/README.md
> **Analyzed At:** 2026-06-13T06:32:46.735Z

## `@humanfs/core`
by [Nicholas C. Zakas](https://humanwhocodes.com)
If you find this useful, please consider supporting my work with a [donation](https://humanwhocodes.com/donate) or [nominate me](https://stars.github.com/nominate/) for a GitHub Star.

## Description
The core functionality for humanfs that is shared across all implementations for all runtimes. The contents of this package are intentionally runtime agnostic and are not intended to be used alone.
Currently, this package simply exports the `Hfs` class, which is an abstract base class intended to be inherited from in runtime-specific hfs packages (like `@humanfs/node`).
> [!WARNING]
> This project is **experimental** and may change significantly before v1.0.0. Use at your own caution and definitely not in production!

## Node.js
Install using your favorite package manager for Node.js:
```shell
npm install @humanfs/core

# or

pnpm install @humanfs/core

# or

yarn add @humanfs/core

# or

bun install @humanfs/core
```
Then you can import the `Hfs` and `Path` classes like this:
```js
import { Hfs, Path } from "@humanfs/core";
```

## Deno
Install using [JSR](https://jsr.io):
```shell
deno add @humanfs/core

# or

jsr add @humanfs/core
```
Then you can import the `Hfs` class like this:
```js
import { Hfs, Path } from "@humanfs/core";
```

## Browser
It's recommended to import the minified version to save bandwidth:
```js
import { Hfs, Path } from "https://cdn.skypack.dev/@humanfs/core?min";
```
However, you can also import the unminified version for debugging purposes:
```js
import { Hfs, Path } from "https://cdn.skypack.dev/@humanfs/core";
```

## `Hfs` Class
The `Hfs` class contains all of the basic functionality for an `Hfs` instance *without* a predefined impl. This class is mostly used for creating runtime-specific impls, such as `NodeHfs` and `DenoHfs`.
You can create your own instance by providing an `impl` directly:
```js
const hfs = new Hfs({ impl: { async text() {} }});
```
The specified `impl` becomes the base impl for the instance, meaning you can always reset back to it using `resetImpl()`.
You can also inherit from `Hfs` to create your own class with a preconfigured impl, such as:
```js
class MyHfs extends Hfs {
	constructor() {
		super({
			impl: myImpl
		});
	}
}
```

## `Path` Class
The `Path` class represents the path to a directory or file within a file system. It's an abstract representation that can be used even outside of traditional file systems where string paths might not make sense.
```js
const myPath = new Path(["dir", "subdir"]);
console.log(myPath.toString());		// "dir/subdir"

// add another step
myPath.push("file.txt");
console.log(myPath.toString());		// "dir/subdir/file.txt"

// get just the last step
console.log(myPath.name);			// "file.txt"

// change just the last step
myPath.name = "file.json";
console.log(myPath.name);			// "file.json"
console.log(myPath.toString());		// "dir/subdir/file.json"

// get the size of the path
console.log(myPath.size);			// 3

// remove the last step
myPath.pop();
console.log(myPath.toString());		// "dir/subdir"

// iterate over the steps
for (const step of myPath) {
	// do something
}

// create a new path from a string
const newPath = Path.fromString("/foo/bar");
```

## License
Apache 2.0

---

# iCloud: web-app/node_modules/@hono/node-server/README.md

> **Source:** icloud://web-app/node_modules/@hono/node-server/README.md
> **Analyzed At:** 2026-06-13T06:32:46.739Z

## Node.js Adapter for Hono
This adapter `@hono/node-server` allows you to run your Hono application on Node.js.
Initially, Hono wasn't designed for Node.js, but with this adapter, you can now use Hono on Node.js.
It utilizes web standard APIs implemented in Node.js version 18 or higher.

## Benchmarks
Hono is 3.5 times faster than Express.
Express:
```txt
$ bombardier -d 10s --fasthttp http://localhost:3000/

Statistics        Avg      Stdev        Max
  Reqs/sec     16438.94    1603.39   19155.47
  Latency        7.60ms     7.51ms   559.89ms
  HTTP codes:
    1xx - 0, 2xx - 164494, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     4.55MB/s
```
Hono + `@hono/node-server`:
```txt
$ bombardier -d 10s --fasthttp http://localhost:3000/

Statistics        Avg      Stdev        Max
  Reqs/sec     58296.56    5512.74   74403.56
  Latency        2.14ms     1.46ms   190.92ms
  HTTP codes:
    1xx - 0, 2xx - 583059, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    12.56MB/s
```

## Requirements
It works on Node.js versions greater than 18.x. The specific required Node.js versions are as follows:
- 18.x => 18.14.1+
- 19.x => 19.7.0+
- 20.x => 20.0.0+
Essentially, you can simply use the latest version of each major release.

## Installation
You can install it from the npm registry with `npm` command:
```sh
npm install @hono/node-server
```
Or use `yarn`:
```sh
yarn add @hono/node-server
```

## Usage
Just import `@hono/node-server` at the top and write the code as usual.
The same code that runs on Cloudflare Workers, Deno, and Bun will work.
```ts
import { serve } from '@hono/node-server'
import { Hono } from 'hono'

const app = new Hono()
app.get('/', (c) => c.text('Hono meets Node.js'))

serve(app, (info) => {
  console.log(`Listening on http://localhost:${info.port}`) // Listening on http://localhost:3000
})
```
For example, run it using `ts-node`. Then an HTTP server will be launched. The default port is `3000`.
```sh
ts-node ./index.ts
```
Open `http://localhost:3000` with your browser.

## `port`
```ts
serve({
  fetch: app.fetch,
  port: 8787, // Port number, default is 3000
})
```

## `createServer`
```ts
import { createServer } from 'node:https'
import fs from 'node:fs'

//...

serve({
  fetch: app.fetch,
  createServer: createServer,
  serverOptions: {
    key: fs.readFileSync('test/fixtures/keys/agent1-key.pem'),
    cert: fs.readFileSync('test/fixtures/keys/agent1-cert.pem'),
  },
})
```

## `overrideGlobalObjects`
The default value is `true`. The Node.js Adapter rewrites the global Request/Response and uses a lightweight Request/Response to improve performance. If you don't want to do that, set `false`.
```ts
serve({
  fetch: app.fetch,
  overrideGlobalObjects: false,
})
```

## `autoCleanupIncoming`
The default value is `true`. The Node.js Adapter automatically cleans up (explicitly call `destroy()` method) if application is not finished to consume the incoming request. If you don't want to do that, set `false`.
If the application accepts connections from arbitrary clients, this cleanup must be done otherwise incomplete requests from clients may cause the application to stop responding. If your application only accepts connections from trusted clients, such as in a reverse proxy environment and there is no process that returns a response without reading the body of the POST request all the way through, you can improve performance by setting it to `false`.
```ts
serve({
  fetch: app.fetch,
  autoCleanupIncoming: false,
})
```

## Middleware
Most built-in middleware also works with Node.js.
Read [the documentation](https://hono.dev/middleware/builtin/basic-auth) and use the Middleware of your liking.
```ts
import { serve } from '@hono/node-server'
import { Hono } from 'hono'
import { prettyJSON } from 'hono/pretty-json'

const app = new Hono()

app.get('*', prettyJSON())
app.get('/', (c) => c.json({ 'Hono meets': 'Node.js' }))

serve(app)
```

## Serve Static Middleware
Use Serve Static Middleware that has been created for Node.js.
```ts
import { serveStatic } from '@hono/node-server/serve-static'

//...

app.use('/static/*', serveStatic({ root: './' }))
```
If using a relative path, `root` will be relative to the current working directory from which the app was started.
This can cause confusion when running your application locally.
Imagine your project structure is:
```
my-hono-project/
  src/
    index.ts
  static/
    index.html
```
Typically, you would run your app from the project's root directory (`my-hono-project`),
so you would need the following code to serve the `static` folder:
```ts
app.use('/static/*', serveStatic({ root: './static' }))
```
Notice that `root` here is not relative to `src/index.ts`, rather to `my-hono-project`.

## `rewriteRequestPath`
If you want to serve files in `./.foojs` with the request path `/__foo/*`, you can write like the following.
```ts
app.use(
  '/__foo/*',
  serveStatic({
    root: './.foojs/',
    rewriteRequestPath: (path: string) => path.replace(/^\/__foo/, ''),
  })
)
```

## `onFound`
You can specify handling when the requested file is found with `onFound`.
```ts
app.use(
  '/static/*',
  serveStatic({
    // ...
    onFound: (_path, c) => {
      c.header('Cache-Control', `public, immutable, max-age=31536000`)
    },
  })
)
```

## `onNotFound`
The `onNotFound` is useful for debugging. You can write a handle for when a file is not found.
```ts
app.use(
  '/static/*',
  serveStatic({
    root: './non-existent-dir',
    onNotFound: (path, c) => {
      console.log(`${path} is not found, request to ${c.req.path}`)
    },
  })
)
```

## `precompressed`
The `precompressed` option checks if files with extensions like `.br` or `.gz` are available and serves them based on the `Accept-Encoding` header. It prioritizes Brotli, then Zstd, and Gzip. If none are available, it serves the original file.
```ts
app.use(
  '/static/*',
  serveStatic({
    precompressed: true,
  })
)
```

## ConnInfo Helper
You can use the [ConnInfo Helper](https://hono.dev/docs/helpers/conninfo) by importing `getConnInfo` from `@hono/node-server/conninfo`.
```ts
import { getConnInfo } from '@hono/node-server/conninfo'

app.get('/', (c) => {
  const info = getConnInfo(c) // info is `ConnInfo`
  return c.text(`Your remote address is ${info.remote.address}`)
})
```

## Accessing Node.js API
You can access the Node.js API from `c.env` in Node.js. For example, if you want to specify a type, you can write the following.
```ts
import { serve } from '@hono/node-server'
import type { HttpBindings } from '@hono/node-server'
import { Hono } from 'hono'

const app = new Hono<{ Bindings: HttpBindings }>()

app.get('/', (c) => {
  return c.json({
    remoteAddress: c.env.incoming.socket.remoteAddress,
  })
})

serve(app)
```
The APIs that you can get from `c.env` are as follows.
```ts
type HttpBindings = {
  incoming: IncomingMessage
  outgoing: ServerResponse
}

type Http2Bindings = {
  incoming: Http2ServerRequest
  outgoing: Http2ServerResponse
}
```

## Direct response from Node.js API
You can directly respond to the client from the Node.js API.
In that case, the response from Hono should be ignored, so return `RESPONSE_ALREADY_SENT`.
> [!NOTE]
> This feature can be used when migrating existing Node.js applications to Hono, but we recommend using Hono's API for new applications.
```ts
import { serve } from '@hono/node-server'
import type { HttpBindings } from '@hono/node-server'
import { RESPONSE_ALREADY_SENT } from '@hono/node-server/utils/response'
import { Hono } from 'hono'

const app = new Hono<{ Bindings: HttpBindings }>()

app.get('/', (c) => {
  const { outgoing } = c.env
  outgoing.writeHead(200, { 'Content-Type': 'text/plain' })
  outgoing.end('Hello World\n')

  return RESPONSE_ALREADY_SENT
})

serve(app)
```

## Listen to a UNIX domain socket
You can configure the HTTP server to listen to a UNIX domain socket instead of a TCP port.
```ts
import { createAdaptorServer } from '@hono/node-server'

// ...

const socketPath = '/tmp/example.sock'

const server = createAdaptorServer(app)
server.listen(socketPath, () => {
  console.log(`Listening on ${socketPath}`)
})
```

## Related projects
- Hono - 
- Hono GitHub repository -

## Authors
- Yusuke Wada 
- Taku Amano

---

# iCloud: web-app/node_modules/@google-cloud/vertexai/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@google-cloud/vertexai/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.744Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@google-cloud/vertexai/node_modules/gcp-metadata/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/vertexai/node_modules/gcp-metadata/README.md
> **Analyzed At:** 2026-06-13T06:32:46.767Z

## [GCP Metadata: Node.js Client](https://github.com/googleapis/gcp-metadata)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/gcp-metadata.svg)](https://www.npmjs.org/package/gcp-metadata)
Get the metadata from a Google Cloud Platform environment
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/gcp-metadata/blob/main/CHANGELOG.md).
* [GCP Metadata Node.js Client API Reference][client-docs]
* [GCP Metadata Documentation][product-docs]
* [github.com/googleapis/gcp-metadata](https://github.com/googleapis/gcp-metadata)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Using the client library](#using-the-client-library)
* [Samples](#samples)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install gcp-metadata
```

## Using the client library
```javascript
const gcpMetadata = require('gcp-metadata');

async function quickstart() {
  // check to see if this code can access a metadata server
  const isAvailable = await gcpMetadata.isAvailable();
  console.log(`Is available: ${isAvailable}`);

  // Instance and Project level metadata will only be available if
  // running inside of a Google Cloud compute environment such as
  // Cloud Functions, App Engine, Kubernetes Engine, or Compute Engine.
  // To learn more about the differences between instance and project
  // level metadata, see:
  // https://cloud.google.com/compute/docs/storing-retrieving-metadata#project-instance-metadata
  if (isAvailable) {
    // grab all top level metadata from the service
    const instanceMetadata = await gcpMetadata.instance();
    console.log('Instance metadata:');
    console.log(instanceMetadata);

    // get all project level metadata
    const projectMetadata = await gcpMetadata.project();
    console.log('Project metadata:');
    console.log(projectMetadata);
  }
}

quickstart();

```

## Check to see if the metadata server is available
```js
const isAvailable = await gcpMetadata.isAvailable();
```

## Access all metadata
```js
const data = await gcpMetadata.instance();
console.log(data); // ... All metadata properties
```

## Access specific properties
```js
const data = await gcpMetadata.instance('hostname');
console.log(data); // ...Instance hostname
const projectId = await gcpMetadata.project('project-id');
console.log(projectId); // ...Project ID of the running instance
```

## Access nested properties with the relative path
```js
const data = await gcpMetadata.instance('service-accounts/default/email');
console.log(data); // ...Email address of the Compute identity service account
```

## Access specific properties with query parameters
```js
const data = await gcpMetadata.instance({
  property: 'tags',
  params: { alt: 'text' }
});
console.log(data) // ...Tags as newline-delimited list
```

## Access with custom headers
```js
await gcpMetadata.instance({
  headers: { 'no-trace': '1' }
}); // ...Request is untraced
```

## Take care with large number valued properties
In some cases number valued properties returned by the Metadata Service may be
too large to be representable as JavaScript numbers. In such cases we return
those values as `BigNumber` objects (from the [bignumber.js](https://github.com/MikeMcl/bignumber.js) library). Numbers
that fit within the JavaScript number range will be returned as normal number
values.
```js
const id = await gcpMetadata.instance('id');
console.log(id)  // ... BigNumber { s: 1, e: 18, c: [ 45200, 31799277581759 ] }
console.log(id.toString()) // ... 4520031799277581759
```

## Environment variables
* `GCE_METADATA_HOST`: provide an alternate host or IP to perform lookup against (useful, for example, you're connecting through a custom proxy server).
For example:
  ```
  export GCE_METADATA_HOST='169.254.169.254'
```
* `DETECT_GCP_RETRIES`: number representing number of retries that should be attempted on metadata lookup.
* `DEBUG_AUTH`: emit debugging logs
* `METADATA_SERVER_DETECTION`: configure desired metadata server availability check behavior.
* `assume-present`: don't try to ping the metadata server, but assume it's present
* `none`: don't try to ping the metadata server, but don't try to use it either
* `bios-only`: treat the result of a BIOS probe as canonical (don't fall back to pinging)
* `ping-only`: skip the BIOS probe, and go straight to pinging

## Samples
Samples are in the [`samples/`](https://github.com/googleapis/gcp-metadata/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.
| Sample                      | Source Code                       | Try it |
| --------------------------- | --------------------------------- | ------ |
| Quickstart | [source code](https://github.com/googleapis/gcp-metadata/blob/main/samples/quickstart.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/gcp-metadata&page=editor&open_in_editor=samples/quickstart.js,samples/README.md) |
The [GCP Metadata Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install gcp-metadata@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/gcp-metadata/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/gcp-metadata/blob/main/LICENSE)
[client-docs]: https://cloud.google.com/nodejs/docs/reference/gcp-metadata/latest
[product-docs]: https://cloud.google.com/compute/docs/storing-retrieving-metadata
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/external/set-up-adc-local

---

# iCloud: web-app/node_modules/@google-cloud/vertexai/node_modules/gaxios/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/vertexai/node_modules/gaxios/README.md
> **Analyzed At:** 2026-06-13T06:32:46.772Z

## gaxios
[![npm version](https://img.shields.io/npm/v/gaxios.svg)](https://www.npmjs.org/package/gaxios)
[![codecov](https://codecov.io/gh/googleapis/gaxios/branch/master/graph/badge.svg)](https://codecov.io/gh/googleapis/gaxios)
[![Code Style: Google](https://img.shields.io/badge/code%20style-google-blueviolet.svg)](https://github.com/google/gts)
> An HTTP request client that provides an `axios` like interface over top of `node-fetch`.

## Install
```sh
$ npm install gaxios
```

## Example
```js
const {request} = require('gaxios');
const res = await request({
  url: 'https://www.googleapis.com/discovery/v1/apis/',
});
```

## Setting Defaults
Gaxios supports setting default properties both on the default instance, and on additional instances. This is often useful when making many requests to the same domain with the same base settings. For example:
```js
const gaxios = require('gaxios');
gaxios.instance.defaults = {
  baseURL: 'https://example.com'
  headers: {
    Authorization: 'SOME_TOKEN'
  }
}
gaxios.request({url: '/data'}).then(...);
```
Note that setting default values will take precedence
over other authentication methods, i.e., application default credentials.

## Request Options
```ts
interface GaxiosOptions = {
  // The url to which the request should be sent.  Required.
  url: string,

  // The HTTP method to use for the request.  Defaults to `GET`.
  method: 'GET',

  // The base Url to use for the request. Prepended to the `url` property above.
  baseURL: 'https://example.com';

  // The HTTP methods to be sent with the request.
  headers: { 'some': 'header' },

  // The data to send in the body of the request. Data objects will be
  // serialized as JSON.
  //
  // Note: if you would like to provide a Content-Type header other than
  // application/json you you must provide a string or readable stream, rather
  // than an object:
  // data: JSON.stringify({some: 'data'})
  // data: fs.readFile('./some-data.jpeg')
  data: {
    some: 'data'
  },

  // The max size of the http response content in bytes allowed.
  // Defaults to `0`, which is the same as unset.
  maxContentLength: 2000,

  // The max number of HTTP redirects to follow.
  // Defaults to 100.
  maxRedirects: 100,

  // The querystring parameters that will be encoded using `qs` and
  // appended to the url
  params: {
    querystring: 'parameters'
  },

  // By default, we use the `querystring` package in node core to serialize
  // querystring parameters.  You can override that and provide your
  // own implementation.
  paramsSerializer: (params) => {
    return qs.stringify(params);
  },

  // The timeout for the HTTP request in milliseconds. Defaults to 0.
  timeout: 1000,

  // Optional method to override making the actual HTTP request. Useful
  // for writing tests and instrumentation
  adapter?: async (options, defaultAdapter) => {
    const res = await defaultAdapter(options);
    res.data = {
      ...res.data,
      extraProperty: 'your extra property',
    };
    return res;
  };

  // The expected return type of the request.  Options are:
  // json | stream | blob | arraybuffer | text | unknown
  // Defaults to `unknown`.
  responseType: 'unknown',

  // The node.js http agent to use for the request.
  agent: someHttpsAgent,

  // Custom function to determine if the response is valid based on the
  // status code.  Defaults to (>= 200 && < 300)
  validateStatus: (status: number) => true,

  // Implementation of `fetch` to use when making the API call. By default,
  // will use the browser context if available, and fall back to `node-fetch`
  // in node.js otherwise.
  fetchImplementation?: typeof fetch;

  // Configuration for retrying of requests.
  retryConfig: {
    // The number of times to retry the request.  Defaults to 3.
    retry?: number;

    // The number of retries already attempted.
    currentRetryAttempt?: number;

    // The HTTP Methods that will be automatically retried.
    // Defaults to ['GET','PUT','HEAD','OPTIONS','DELETE']
    httpMethodsToRetry?: string[];

    // The HTTP response status codes that will automatically be retried.
    // Defaults to: [[100, 199], [408, 408], [429, 429], [500, 599]]
    statusCodesToRetry?: number[][];

    // Function to invoke when a retry attempt is made.
    onRetryAttempt?: (err: GaxiosError) => Promise<void> | void;

    // Function to invoke which determines if you should retry
    shouldRetry?: (err: GaxiosError) => Promise<boolean> | boolean;

    // When there is no response, the number of retries to attempt. Defaults to 2.
    noResponseRetries?: number;

    // The amount of time to initially delay the retry, in ms.  Defaults to 100ms.
    retryDelay?: number;
  },

  // Enables default configuration for retries.
  retry: boolean,

  // Cancelling a request requires the `abort-controller` library.
  // See https://github.com/bitinn/node-fetch#request-cancellation-with-abortsignal
  signal?: AbortSignal

  /**
   * A collection of parts to send as a `Content-Type: multipart/related` request.
   */
  multipart?: GaxiosMultipartOptions;

  /**
   * An optional proxy to use for requests.
   * Available via `process.env.HTTP_PROXY` and `process.env.HTTPS_PROXY` as well - with a preference for the this config option when multiple are available.
   * The `agent` option overrides this.
   *
   * @see {@link GaxiosOptions.noProxy}
   * @see {@link GaxiosOptions.agent}
   */
  proxy?: string | URL;
  /**
   * A list for excluding traffic for proxies.
   * Available via `process.env.NO_PROXY` as well as a common-separated list of strings - merged with any local `noProxy` rules.
   *
   * - When provided a string, it is matched by
   *   - Wildcard `*.` and `.` matching are available. (e.g. `.example.com` or `*.example.com`)
   * - When provided a URL, it is matched by the `.origin` property.
   *   - For example, requesting `https://example.com` with the following `noProxy`s would result in a no proxy use:
   *     - new URL('https://example.com')
   *     - new URL('https://example.com:443')
   *   - The following would be used with a proxy:
   *     - new URL('http://example.com:80')
   *     - new URL('https://example.com:8443')
   * - When provided a regular expression it is used to match the stringified URL
   *
   * @see {@link GaxiosOptions.proxy}
   */
  noProxy?: (string | URL | RegExp)[];

  /**
   * An experimental, customizable error redactor.
   *
   * Set `false` to disable.
   *
   * @remarks
   *
   * This does not replace the requirement for an active Data Loss Prevention (DLP) provider. For DLP suggestions, see:
   * - https://cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data#dlp_deidentify_replace_infotype-nodejs
   * - https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets
   *
   * @experimental
   */
  errorRedactor?: typeof defaultErrorRedactor | false;
}
```

## License
[Apache-2.0](https://github.com/googleapis/gaxios/blob/master/LICENSE)

---

# iCloud: web-app/node_modules/@google-cloud/storage/node_modules/uuid/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@google-cloud/storage/node_modules/uuid/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.783Z

## Changelog
All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## Bug Fixes
- lazy load getRandomValues ([#537](https://github.com/uuidjs/uuid/issues/537)) ([16c8f6d](https://github.com/uuidjs/uuid/commit/16c8f6df2f6b09b4d6235602d6a591188320a82e)), closes [#536](https://github.com/uuidjs/uuid/issues/536)

## Bug Fixes
- support expo>=39.0.0 ([#515](https://github.com/uuidjs/uuid/issues/515)) ([c65a0f3](https://github.com/uuidjs/uuid/commit/c65a0f3fa73b901959d638d1e3591dfacdbed867)), closes [#375](https://github.com/uuidjs/uuid/issues/375)

## Features
- add parse/stringify/validate/version/NIL APIs ([#479](https://github.com/uuidjs/uuid/issues/479)) ([0e6c10b](https://github.com/uuidjs/uuid/commit/0e6c10ba1bf9517796ff23c052fc0468eedfd5f4)), closes [#475](https://github.com/uuidjs/uuid/issues/475) [#478](https://github.com/uuidjs/uuid/issues/478) [#480](https://github.com/uuidjs/uuid/issues/480) [#481](https://github.com/uuidjs/uuid/issues/481) [#180](https://github.com/uuidjs/uuid/issues/180)

## Features
- improve performance of v1 string representation ([#453](https://github.com/uuidjs/uuid/issues/453)) ([0ee0b67](https://github.com/uuidjs/uuid/commit/0ee0b67c37846529c66089880414d29f3ae132d5))
- remove deprecated v4 string parameter ([#454](https://github.com/uuidjs/uuid/issues/454)) ([88ce3ca](https://github.com/uuidjs/uuid/commit/88ce3ca0ba046f60856de62c7ce03f7ba98ba46c)), closes [#437](https://github.com/uuidjs/uuid/issues/437)
- support jspm ([#473](https://github.com/uuidjs/uuid/issues/473)) ([e9f2587](https://github.com/uuidjs/uuid/commit/e9f2587a92575cac31bc1d4ae944e17c09756659))

## Bug Fixes
- prepare package exports for webpack 5 ([#468](https://github.com/uuidjs/uuid/issues/468)) ([8d6e6a5](https://github.com/uuidjs/uuid/commit/8d6e6a5f8965ca9575eb4d92e99a43435f4a58a8))

## Features
- improve v4 performance by reusing random number array ([#435](https://github.com/uuidjs/uuid/issues/435)) ([bf4af0d](https://github.com/uuidjs/uuid/commit/bf4af0d711b4d2ed03d1f74fd12ad0baa87dc79d))
- optimize V8 performance of bytesToUuid ([#434](https://github.com/uuidjs/uuid/issues/434)) ([e156415](https://github.com/uuidjs/uuid/commit/e156415448ec1af2351fa0b6660cfb22581971f2))

## Bug Fixes
- export package.json required by react-native and bundlers ([#449](https://github.com/uuidjs/uuid/issues/449)) ([be1c8fe](https://github.com/uuidjs/uuid/commit/be1c8fe9a3206c358e0059b52fafd7213aa48a52)), closes [ai/nanoevents#44](https://github.com/ai/nanoevents/issues/44#issuecomment-602010343) [#444](https://github.com/uuidjs/uuid/issues/444)

## ⚠ BREAKING CHANGES
- For native ECMAScript Module (ESM) usage in Node.js only named exports are exposed, there is no more default export.
  ```diff
  -import uuid from 'uuid';
  -console.log(uuid.v4()); // -> 'cd6c3b08-0adc-4f4b-a6ef-36087a1c9869'
  +import { v4 as uuidv4 } from 'uuid';
  +uuidv4(); // ⇨ '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'
```
- Deep requiring specific algorithms of this library like `require('uuid/v4')`, which has been deprecated in `uuid@7`, is no longer supported.
Instead use the named exports that this module exports.
For ECMAScript Modules (ESM):
  ```diff
  -import uuidv4 from 'uuid/v4';
  +import { v4 as uuidv4 } from 'uuid';
  uuidv4();
```
For CommonJS:
  ```diff
  -const uuidv4 = require('uuid/v4');
  +const { v4: uuidv4 } = require('uuid');
  uuidv4();
```

## Features
- native Node.js ES Modules (wrapper approach) ([#423](https://github.com/uuidjs/uuid/issues/423)) ([2d9f590](https://github.com/uuidjs/uuid/commit/2d9f590ad9701d692625c07ed62f0a0f91227991)), closes [#245](https://github.com/uuidjs/uuid/issues/245) [#419](https://github.com/uuidjs/uuid/issues/419) [#342](https://github.com/uuidjs/uuid/issues/342)
- remove deep requires ([#426](https://github.com/uuidjs/uuid/issues/426)) ([daf72b8](https://github.com/uuidjs/uuid/commit/daf72b84ceb20272a81bb5fbddb05dd95922cbba))

## Bug Fixes
- add CommonJS syntax example to README quickstart section ([#417](https://github.com/uuidjs/uuid/issues/417)) ([e0ec840](https://github.com/uuidjs/uuid/commit/e0ec8402c7ad44b7ef0453036c612f5db513fda0))

## Bug Fixes
- make deep require deprecation warning work in browsers ([#409](https://github.com/uuidjs/uuid/issues/409)) ([4b71107](https://github.com/uuidjs/uuid/commit/4b71107d8c0d2ef56861ede6403fc9dc35a1e6bf)), closes [#408](https://github.com/uuidjs/uuid/issues/408)

## Bug Fixes
- make access to msCrypto consistent ([#393](https://github.com/uuidjs/uuid/issues/393)) ([8bf2a20](https://github.com/uuidjs/uuid/commit/8bf2a20f3565df743da7215eebdbada9d2df118c))
- simplify link in deprecation warning ([#391](https://github.com/uuidjs/uuid/issues/391)) ([bb2c8e4](https://github.com/uuidjs/uuid/commit/bb2c8e4e9f4c5f9c1eaaf3ea59710c633cd90cb7))
- update links to match content in readme ([#386](https://github.com/uuidjs/uuid/issues/386)) ([44f2f86](https://github.com/uuidjs/uuid/commit/44f2f86e9d2bbf14ee5f0f00f72a3db1292666d4))

## Bug Fixes
- clean up esm builds for node and browser ([#383](https://github.com/uuidjs/uuid/issues/383)) ([59e6a49](https://github.com/uuidjs/uuid/commit/59e6a49e7ce7b3e8fb0f3ee52b9daae72af467dc))
- provide browser versions independent from module system ([#380](https://github.com/uuidjs/uuid/issues/380)) ([4344a22](https://github.com/uuidjs/uuid/commit/4344a22e7aed33be8627eeaaf05360f256a21753)), closes [#378](https://github.com/uuidjs/uuid/issues/378)

## ⚠ BREAKING CHANGES
- The default export, which used to be the v4() method but which was already discouraged in v3.x of this library, has been removed.
- Explicitly note that deep imports of the different uuid version functions are deprecated and no longer encouraged and that ECMAScript module named imports should be used instead. Emit a deprecation warning for people who deep-require the different algorithm variants.
- Remove builtin support for insecure random number generators in the browser. Users who want that will have to supply their own random number generator function.
- Remove support for generating v3 and v5 UUIDs in Node.js<4.x
- Convert code base to ECMAScript Modules (ESM) and release CommonJS build for node and ESM build for browser bundlers.

## Features
- add UMD build to npm package ([#357](https://github.com/uuidjs/uuid/issues/357)) ([4e75adf](https://github.com/uuidjs/uuid/commit/4e75adf435196f28e3fbbe0185d654b5ded7ca2c)), closes [#345](https://github.com/uuidjs/uuid/issues/345)
- add various es module and CommonJS examples ([b238510](https://github.com/uuidjs/uuid/commit/b238510bf352463521f74bab175a3af9b7a42555))
- ensure that docs are up-to-date in CI ([ee5e77d](https://github.com/uuidjs/uuid/commit/ee5e77db547474f5a8f23d6c857a6d399209986b))
- hybrid CommonJS & ECMAScript modules build ([a3f078f](https://github.com/uuidjs/uuid/commit/a3f078faa0baff69ab41aed08e041f8f9c8993d0))
- remove insecure fallback random number generator ([3a5842b](https://github.com/uuidjs/uuid/commit/3a5842b141a6e5de0ae338f391661e6b84b167c9)), closes [#173](https://github.com/uuidjs/uuid/issues/173)
- remove support for pre Node.js v4 Buffer API ([#356](https://github.com/uuidjs/uuid/issues/356)) ([b59b5c5](https://github.com/uuidjs/uuid/commit/b59b5c5ecad271c5453f1a156f011671f6d35627))
- rename repository to github:uuidjs/uuid ([#351](https://github.com/uuidjs/uuid/issues/351)) ([c37a518](https://github.com/uuidjs/uuid/commit/c37a518e367ac4b6d0aa62dba1bc6ce9e85020f7)), closes [#338](https://github.com/uuidjs/uuid/issues/338)

## Bug Fixes
- add deep-require proxies for local testing and adjust tests ([#365](https://github.com/uuidjs/uuid/issues/365)) ([7fedc79](https://github.com/uuidjs/uuid/commit/7fedc79ac8fda4bfd1c566c7f05ef4ac13b2db48))
- add note about removal of default export ([#372](https://github.com/uuidjs/uuid/issues/372)) ([12749b7](https://github.com/uuidjs/uuid/commit/12749b700eb49db8a9759fd306d8be05dbfbd58c)), closes [#370](https://github.com/uuidjs/uuid/issues/370)
- deprecated deep requiring of the different algorithm versions ([#361](https://github.com/uuidjs/uuid/issues/361)) ([c0bdf15](https://github.com/uuidjs/uuid/commit/c0bdf15e417639b1aeb0b247b2fb11f7a0a26b23))

## Features
- rename repository to github:uuidjs/uuid ([#351](https://github.com/uuidjs/uuid/issues/351)) ([e2d7314](https://github.com/uuidjs/uuid/commit/e2d7314)), closes [#338](https://github.com/uuidjs/uuid/issues/338)

## Bug Fixes
- no longer run ci tests on node v4
- upgrade dependencies

## Bug Fixes
- typo ([305d877](https://github.com/uuidjs/uuid/commit/305d877))

## Bug Fixes
- fix [#284](https://github.com/uuidjs/uuid/issues/284) by setting function name in try-catch ([f2a60f2](https://github.com/uuidjs/uuid/commit/f2a60f2))

## Bug Fixes
- assignment to readonly property to allow running in strict mode ([#270](https://github.com/uuidjs/uuid/issues/270)) ([d062fdc](https://github.com/uuidjs/uuid/commit/d062fdc))
- fix [#229](https://github.com/uuidjs/uuid/issues/229) ([c9684d4](https://github.com/uuidjs/uuid/commit/c9684d4))
- Get correct version of IE11 crypto ([#274](https://github.com/uuidjs/uuid/issues/274)) ([153d331](https://github.com/uuidjs/uuid/commit/153d331))
- mem issue when generating uuid ([#267](https://github.com/uuidjs/uuid/issues/267)) ([c47702c](https://github.com/uuidjs/uuid/commit/c47702c))

## Features
- enforce Conventional Commit style commit messages ([#282](https://github.com/uuidjs/uuid/issues/282)) ([cc9a182](https://github.com/uuidjs/uuid/commit/cc9a182))

## Bug Fixes
- use msCrypto if available. Fixes [#241](https://github.com/uuidjs/uuid/issues/241) ([#247](https://github.com/uuidjs/uuid/issues/247)) ([1fef18b](https://github.com/uuidjs/uuid/commit/1fef18b))

## Bug Fixes
- remove mistakenly added typescript dependency, rollback version (standard-version will auto-increment) ([09fa824](https://github.com/uuidjs/uuid/commit/09fa824))
- use msCrypto if available. Fixes [#241](https://github.com/uuidjs/uuid/issues/241) ([#247](https://github.com/uuidjs/uuid/issues/247)) ([1fef18b](https://github.com/uuidjs/uuid/commit/1fef18b))

## Features
- Add v3 Support ([#217](https://github.com/uuidjs/uuid/issues/217)) ([d94f726](https://github.com/uuidjs/uuid/commit/d94f726))

## Bug Fixes
- (fix) Add .npmignore file to exclude test/ and other non-essential files from packing. (#183)
- Fix typo (#178)
- Simple typo fix (#165)

## Features
- v5 support in CLI (#197)
- V5 support (#188)

## 3.0.1 (2016-11-28)
- split uuid versions into separate files

## 3.0.0 (2016-11-17)
- remove .parse and .unparse

## 2.0.0
- Removed uuid.BufferClass

## 1.4.0
- Improved module context detection
- Removed public RNG functions

## 1.3.2
- Improve tests and handling of v1() options (Issue #24)
- Expose RNG option to allow for perf testing with different generators

## 1.3.0
- Support for version 1 ids, thanks to [@ctavan](https://github.com/ctavan)!
- Support for node.js crypto API
- De-emphasizing performance in favor of a) cryptographic quality PRNGs where available and b) more manageable code

---

# iCloud: web-app/node_modules/@google-cloud/storage/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@google-cloud/storage/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.787Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@google-cloud/storage/node_modules/mime/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@google-cloud/storage/node_modules/mime/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.801Z

## Changelog
All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## ⚠ BREAKING CHANGES
* drop support for node < 10.x

## Bug Fixes
* skypack.dev for direct browser import, fixes [#263](https://github.com/broofa/mime/issues/263) ([41db4c0](https://github.com/broofa/mime/commit/41db4c042ccf50ea7baf3d2160ea37dcca37998d))

## update
* drop support for node < 10.x ([8857363](https://github.com/broofa/mime/commit/8857363ae0446ed0229b17291cf4483cf801f0d0))

## Features
* mime-db@1.50.0 ([cef0cc4](https://github.com/broofa/mime/commit/cef0cc484ff6d05ff1e12b54ca3e8b856fbc14d8))

## Bug Fixes
* update to mime-db@1.46.0, fixes [#253](https://github.com/broofa/mime/issues/253) ([f10e6aa](https://github.com/broofa/mime/commit/f10e6aa62e1356de7e2491d7fb4374c8dac65800))

## Features
* improved CLI ([#244](https://github.com/broofa/mime/issues/244)) ([c8a8356](https://github.com/broofa/mime/commit/c8a8356e3b27f3ef46b64b89b428fdb547b14d5f))

## Bug Fixes
* update to latest mime-db ([43b09ef](https://github.com/broofa/mime/commit/43b09eff0233eacc449af2b1f99a19ba9e104a44))

## Bug Fixes
* add cli.js to package.json files ([#237](https://github.com/broofa/mime/issues/237)) ([6c070bc](https://github.com/broofa/mime/commit/6c070bc298fa12a48e2ed126fbb9de641a1e7ebc))

## Bug Fixes
* fix [#236](https://github.com/broofa/mime/issues/236) ([7f4ecd0](https://github.com/broofa/mime/commit/7f4ecd0d850ed22c9e3bfda2c11fc74e4dde12a7))
* update to latest mime-db ([c5cb3f2](https://github.com/broofa/mime/commit/c5cb3f2ab8b07642a066efbde1142af1b90c927b))

## Bug Fixes
* don't use arrow function introduced in 2.4.1 ([2e00b5c](https://github.com/broofa/mime/commit/2e00b5c))

## Bug Fixes
* update MDN and mime-db types ([3e567a9](https://github.com/broofa/mime/commit/3e567a9))

## Features
* Bind exported methods ([9d2a7b8](https://github.com/broofa/mime/commit/9d2a7b8))
* update to mime-db@1.37.0 ([49e6e41](https://github.com/broofa/mime/commit/49e6e41))

## Bug Fixes
* fix [#198](https://github.com/broofa/mime/issues/198) ([25ca180](https://github.com/broofa/mime/commit/25ca180))

## Bug Fixes
* fix [#192](https://github.com/broofa/mime/issues/192) ([5c35df6](https://github.com/broofa/mime/commit/5c35df6))

## Features
* add travis-ci testing ([d64160f](https://github.com/broofa/mime/commit/d64160f))

## Bug Fixes
* update types files to mime-db@1.32.0 ([85aac16](https://github.com/broofa/mime/commit/85aac16))

## Bug Fixes
* Retain type->extension mappings for non-default types.  Fixes [#180](https://github.com/broofa/mime/issues/180) ([b5c83fb](https://github.com/broofa/mime/commit/b5c83fb))

## Features
* Retain type->extension mappings for non-default types.  Fixes [#180](https://github.com/broofa/mime/issues/180) ([10f82ac](https://github.com/broofa/mime/commit/10f82ac))

## Features
* Upgrade to mime-db@1.32.0.  Fixes [#185](https://github.com/broofa/mime/issues/185) ([3f775ba](https://github.com/broofa/mime/commit/3f775ba))

## Bug Fixes
* ES5 support (back to node v0.4) ([f14ccb6](https://github.com/broofa/mime/commit/f14ccb6))

## v2.0.4 (24/11/2017)
- [**closed**] Switch to mime-score module for resolving extension contention issues. [#182](https://github.com/broofa/mime/issues/182)
- [**closed**] Update mime-db to 1.31.0 in v1.x branch [#181](https://github.com/broofa/mime/issues/181)
---

## v1.5.0 (22/11/2017)
- [**closed**] need ES5 version ready in npm package [#179](https://github.com/broofa/mime/issues/179)
- [**closed**] mime-db no trace of iWork - pages / numbers / etc. [#178](https://github.com/broofa/mime/issues/178)
- [**closed**] How it works in brownser ? [#176](https://github.com/broofa/mime/issues/176)
- [**closed**] Missing `./Mime` [#175](https://github.com/broofa/mime/issues/175)
- [**closed**] Vulnerable Regular Expression [#167](https://github.com/broofa/mime/issues/167)
---

## v2.0.3 (25/09/2017)
*No changelog for this release.*
---

## v1.4.1 (25/09/2017)
- [**closed**] Issue when bundling with webpack [#172](https://github.com/broofa/mime/issues/172)
---

## v2.0.2 (15/09/2017)
- [**V2**] fs.readFileSync is not a function [#165](https://github.com/broofa/mime/issues/165)
- [**closed**] The extension for video/quicktime should map to .mov, not .qt [#164](https://github.com/broofa/mime/issues/164)
- [**V2**] [v2 Feedback request] Mime class API [#163](https://github.com/broofa/mime/issues/163)
- [**V2**] [v2 Feedback request] Resolving conflicts over extensions [#162](https://github.com/broofa/mime/issues/162)
- [**V2**] Allow callers to load module with official, full, or no defined types.  [#161](https://github.com/broofa/mime/issues/161)
- [**V2**] Use "facets" to resolve extension conflicts [#160](https://github.com/broofa/mime/issues/160)
- [**V2**] Remove fs and path dependencies [#152](https://github.com/broofa/mime/issues/152)
- [**V2**] Default content-type should not be application/octet-stream [#139](https://github.com/broofa/mime/issues/139)
- [**V2**] reset mime-types [#124](https://github.com/broofa/mime/issues/124)
- [**V2**] Extensionless paths should return null or false [#113](https://github.com/broofa/mime/issues/113)
---

## v2.0.1 (14/09/2017)
- [**closed**] Changelog for v2.0 does not mention breaking changes [#171](https://github.com/broofa/mime/issues/171)
- [**closed**] MIME breaking with 'class' declaration as it is without 'use strict mode' [#170](https://github.com/broofa/mime/issues/170)
---

## v2.0.0 (12/09/2017)
- [**closed**] woff and woff2 [#168](https://github.com/broofa/mime/issues/168)
---

## v1.4.0 (28/08/2017)
- [**closed**] support for ac3 voc files [#159](https://github.com/broofa/mime/issues/159)
- [**closed**] Help understanding change from application/xml to text/xml [#158](https://github.com/broofa/mime/issues/158)
- [**closed**] no longer able to override mimetype [#157](https://github.com/broofa/mime/issues/157)
- [**closed**] application/vnd.adobe.photoshop [#147](https://github.com/broofa/mime/issues/147)
- [**closed**] Directories should appear as something other than application/octet-stream [#135](https://github.com/broofa/mime/issues/135)
- [**closed**] requested features [#131](https://github.com/broofa/mime/issues/131)
- [**closed**] Make types.json loading optional? [#129](https://github.com/broofa/mime/issues/129)
- [**closed**] Cannot find module './types.json' [#120](https://github.com/broofa/mime/issues/120)
- [**V2**] .wav files show up as "audio/x-wav" instead of "audio/x-wave" [#118](https://github.com/broofa/mime/issues/118)
- [**closed**] Don't be a pain in the ass for node community [#108](https://github.com/broofa/mime/issues/108)
- [**closed**] don't make default_type global [#78](https://github.com/broofa/mime/issues/78)
- [**closed**] mime.extension() fails if the content-type is parameterized [#74](https://github.com/broofa/mime/issues/74)
---

## v1.3.6 (11/05/2017)
- [**closed**] .md should be text/markdown as of March 2016 [#154](https://github.com/broofa/mime/issues/154)
- [**closed**] Error while installing mime [#153](https://github.com/broofa/mime/issues/153)
- [**closed**] application/manifest+json [#149](https://github.com/broofa/mime/issues/149)
- [**closed**] Dynamic adaptive streaming over HTTP (DASH) file extension typo [#141](https://github.com/broofa/mime/issues/141)
- [**closed**] charsets image/png undefined [#140](https://github.com/broofa/mime/issues/140)
- [**closed**] Mime-db dependency out of date [#130](https://github.com/broofa/mime/issues/130)
- [**closed**] how to support plist？ [#126](https://github.com/broofa/mime/issues/126)
- [**closed**] how does .types file format look like? [#123](https://github.com/broofa/mime/issues/123)
- [**closed**] Feature: support for expanding MIME patterns [#121](https://github.com/broofa/mime/issues/121)
- [**closed**] DEBUG_MIME doesn't work [#117](https://github.com/broofa/mime/issues/117)
---

## v1.3.4 (06/02/2015)
*No changelog for this release.*
---

## v1.3.3 (06/02/2015)
*No changelog for this release.*
---

## v1.3.1 (05/02/2015)
- [**closed**] Consider adding support for Handlebars .hbs file ending [#111](https://github.com/broofa/mime/issues/111)
- [**closed**] Consider adding support for hjson. [#110](https://github.com/broofa/mime/issues/110)
- [**closed**] Add mime type for Opus audio files [#94](https://github.com/broofa/mime/issues/94)
- [**closed**] Consider making the `Requesting New Types` information more visible [#77](https://github.com/broofa/mime/issues/77)
---

## v1.3.0 (05/02/2015)
- [**closed**] Add common name? [#114](https://github.com/broofa/mime/issues/114)
- [**closed**] application/x-yaml [#104](https://github.com/broofa/mime/issues/104)
- [**closed**] Add mime type for WOFF file format 2.0 [#102](https://github.com/broofa/mime/issues/102)
- [**closed**] application/x-msi for .msi [#99](https://github.com/broofa/mime/issues/99)
- [**closed**] Add mimetype for gettext translation files [#98](https://github.com/broofa/mime/issues/98)
- [**closed**] collaborators [#88](https://github.com/broofa/mime/issues/88)
- [**closed**] getting errot in installation of mime module...any1 can help? [#87](https://github.com/broofa/mime/issues/87)
- [**closed**] should application/json's charset be utf8? [#86](https://github.com/broofa/mime/issues/86)
- [**closed**] Add "license" and "licenses" to package.json [#81](https://github.com/broofa/mime/issues/81)
- [**closed**] lookup with extension-less file on Windows returns wrong type [#68](https://github.com/broofa/mime/issues/68)
---

## v1.2.11 (15/08/2013)
- [**closed**] Update mime.types [#65](https://github.com/broofa/mime/issues/65)
- [**closed**] Publish a new version [#63](https://github.com/broofa/mime/issues/63)
- [**closed**] README should state upfront that "application/octet-stream" is default for unknown extension [#55](https://github.com/broofa/mime/issues/55)
- [**closed**] Suggested improvement to the charset API [#52](https://github.com/broofa/mime/issues/52)
---

## v1.2.10 (25/07/2013)
- [**closed**] Mime type for woff files should be application/font-woff and not application/x-font-woff [#62](https://github.com/broofa/mime/issues/62)
- [**closed**] node.types in conflict with mime.types [#51](https://github.com/broofa/mime/issues/51)
---

## v1.2.9 (17/01/2013)
- [**closed**] Please update "mime" NPM [#49](https://github.com/broofa/mime/issues/49)
- [**closed**] Please add semicolon [#46](https://github.com/broofa/mime/issues/46)
- [**closed**] parse full mime types [#43](https://github.com/broofa/mime/issues/43)
---

## v1.2.8 (10/01/2013)
- [**closed**] /js directory mime is application/javascript. Is it correct? [#47](https://github.com/broofa/mime/issues/47)
- [**closed**] Add mime types for lua code. [#45](https://github.com/broofa/mime/issues/45)
---

## v1.2.7 (19/10/2012)
- [**closed**] cannot install 1.2.7 via npm [#41](https://github.com/broofa/mime/issues/41)
- [**closed**] Transfer ownership to @broofa [#36](https://github.com/broofa/mime/issues/36)
- [**closed**] it's wrong to set charset to UTF-8 for text [#30](https://github.com/broofa/mime/issues/30)
- [**closed**] Allow multiple instances of MIME types container [#27](https://github.com/broofa/mime/issues/27)

---

# iCloud: web-app/node_modules/@google-cloud/storage/node_modules/mime/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/storage/node_modules/mime/README.md
> **Analyzed At:** 2026-06-13T06:32:46.805Z

## Mime
A comprehensive, compact MIME type module.
[![Build Status](https://travis-ci.org/broofa/mime.svg?branch=master)](https://travis-ci.org/broofa/mime)

## NPM
```
npm install mime
```

## Browser
It is recommended that you use a bundler such as
[webpack](https://webpack.github.io/) or [browserify](http://browserify.org/) to
package your code.  However, browser-ready versions are available via
skypack.dev as follows:
```
// Full version

```
```
// "lite" version

```

## Quick Start
For the full version (800+ MIME types, 1,000+ extensions):
```javascript
const mime = require('mime');

mime.getType('txt');                    // ⇨ 'text/plain'
mime.getExtension('text/plain');        // ⇨ 'txt'
```
See [Mime API](#mime-api) below for API details.

## Lite Version
The "lite" version of this module omits vendor-specific (`*/vnd.*`) and
experimental (`*/x-*`) types.  It weighs in at ~2.5KB, compared to 8KB for the
full version.  To load the lite version:
```javascript
const mime = require('mime/lite');
```

## Mime .vs. mime-types .vs. mime-db modules
For those of you wondering about the difference between these [popular] NPM modules,
here's a brief rundown ...
[`mime-db`](https://github.com/jshttp/mime-db) is "the source of
truth" for MIME type information.  It is not an API.  Rather, it is a canonical
dataset of mime type definitions pulled from IANA, Apache, NGINX, and custom mappings
submitted by the Node.js community.
[`mime-types`](https://github.com/jshttp/mime-types) is a thin
wrapper around mime-db that provides an API drop-in compatible(ish) with `mime @ < v1.3.6` API.
`mime` is, as of v2, a self-contained module bundled with a pre-optimized version
of the `mime-db` dataset.  It provides a simplified API with the following characteristics:
* Intelligently resolved type conflicts (See [mime-score](https://github.com/broofa/mime-score) for details)
* Method naming consistent with industry best-practices
* Compact footprint.  E.g. The minified+compressed sizes of the various modules:
Module | Size
--- | ---
`mime-db`  | 18 KB
`mime-types` | same as mime-db
`mime` | 8 KB
`mime/lite` | 2 KB

## Mime API
Both `require('mime')` and `require('mime/lite')` return instances of the MIME
class, documented below.
Note: Inputs to this API are case-insensitive.  Outputs (returned values) will
be lowercase.

## new Mime(typeMap, ... more maps)
Most users of this module will not need to create Mime instances directly.
However if you would like to create custom mappings, you may do so as follows
...
```javascript
// Require Mime class
const Mime = require('mime/Mime');

// Define mime type -> extensions map
const typeMap = {
  'text/abc': ['abc', 'alpha', 'bet'],
  'text/def': ['leppard']
};

// Create and use Mime instance
const myMime = new Mime(typeMap);
myMime.getType('abc');            // ⇨ 'text/abc'
myMime.getExtension('text/def');  // ⇨ 'leppard'
```
If more than one map argument is provided, each map is `define()`ed (see below), in order.

## mime.getType(pathOrExtension)
Get mime type for the given path or extension.  E.g.
```javascript
mime.getType('js');             // ⇨ 'application/javascript'
mime.getType('json');           // ⇨ 'application/json'

mime.getType('txt');            // ⇨ 'text/plain'
mime.getType('dir/text.txt');   // ⇨ 'text/plain'
mime.getType('dir\\text.txt');  // ⇨ 'text/plain'
mime.getType('.text.txt');      // ⇨ 'text/plain'
mime.getType('.txt');           // ⇨ 'text/plain'
```
`null` is returned in cases where an extension is not detected or recognized
```javascript
mime.getType('foo/txt');        // ⇨ null
mime.getType('bogus_type');     // ⇨ null
```

## mime.getExtension(type)
Get extension for the given mime type.  Charset options (often included in
Content-Type headers) are ignored.
```javascript
mime.getExtension('text/plain');               // ⇨ 'txt'
mime.getExtension('application/json');         // ⇨ 'json'
mime.getExtension('text/html; charset=utf8');  // ⇨ 'html'
```

## mime.define(typeMap[, force = false])
Define [more] type mappings.
`typeMap` is a map of type -> extensions, as documented in `new Mime`, above.
By default this method will throw an error if you try to map a type to an
extension that is already assigned to another type.  Passing `true` for the
`force` argument will suppress this behavior (overriding any previous mapping).
```javascript
mime.define({'text/x-abc': ['abc', 'abcd']});

mime.getType('abcd');            // ⇨ 'text/x-abc'
mime.getExtension('text/x-abc')  // ⇨ 'abc'
```

## Command Line
mime [path_or_extension]
E.g.
> mime scripts/jquery.js
application/javascript
----
Markdown generated from [src/README_js.md](src/README_js.md) by [![RunMD Logo](http://i.imgur.com/h0FVyzU.png)](https://github.com/broofa/runmd)

---

# iCloud: web-app/node_modules/@google-cloud/storage/node_modules/gcp-metadata/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/storage/node_modules/gcp-metadata/README.md
> **Analyzed At:** 2026-06-13T06:32:46.813Z

## [GCP Metadata: Node.js Client](https://github.com/googleapis/gcp-metadata)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/gcp-metadata.svg)](https://www.npmjs.org/package/gcp-metadata)
Get the metadata from a Google Cloud Platform environment
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/gcp-metadata/blob/main/CHANGELOG.md).
* [GCP Metadata Node.js Client API Reference][client-docs]
* [GCP Metadata Documentation][product-docs]
* [github.com/googleapis/gcp-metadata](https://github.com/googleapis/gcp-metadata)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Using the client library](#using-the-client-library)
* [Samples](#samples)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install gcp-metadata
```

## Using the client library
```javascript
const gcpMetadata = require('gcp-metadata');

async function quickstart() {
  // check to see if this code can access a metadata server
  const isAvailable = await gcpMetadata.isAvailable();
  console.log(`Is available: ${isAvailable}`);

  // Instance and Project level metadata will only be available if
  // running inside of a Google Cloud compute environment such as
  // Cloud Functions, App Engine, Kubernetes Engine, or Compute Engine.
  // To learn more about the differences between instance and project
  // level metadata, see:
  // https://cloud.google.com/compute/docs/storing-retrieving-metadata#project-instance-metadata
  if (isAvailable) {
    // grab all top level metadata from the service
    const instanceMetadata = await gcpMetadata.instance();
    console.log('Instance metadata:');
    console.log(instanceMetadata);

    // get all project level metadata
    const projectMetadata = await gcpMetadata.project();
    console.log('Project metadata:');
    console.log(projectMetadata);
  }
}

quickstart();

```

## Check to see if the metadata server is available
```js
const isAvailable = await gcpMetadata.isAvailable();
```

## Access all metadata
```js
const data = await gcpMetadata.instance();
console.log(data); // ... All metadata properties
```

## Access specific properties
```js
const data = await gcpMetadata.instance('hostname');
console.log(data); // ...Instance hostname
const projectId = await gcpMetadata.project('project-id');
console.log(projectId); // ...Project ID of the running instance
```

## Access nested properties with the relative path
```js
const data = await gcpMetadata.instance('service-accounts/default/email');
console.log(data); // ...Email address of the Compute identity service account
```

## Access specific properties with query parameters
```js
const data = await gcpMetadata.instance({
  property: 'tags',
  params: { alt: 'text' }
});
console.log(data) // ...Tags as newline-delimited list
```

## Access with custom headers
```js
await gcpMetadata.instance({
  headers: { 'no-trace': '1' }
}); // ...Request is untraced
```

## Take care with large number valued properties
In some cases number valued properties returned by the Metadata Service may be
too large to be representable as JavaScript numbers. In such cases we return
those values as `BigNumber` objects (from the [bignumber.js](https://github.com/MikeMcl/bignumber.js) library). Numbers
that fit within the JavaScript number range will be returned as normal number
values.
```js
const id = await gcpMetadata.instance('id');
console.log(id)  // ... BigNumber { s: 1, e: 18, c: [ 45200, 31799277581759 ] }
console.log(id.toString()) // ... 4520031799277581759
```

## Environment variables
* `GCE_METADATA_HOST`: provide an alternate host or IP to perform lookup against (useful, for example, you're connecting through a custom proxy server).
For example:
  ```
  export GCE_METADATA_HOST='169.254.169.254'
```
* `DETECT_GCP_RETRIES`: number representing number of retries that should be attempted on metadata lookup.
* `DEBUG_AUTH`: emit debugging logs
* `METADATA_SERVER_DETECTION`: configure desired metadata server availability check behavior.
* `assume-present`: don't try to ping the metadata server, but assume it's present
* `none`: don't try to ping the metadata server, but don't try to use it either
* `bios-only`: treat the result of a BIOS probe as canonical (don't fall back to pinging)
* `ping-only`: skip the BIOS probe, and go straight to pinging

## Samples
Samples are in the [`samples/`](https://github.com/googleapis/gcp-metadata/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.
| Sample                      | Source Code                       | Try it |
| --------------------------- | --------------------------------- | ------ |
| Quickstart | [source code](https://github.com/googleapis/gcp-metadata/blob/main/samples/quickstart.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/gcp-metadata&page=editor&open_in_editor=samples/quickstart.js,samples/README.md) |
The [GCP Metadata Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install gcp-metadata@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/gcp-metadata/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/gcp-metadata/blob/main/LICENSE)
[client-docs]: https://cloud.google.com/nodejs/docs/reference/gcp-metadata/latest
[product-docs]: https://cloud.google.com/compute/docs/storing-retrieving-metadata
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/external/set-up-adc-local

---

# iCloud: web-app/node_modules/@google-cloud/storage/node_modules/gaxios/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/storage/node_modules/gaxios/README.md
> **Analyzed At:** 2026-06-13T06:32:46.819Z

## gaxios
[![npm version](https://img.shields.io/npm/v/gaxios.svg)](https://www.npmjs.org/package/gaxios)
[![codecov](https://codecov.io/gh/googleapis/gaxios/branch/master/graph/badge.svg)](https://codecov.io/gh/googleapis/gaxios)
[![Code Style: Google](https://img.shields.io/badge/code%20style-google-blueviolet.svg)](https://github.com/google/gts)
> An HTTP request client that provides an `axios` like interface over top of `node-fetch`.

## Install
```sh
$ npm install gaxios
```

## Example
```js
const {request} = require('gaxios');
const res = await request({
  url: 'https://www.googleapis.com/discovery/v1/apis/',
});
```

## Setting Defaults
Gaxios supports setting default properties both on the default instance, and on additional instances. This is often useful when making many requests to the same domain with the same base settings. For example:
```js
const gaxios = require('gaxios');
gaxios.instance.defaults = {
  baseURL: 'https://example.com'
  headers: {
    Authorization: 'SOME_TOKEN'
  }
}
gaxios.request({url: '/data'}).then(...);
```
Note that setting default values will take precedence
over other authentication methods, i.e., application default credentials.

## Request Options
```ts
interface GaxiosOptions = {
  // The url to which the request should be sent.  Required.
  url: string,

  // The HTTP method to use for the request.  Defaults to `GET`.
  method: 'GET',

  // The base Url to use for the request. Prepended to the `url` property above.
  baseURL: 'https://example.com';

  // The HTTP methods to be sent with the request.
  headers: { 'some': 'header' },

  // The data to send in the body of the request. Data objects will be
  // serialized as JSON.
  //
  // Note: if you would like to provide a Content-Type header other than
  // application/json you you must provide a string or readable stream, rather
  // than an object:
  // data: JSON.stringify({some: 'data'})
  // data: fs.readFile('./some-data.jpeg')
  data: {
    some: 'data'
  },

  // The max size of the http response content in bytes allowed.
  // Defaults to `0`, which is the same as unset.
  maxContentLength: 2000,

  // The max number of HTTP redirects to follow.
  // Defaults to 100.
  maxRedirects: 100,

  // The querystring parameters that will be encoded using `qs` and
  // appended to the url
  params: {
    querystring: 'parameters'
  },

  // By default, we use the `querystring` package in node core to serialize
  // querystring parameters.  You can override that and provide your
  // own implementation.
  paramsSerializer: (params) => {
    return qs.stringify(params);
  },

  // The timeout for the HTTP request in milliseconds. Defaults to 0.
  timeout: 1000,

  // Optional method to override making the actual HTTP request. Useful
  // for writing tests and instrumentation
  adapter?: async (options, defaultAdapter) => {
    const res = await defaultAdapter(options);
    res.data = {
      ...res.data,
      extraProperty: 'your extra property',
    };
    return res;
  };

  // The expected return type of the request.  Options are:
  // json | stream | blob | arraybuffer | text | unknown
  // Defaults to `unknown`.
  responseType: 'unknown',

  // The node.js http agent to use for the request.
  agent: someHttpsAgent,

  // Custom function to determine if the response is valid based on the
  // status code.  Defaults to (>= 200 && < 300)
  validateStatus: (status: number) => true,

  // Implementation of `fetch` to use when making the API call. By default,
  // will use the browser context if available, and fall back to `node-fetch`
  // in node.js otherwise.
  fetchImplementation?: typeof fetch;

  // Configuration for retrying of requests.
  retryConfig: {
    // The number of times to retry the request.  Defaults to 3.
    retry?: number;

    // The number of retries already attempted.
    currentRetryAttempt?: number;

    // The HTTP Methods that will be automatically retried.
    // Defaults to ['GET','PUT','HEAD','OPTIONS','DELETE']
    httpMethodsToRetry?: string[];

    // The HTTP response status codes that will automatically be retried.
    // Defaults to: [[100, 199], [408, 408], [429, 429], [500, 599]]
    statusCodesToRetry?: number[][];

    // Function to invoke when a retry attempt is made.
    onRetryAttempt?: (err: GaxiosError) => Promise<void> | void;

    // Function to invoke which determines if you should retry
    shouldRetry?: (err: GaxiosError) => Promise<boolean> | boolean;

    // When there is no response, the number of retries to attempt. Defaults to 2.
    noResponseRetries?: number;

    // The amount of time to initially delay the retry, in ms.  Defaults to 100ms.
    retryDelay?: number;
  },

  // Enables default configuration for retries.
  retry: boolean,

  // Cancelling a request requires the `abort-controller` library.
  // See https://github.com/bitinn/node-fetch#request-cancellation-with-abortsignal
  signal?: AbortSignal

  /**
   * A collection of parts to send as a `Content-Type: multipart/related` request.
   */
  multipart?: GaxiosMultipartOptions;

  /**
   * An optional proxy to use for requests.
   * Available via `process.env.HTTP_PROXY` and `process.env.HTTPS_PROXY` as well - with a preference for the this config option when multiple are available.
   * The `agent` option overrides this.
   *
   * @see {@link GaxiosOptions.noProxy}
   * @see {@link GaxiosOptions.agent}
   */
  proxy?: string | URL;
  /**
   * A list for excluding traffic for proxies.
   * Available via `process.env.NO_PROXY` as well as a common-separated list of strings - merged with any local `noProxy` rules.
   *
   * - When provided a string, it is matched by
   *   - Wildcard `*.` and `.` matching are available. (e.g. `.example.com` or `*.example.com`)
   * - When provided a URL, it is matched by the `.origin` property.
   *   - For example, requesting `https://example.com` with the following `noProxy`s would result in a no proxy use:
   *     - new URL('https://example.com')
   *     - new URL('https://example.com:443')
   *   - The following would be used with a proxy:
   *     - new URL('http://example.com:80')
   *     - new URL('https://example.com:8443')
   * - When provided a regular expression it is used to match the stringified URL
   *
   * @see {@link GaxiosOptions.proxy}
   */
  noProxy?: (string | URL | RegExp)[];

  /**
   * An experimental, customizable error redactor.
   *
   * Set `false` to disable.
   *
   * @remarks
   *
   * This does not replace the requirement for an active Data Loss Prevention (DLP) provider. For DLP suggestions, see:
   * - https://cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data#dlp_deidentify_replace_infotype-nodejs
   * - https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets
   *
   * @experimental
   */
  errorRedactor?: typeof defaultErrorRedactor | false;
}
```

## License
[Apache-2.0](https://github.com/googleapis/gaxios/blob/master/LICENSE)

---

# iCloud: web-app/node_modules/@google-cloud/storage/node_modules/gaxios/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@google-cloud/storage/node_modules/gaxios/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.827Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@google-cloud/promisify/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@google-cloud/promisify/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.857Z

## Changelog
[npm history][1]
[1]: https://www.npmjs.com/package/nodejs-promisify?activeTab=versions

## ⚠ BREAKING CHANGES
* upgrade to Node 14 ([#325](https://github.com/googleapis/nodejs-promisify/issues/325))

## Miscellaneous Chores
* Upgrade to Node 14 ([#325](https://github.com/googleapis/nodejs-promisify/issues/325)) ([57d02c1](https://github.com/googleapis/nodejs-promisify/commit/57d02c1c23c65d63131bb99c07919ff80e5604cd))

## Bug Fixes
* remove pip install statements ([#1546](https://github.com/googleapis/nodejs-promisify/issues/1546)) ([#310](https://github.com/googleapis/nodejs-promisify/issues/310)) ([c7c6883](https://github.com/googleapis/nodejs-promisify/commit/c7c688389de72ddc0181b19bceee2d95eacd3d96))

## ⚠ BREAKING CHANGES
* drop node 10 from engines list, update typescript to 4.6.3 (#300)

## Build System
* drop node 10 from engines list, update typescript to 4.6.3 ([#300](https://github.com/googleapis/nodejs-promisify/issues/300)) ([fed2f14](https://github.com/googleapis/nodejs-promisify/commit/fed2f145a5256c939eb66b85a5c7c48332b8841d))

## Bug Fixes
* **build:** switch primary branch to main ([#270](https://www.github.com/googleapis/nodejs-promisify/issues/270)) ([11242f7](https://www.github.com/googleapis/nodejs-promisify/commit/11242f7f76e170dae7a429f8d4064bf33be9bb3f))

## Bug Fixes
* allow excluding accessor methods ([#228](https://www.github.com/googleapis/nodejs-promisify/issues/228)) ([114d8bc](https://www.github.com/googleapis/nodejs-promisify/commit/114d8bcef7093bdfda195a15e0c2f376195fd3fc))

## Bug Fixes
* update node issue template ([#204](https://www.github.com/googleapis/nodejs-promisify/issues/204)) ([a2ba8d8](https://www.github.com/googleapis/nodejs-promisify/commit/a2ba8d8e45ef03d093d987292a467696745fc9fd))

## Bug Fixes
* apache license URL ([#468](https://www.github.com/googleapis/nodejs-promisify/issues/468)) ([#191](https://www.github.com/googleapis/nodejs-promisify/issues/191)) ([0edc724](https://www.github.com/googleapis/nodejs-promisify/commit/0edc7246c53d25d9dd220b813561bcee97250783))

## ⚠ BREAKING CHANGES
* update to latest version of gts/typescript (#183)
* drop Node 8 from engines field (#184)

## Features
* drop Node 8 from engines field ([#184](https://www.github.com/googleapis/nodejs-promisify/issues/184)) ([7e6d3c5](https://www.github.com/googleapis/nodejs-promisify/commit/7e6d3c54066d89530ed25c7f9722efd252f43fb8))

## Build System
* update to latest version of gts/typescript ([#183](https://www.github.com/googleapis/nodejs-promisify/issues/183)) ([9c3ed12](https://www.github.com/googleapis/nodejs-promisify/commit/9c3ed12c12f4bb1e17af7440c6371c4cefddcd59))

## Bug Fixes
* **deps:** pin TypeScript below 3.7.0 ([e48750e](https://www.github.com/googleapis/nodejs-promisify/commit/e48750ef96aa20eb3a2b73fe2f062d04430468a7))

## Bug Fixes
* **docs:** add jsdoc-region-tag plugin ([#146](https://www.github.com/googleapis/nodejs-promisify/issues/146)) ([ff0ee74](https://www.github.com/googleapis/nodejs-promisify/commit/ff0ee7408f50e8f7147b8ccf7e10337aa5920076))

## Bug Fixes
* **docs:** link to reference docs section on googleapis.dev ([#128](https://www.github.com/googleapis/nodejs-promisify/issues/128)) ([5a8bd90](https://www.github.com/googleapis/nodejs-promisify/commit/5a8bd90))

## Bug Fixes
* **docs:** move to new client docs URL ([#124](https://www.github.com/googleapis/nodejs-promisify/issues/124)) ([34d18cd](https://www.github.com/googleapis/nodejs-promisify/commit/34d18cd))

## Build System
* upgrade engines field to >=8.10.0 ([#108](https://www.github.com/googleapis/nodejs-promisify/issues/108)) ([78ab89c](https://www.github.com/googleapis/nodejs-promisify/commit/78ab89c))

## BREAKING CHANGES
* upgrade engines field to >=8.10.0 (#108)

## v0.4.0
02-12-2019 19:44 PST

## New features
- feat: add callbackify() and callbackifyAll() methods ([#82](https://github.com/googleapis/nodejs-promisify/pull/82))

## Documentation
- docs: update contributing path in README ([#86](https://github.com/googleapis/nodejs-promisify/pull/86))
- chore: move CONTRIBUTING.md to root ([#85](https://github.com/googleapis/nodejs-promisify/pull/85))
- docs: add lint/fix example to contributing guide ([#83](https://github.com/googleapis/nodejs-promisify/pull/83))

## Internal / Testing Changes
- build: create docs test npm scripts ([#88](https://github.com/googleapis/nodejs-promisify/pull/88))
- build: test using @grpc/grpc-js in CI ([#87](https://github.com/googleapis/nodejs-promisify/pull/87))
- build: ignore googleapis.com in doc link check ([#81](https://github.com/googleapis/nodejs-promisify/pull/81))
- build: check broken links in generated docs ([#79](https://github.com/googleapis/nodejs-promisify/pull/79))
- chore(deps): update dependency @types/sinon to v7 ([#78](https://github.com/googleapis/nodejs-promisify/pull/78))
- chore(build): inject yoshi automation key ([#77](https://github.com/googleapis/nodejs-promisify/pull/77))
- chore: update nyc and eslint configs ([#76](https://github.com/googleapis/nodejs-promisify/pull/76))
- chore: fix publish.sh permission +x ([#74](https://github.com/googleapis/nodejs-promisify/pull/74))
- fix(build): fix Kokoro release script ([#73](https://github.com/googleapis/nodejs-promisify/pull/73))
- build: add Kokoro configs for autorelease ([#72](https://github.com/googleapis/nodejs-promisify/pull/72))
- chore: always nyc report before calling codecov ([#69](https://github.com/googleapis/nodejs-promisify/pull/69))
- chore: nyc ignore build/test by default ([#68](https://github.com/googleapis/nodejs-promisify/pull/68))
- chore(build): update prettier config ([#66](https://github.com/googleapis/nodejs-promisify/pull/66))
- fix: get the build passing ([#65](https://github.com/googleapis/nodejs-promisify/pull/65))
- chore: update license file ([#64](https://github.com/googleapis/nodejs-promisify/pull/64))
- fix(build): fix system key decryption ([#60](https://github.com/googleapis/nodejs-promisify/pull/60))
- chore(deps): update dependency @types/sinon to v5.0.7 ([#58](https://github.com/googleapis/nodejs-promisify/pull/58))
- fix: Pin @types/sinon to last compatible version ([#57](https://github.com/googleapis/nodejs-promisify/pull/57))
- chore: add synth.metadata
- chore(deps): update dependency gts to ^0.9.0 ([#54](https://github.com/googleapis/nodejs-promisify/pull/54))
- chore: update eslintignore config ([#53](https://github.com/googleapis/nodejs-promisify/pull/53))
- chore: use latest npm on Windows ([#52](https://github.com/googleapis/nodejs-promisify/pull/52))
- chore: update CircleCI config ([#51](https://github.com/googleapis/nodejs-promisify/pull/51))
- chore: include build in eslintignore ([#48](https://github.com/googleapis/nodejs-promisify/pull/48))
- chore: update issue templates ([#44](https://github.com/googleapis/nodejs-promisify/pull/44))
- chore: remove old issue template ([#42](https://github.com/googleapis/nodejs-promisify/pull/42))
- build: run tests on node11 ([#41](https://github.com/googleapis/nodejs-promisify/pull/41))
- chores(build): do not collect sponge.xml from windows builds ([#40](https://github.com/googleapis/nodejs-promisify/pull/40))
- chores(build): run codecov on continuous builds ([#39](https://github.com/googleapis/nodejs-promisify/pull/39))
- chore: update new issue template ([#38](https://github.com/googleapis/nodejs-promisify/pull/38))
- chore(deps): update dependency sinon to v7 ([#33](https://github.com/googleapis/nodejs-promisify/pull/33))
- build: fix codecov uploading on Kokoro ([#34](https://github.com/googleapis/nodejs-promisify/pull/34))
- Update kokoro config ([#30](https://github.com/googleapis/nodejs-promisify/pull/30))
- Update CI config ([#28](https://github.com/googleapis/nodejs-promisify/pull/28))
- Don't publish sourcemaps ([#26](https://github.com/googleapis/nodejs-promisify/pull/26))
- Update kokoro config ([#24](https://github.com/googleapis/nodejs-promisify/pull/24))
- test: remove appveyor config ([#23](https://github.com/googleapis/nodejs-promisify/pull/23))
- Update CI config ([#22](https://github.com/googleapis/nodejs-promisify/pull/22))
- Enable prefer-const in the eslint config ([#21](https://github.com/googleapis/nodejs-promisify/pull/21))
- Enable no-var in eslint ([#19](https://github.com/googleapis/nodejs-promisify/pull/19))
- Update CI config ([#18](https://github.com/googleapis/nodejs-promisify/pull/18))

## Internal / Testing Changes
- Add synth script and update CI (#14)
- chore(deps): update dependency nyc to v13 (#12)
- chore: ignore package-lock.json (#11)
- chore(deps): lock file maintenance (#10)
- chore: update renovate config (#9)
- remove that whitespace (#8)
- chore(deps): lock file maintenance (#7)
- chore(deps): update dependency typescript to v3 (#6)
- chore: assert.deelEqual => assert.deepStrictEqual (#5)
- chore: move mocha options to mocha.opts (#4)
- chore(deps): update dependency gts to ^0.8.0 (#1)
- chore(deps): lock file maintenance (#3)
- chore(deps): lock file maintenance (#2)

---

# iCloud: web-app/node_modules/@google-cloud/promisify/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/promisify/README.md
> **Analyzed At:** 2026-06-13T06:32:46.861Z

## [Google Cloud Common Promisify: Node.js Client](https://github.com/googleapis/nodejs-promisify)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/@google-cloud/promisify.svg)](https://www.npmjs.org/package/@google-cloud/promisify)
A simple utility for promisifying functions and classes.
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/nodejs-promisify/blob/main/CHANGELOG.md).
* [Google Cloud Common Promisify Node.js Client API Reference][client-docs]
* [github.com/googleapis/nodejs-promisify](https://github.com/googleapis/nodejs-promisify)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Using the client library](#using-the-client-library)
* [Samples](#samples)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install @google-cloud/promisify
```

## Using the client library
```javascript
const {promisify} = require('@google-cloud/promisify');

/**
 * This is a very basic example function that accepts a callback.
 */
function someCallbackFunction(name, callback) {
  if (!name) {
    callback(new Error('Name is required!'));
  } else {
    callback(null, `Well hello there, ${name}!`);
  }
}

// let's promisify it!
const somePromiseFunction = promisify(someCallbackFunction);

async function quickstart() {
  // now we can just `await` the function to use it like a promisified method
  const [result] = await somePromiseFunction('nodestronaut');
  console.log(result);
}
quickstart();

```
It's unlikely you will need to install this package directly, as it will be
installed as a dependency when you install other `@google-cloud` packages.

## Samples
Samples are in the [`samples/`](https://github.com/googleapis/nodejs-promisify/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.
| Sample                      | Source Code                       | Try it |
| --------------------------- | --------------------------------- | ------ |
| Quickstart | [source code](https://github.com/googleapis/nodejs-promisify/blob/main/samples/quickstart.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-promisify&page=editor&open_in_editor=samples/quickstart.js,samples/README.md) |
The [Google Cloud Common Promisify Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install @google-cloud/promisify@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-promisify/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/nodejs-promisify/blob/main/LICENSE)
[client-docs]: https://googleapis.dev/nodejs/promisify/latest
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/getting-started

---

# iCloud: web-app/node_modules/@google-cloud/projectify/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@google-cloud/projectify/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.867Z

## Changelog
[npm history][1]
[1]: https://www.npmjs.com/package/@google-cloud/projectify?activeTab=versions

## ⚠ BREAKING CHANGES
* upgrade to Node 14 ([#318](https://github.com/googleapis/nodejs-projectify/issues/318))

## Bug Fixes
* Remove pip install statements ([#1546](https://github.com/googleapis/nodejs-projectify/issues/1546)) ([#304](https://github.com/googleapis/nodejs-projectify/issues/304)) ([94cfff6](https://github.com/googleapis/nodejs-projectify/commit/94cfff665b7c6b8916b5c59e1c7a3cca7ff29303))

## Miscellaneous Chores
* Upgrade to Node 14 ([#318](https://github.com/googleapis/nodejs-projectify/issues/318)) ([6e9da4d](https://github.com/googleapis/nodejs-projectify/commit/6e9da4db77fab7ed6876e755a72156960b376d57))

## ⚠ BREAKING CHANGES
* update library to use Node 12 (#299)

## Build System
* update library to use Node 12 ([#299](https://github.com/googleapis/nodejs-projectify/issues/299)) ([83b63ca](https://github.com/googleapis/nodejs-projectify/commit/83b63ca8cb89086a8535a9fc8abd39e95f0cecd4))

## Bug Fixes
* **build:** switch primary branch to main ([#267](https://www.github.com/googleapis/nodejs-projectify/issues/267)) ([9e8d6e4](https://www.github.com/googleapis/nodejs-projectify/commit/9e8d6e48c080806b42164d7be0bd11197996f245))

## Features
* add `gcf-owl-bot[bot]` to `ignoreAuthors` ([#245](https://www.github.com/googleapis/nodejs-projectify/issues/245)) ([30f0499](https://www.github.com/googleapis/nodejs-projectify/commit/30f0499ade5f140774c3aa672b44fd3538e72309))

## Bug Fixes
* update node issue template ([#197](https://www.github.com/googleapis/nodejs-projectify/issues/197)) ([3406f2a](https://www.github.com/googleapis/nodejs-projectify/commit/3406f2aa431ed04541585b63c330c04270c602aa))

## ⚠ BREAKING CHANGES
* typescript@3.7 introduced some breaking changes
* drop Node 8 from engines field (#172)

## Features
* drop Node 8 from engines field ([#172](https://www.github.com/googleapis/nodejs-projectify/issues/172)) ([3eac424](https://www.github.com/googleapis/nodejs-projectify/commit/3eac424bfb1ee47144a77888dc68db687988945e))

## Build System
* update to latest version of gts/typescript ([#171](https://www.github.com/googleapis/nodejs-projectify/issues/171)) ([30f90cc](https://www.github.com/googleapis/nodejs-projectify/commit/30f90cc172da6ed9394da91869556bf5eef42434))

## Bug Fixes
* **publish:** publication failed to reach npm ([#141](https://www.github.com/googleapis/nodejs-projectify/issues/141)) ([5406ba5](https://www.github.com/googleapis/nodejs-projectify/commit/5406ba5e1d43a228a19072023c1baebce34190af))

## Bug Fixes
* **deps:** pin TypeScript below 3.7.0 ([6c95307](https://www.github.com/googleapis/nodejs-projectify/commit/6c953070139a77d30c4ce5b7dee1443874046906))

## Bug Fixes
* **docs:** add jsdoc-region-tag plugin ([#135](https://www.github.com/googleapis/nodejs-projectify/issues/135)) ([59301e7](https://www.github.com/googleapis/nodejs-projectify/commit/59301e7cfa855add4894dd9c46870e61fffa7413))

## Bug Fixes
* **docs:** link to reference docs section on googleapis.dev ([#119](https://www.github.com/googleapis/nodejs-projectify/issues/119)) ([90a009f](https://www.github.com/googleapis/nodejs-projectify/commit/90a009f))

## Build System
* upgrade engines field to >=8.10.0 ([#103](https://www.github.com/googleapis/nodejs-projectify/issues/103)) ([0149650](https://www.github.com/googleapis/nodejs-projectify/commit/0149650))

## BREAKING CHANGES
* upgrade engines field to >=8.10.0 (#103)

## v0.3.3
03-12-2019 12:27 PDT
This patch release contains a few updates to the docs.  That's all!

## Documentation
- docs: update links in contrib guide ([#86](https://github.com/googleapis/nodejs-projectify/pull/86))
- docs: update contributing path in README ([#82](https://github.com/googleapis/nodejs-projectify/pull/82))
- docs: move CONTRIBUTING.md to root ([#81](https://github.com/googleapis/nodejs-projectify/pull/81))
- docs: add lint/fix example to contributing guide ([#79](https://github.com/googleapis/nodejs-projectify/pull/79))

## Internal / Testing Changes
- build: Add docuploader credentials to node publish jobs ([#90](https://github.com/googleapis/nodejs-projectify/pull/90))
- build: use node10 to run samples-test, system-test etc ([#89](https://github.com/googleapis/nodejs-projectify/pull/89))
- build: update release configuration
- chore(deps): update dependency mocha to v6
- build: use linkinator for docs test ([#85](https://github.com/googleapis/nodejs-projectify/pull/85))
- build: create docs test npm scripts ([#84](https://github.com/googleapis/nodejs-projectify/pull/84))
- build: test using @grpc/grpc-js in CI ([#83](https://github.com/googleapis/nodejs-projectify/pull/83))
- build: ignore googleapis.com in doc link check ([#78](https://github.com/googleapis/nodejs-projectify/pull/78))
- build: check for 404s in the docs ([#77](https://github.com/googleapis/nodejs-projectify/pull/77))
- chore(build): inject yoshi automation key ([#75](https://github.com/googleapis/nodejs-projectify/pull/75))
- chore: update nyc and eslint configs ([#74](https://github.com/googleapis/nodejs-projectify/pull/74))
- chore: fix publish.sh permission +x ([#72](https://github.com/googleapis/nodejs-projectify/pull/72))
- fix(build): fix Kokoro release script ([#71](https://github.com/googleapis/nodejs-projectify/pull/71))
- build: add Kokoro configs for autorelease ([#70](https://github.com/googleapis/nodejs-projectify/pull/70))
- chore: always nyc report before calling codecov ([#67](https://github.com/googleapis/nodejs-projectify/pull/67))
- chore: nyc ignore build/test by default ([#66](https://github.com/googleapis/nodejs-projectify/pull/66))
- chore(build): update prettier config ([#64](https://github.com/googleapis/nodejs-projectify/pull/64))
- chore: update license file ([#63](https://github.com/googleapis/nodejs-projectify/pull/63))
- fix(build): fix system key decryption ([#59](https://github.com/googleapis/nodejs-projectify/pull/59))
- chore: add synth.metadata

## Bug fixes
- fix: do not replace projectId on stream objects ([#53](https://github.com/googleapis/nodejs-projectify/pull/53))

## Dependencies
- chore(deps): update dependency gts to ^0.9.0 ([#52](https://github.com/googleapis/nodejs-projectify/pull/52))

## Internal / Testing Changes
- chore: update eslintignore config ([#51](https://github.com/googleapis/nodejs-projectify/pull/51))
- chore: use latest npm on Windows ([#50](https://github.com/googleapis/nodejs-projectify/pull/50))
- chore: update CircleCI config ([#49](https://github.com/googleapis/nodejs-projectify/pull/49))
- chore: include build in eslintignore ([#46](https://github.com/googleapis/nodejs-projectify/pull/46))

## Implementation Changes
- fix: replaceProjectId should not fail when passed a Buffer ([#43](https://github.com/googleapis/nodejs-projectify/pull/43))

## Dependencies
- chore(deps): update dependency nyc to v13 ([#13](https://github.com/googleapis/nodejs-projectify/pull/13))
- chore(deps): lock file maintenance ([#11](https://github.com/googleapis/nodejs-projectify/pull/11))
- chore(deps): lock file maintenance ([#8](https://github.com/googleapis/nodejs-projectify/pull/8))
- chore(deps): update dependency typescript to v3 ([#7](https://github.com/googleapis/nodejs-projectify/pull/7))
- chore(deps): update dependency gts to ^0.8.0 ([#2](https://github.com/googleapis/nodejs-projectify/pull/2))
- chore(deps): lock file maintenance ([#4](https://github.com/googleapis/nodejs-projectify/pull/4))
- chore(deps): lock file maintenance ([#3](https://github.com/googleapis/nodejs-projectify/pull/3))

## Internal / Testing Changes
- chore: update issue templates ([#40](https://github.com/googleapis/nodejs-projectify/pull/40))
- chore: remove old issue template ([#38](https://github.com/googleapis/nodejs-projectify/pull/38))
- build: run tests on node11 ([#37](https://github.com/googleapis/nodejs-projectify/pull/37))
- chores(build): run codecov on continuous builds ([#34](https://github.com/googleapis/nodejs-projectify/pull/34))
- chores(build): do not collect sponge.xml from windows builds ([#35](https://github.com/googleapis/nodejs-projectify/pull/35))
- chore: update new issue template ([#33](https://github.com/googleapis/nodejs-projectify/pull/33))
- build: fix codecov uploading on Kokoro ([#30](https://github.com/googleapis/nodejs-projectify/pull/30))
- Update kokoro config ([#28](https://github.com/googleapis/nodejs-projectify/pull/28))
- Update CI config ([#26](https://github.com/googleapis/nodejs-projectify/pull/26))
- Don't publish sourcemaps ([#24](https://github.com/googleapis/nodejs-projectify/pull/24))
- build: prevent system/sample-test from leaking credentials
- Update kokoro config ([#22](https://github.com/googleapis/nodejs-projectify/pull/22))
- test: remove appveyor config ([#21](https://github.com/googleapis/nodejs-projectify/pull/21))
- Update CI config ([#20](https://github.com/googleapis/nodejs-projectify/pull/20))
- Enable prefer-const in the eslint config ([#19](https://github.com/googleapis/nodejs-projectify/pull/19))
- Enable no-var in eslint ([#18](https://github.com/googleapis/nodejs-projectify/pull/18))
- Update CI config ([#17](https://github.com/googleapis/nodejs-projectify/pull/17))
- Add synth and update CI config ([#15](https://github.com/googleapis/nodejs-projectify/pull/15))
- chore: ignore package-lock.json ([#12](https://github.com/googleapis/nodejs-projectify/pull/12))
- chore: update renovate config ([#10](https://github.com/googleapis/nodejs-projectify/pull/10))
- remove that whitespace ([#9](https://github.com/googleapis/nodejs-projectify/pull/9))
- chore: assert.deelEqual => assert.deepStrictEqual ([#6](https://github.com/googleapis/nodejs-projectify/pull/6))
- chore: move mocha options to mocha.opts ([#5](https://github.com/googleapis/nodejs-projectify/pull/5))

---

# iCloud: web-app/node_modules/@google-cloud/projectify/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/projectify/README.md
> **Analyzed At:** 2026-06-13T06:32:46.871Z

## [Google Cloud Common Projectify: Node.js Client](https://github.com/googleapis/nodejs-projectify)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/@google-cloud/projectify.svg)](https://www.npmjs.org/package/@google-cloud/projectify)
A simple utility for replacing the projectid token in objects.
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/nodejs-projectify/blob/main/CHANGELOG.md).
* [Google Cloud Common Projectify Node.js Client API Reference][client-docs]
* [github.com/googleapis/nodejs-projectify](https://github.com/googleapis/nodejs-projectify)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Using the client library](#using-the-client-library)
* [Samples](#samples)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install @google-cloud/projectify
```

## Using the client library
```javascript
const {replaceProjectIdToken} = require('@google-cloud/projectify');
const options = {
  projectId: '{{projectId}}',
};
replaceProjectIdToken(options, 'fake-project-id');

```

## Samples
Samples are in the [`samples/`](https://github.com/googleapis/nodejs-projectify/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.
| Sample                      | Source Code                       | Try it |
| --------------------------- | --------------------------------- | ------ |
| Quickstart | [source code](https://github.com/googleapis/nodejs-projectify/blob/main/samples/quickstart.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-projectify&page=editor&open_in_editor=samples/quickstart.js,samples/README.md) |
The [Google Cloud Common Projectify Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install @google-cloud/projectify@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-projectify/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/nodejs-projectify/blob/main/LICENSE)
[client-docs]: https://cloud.google.com/nodejs/docs/reference/projectify/latest
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/getting-started

---

# iCloud: web-app/node_modules/@google-cloud/precise-date/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@google-cloud/precise-date/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.878Z

## Changelog
[npm history][1]
[1]: https://www.npmjs.com/package/@google-cloud/precise-date?activeTab=versions

## ⚠ BREAKING CHANGES
* upgrade to Node 14 ([#235](https://github.com/googleapis/nodejs-precise-date/issues/235))

## Miscellaneous Chores
* Upgrade to Node 14 ([#235](https://github.com/googleapis/nodejs-precise-date/issues/235)) ([730c500](https://github.com/googleapis/nodejs-precise-date/commit/730c50022954bf4c9fbef9b6fa357266859660c3))

## Bug Fixes
* remove pip install statements ([#1546](https://github.com/googleapis/nodejs-precise-date/issues/1546)) ([#219](https://github.com/googleapis/nodejs-precise-date/issues/219)) ([8a81e94](https://github.com/googleapis/nodejs-precise-date/commit/8a81e94c0430ff801978bedf8827f2b978f352fb))

## ⚠ BREAKING CHANGES
* update library to use Node 12 (#215)

## Build System
* update library to use Node 12 ([#215](https://github.com/googleapis/nodejs-precise-date/issues/215)) ([209a3d1](https://github.com/googleapis/nodejs-precise-date/commit/209a3d1a8a0bf4841c695c6fffe5ef663857161f))

## Bug Fixes
* **build:** switch primary branch to main ([#186](https://www.github.com/googleapis/nodejs-precise-date/issues/186)) ([aaa4044](https://www.github.com/googleapis/nodejs-precise-date/commit/aaa4044fdf81aaeee8b62e00f71abd9b9d1a0827))

## Bug Fixes
* move gitattributes files to node templates ([#130](https://www.github.com/googleapis/nodejs-precise-date/issues/130)) ([d4de5dd](https://www.github.com/googleapis/nodejs-precise-date/commit/d4de5dd73a4aec17c4c8c1e8a95335e1d3e656e5))

## Bug Fixes
* update node issue template ([#117](https://www.github.com/googleapis/nodejs-precise-date/issues/117)) ([ae4d6a1](https://www.github.com/googleapis/nodejs-precise-date/commit/ae4d6a1d07e5327d25eda58e709f3d547ffca607))

## Bug Fixes
* apache license URL ([#468](https://www.github.com/googleapis/nodejs-precise-date/issues/468)) ([#103](https://www.github.com/googleapis/nodejs-precise-date/issues/103)) ([efdc8c6](https://www.github.com/googleapis/nodejs-precise-date/commit/efdc8c6a1e5f8b35da4c5e6ff03fa1f2be6c790f))

## ⚠ BREAKING CHANGES
* **dep:** upgrade typescript/gts (#97)
* **dep:** deprecate Node 8 to 10 (#92)

## Miscellaneous Chores
* **dep:** deprecate Node 8 to 10 ([#92](https://www.github.com/googleapis/nodejs-precise-date/issues/92)) ([75ca209](https://www.github.com/googleapis/nodejs-precise-date/commit/75ca209b49abcba8efcbc401b270ac1346874647))
* **dep:** upgrade typescript/gts ([#97](https://www.github.com/googleapis/nodejs-precise-date/issues/97)) ([59ca2de](https://www.github.com/googleapis/nodejs-precise-date/commit/59ca2de8f6da249808dddebdba3961e59140d06d))

## Bug Fixes
* **deps:** pin TypeScript below 3.7.0 ([c4aef9c](https://www.github.com/googleapis/nodejs-precise-date/commit/c4aef9c42cfab91c4701891d12a7b7118e3ba76c))

## Bug Fixes
* **docs:** add jsdoc-region-tag plugin ([#60](https://www.github.com/googleapis/nodejs-precise-date/issues/60)) ([a975b1c](https://www.github.com/googleapis/nodejs-precise-date/commit/a975b1c39b9ad283b48eb8e2cb13d9eb1cb053ba))

## Bug Fixes
* **docs:** make anchors work in jsdoc ([#43](https://www.github.com/googleapis/nodejs-precise-date/issues/43)) ([5828db8](https://www.github.com/googleapis/nodejs-precise-date/commit/5828db8))

## Build System
* upgrade engines field to >=8.10.0 ([#25](https://www.github.com/googleapis/nodejs-precise-date/issues/25)) ([10b9cc1](https://www.github.com/googleapis/nodejs-precise-date/commit/10b9cc1))

## BREAKING CHANGES
* upgrade engines field to >=8.10.0 (#25)

## v0.1.0
02-19-2019 12:27 PST

## Hello, world!
- feat: initial code commit (#1)

## Documentation
- docs: update links in contrib guide (#4)

## Internal / Testing Changes
- chore: add missing boilerplate files (#3)
- chore: add dummy docs-test script and fix tests for Node 11 (#6)

---

# iCloud: web-app/node_modules/@google-cloud/precise-date/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/precise-date/README.md
> **Analyzed At:** 2026-06-13T06:32:46.883Z

## @google-cloud/precise-date
> A simple utility for precise-dateing functions and classes.

## Installing the package
It's unlikely you will need to install this package directly, as it will be
installed as a dependency when you install other `@google-cloud` packages.
```sh
$ npm install --save @google-cloud/precise-date
```

## Using the package
`PreciseDate` extends the native `Date` object, so you can use it in place of
that or when you need nanosecond precision.
```js
const {PreciseDate} = require('@google-cloud/precise-date');
const date = new PreciseDate('1547253035381101032');

date.toISOString();
// => 2019-01-12T00:30:35.381101032Z

date.toFullTimeString();
// => '1547253035381101032'
```

## PreciseDate([time])
Returns a new `date` instance.

## time
Type: `string` [`BigInt`][big_int] `Object<string, number>` `[number, number]`
```js
// from a full ISO string
date = new PreciseDate('2019-02-08T10:34:29.481145231Z');

// from a string representing nanoseconds
date = new PreciseDate('1549622069481320032');

// from a BigInt representing nanoseconds (requires Node >= 10.7)
date = new PreciseDate(1549622069481320032n);

// from an object containing `seconds` and `nanos` values
date = new PreciseDate({seconds: 1549622069, nanos: 481320032});

// from a tuple representing [seconds, nanos]
date = new PreciseDate([1549622069, 481320032]);
```

## PreciseDate.parseFull(time)
Similar to [`Date.parse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse), but this accepts the same nanosecond time options as the `PreciseDate` constructor and returns a string representing the nanoseconds in the specified date according to universal time.
```js
PreciseDate.parseFull('2019-02-08T10:34:29.481145231Z');
// => '1549622069481145231'
```

## PreciseDate.fullUTCString(...dateFields)
Similar to [`Date.UTC()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC), but also accepts microsecond and nanosecond parameters. Returns a string that represents the number of nanoseconds since January 1, 1970, 00:00:00 UTC.

## dateFields
Type: `...number`
```js
PreciseDate.fullUTCString(2019, 1, 8, 10, 34, 29, 481, 145, 231);
// => '1549622069481145231'
```

## PreciseDate.fullUTC(...dateFields)
Like `PreciseDate.fullUTCString()` but returns a native [`BigInt`][big_int] instead of a string. **Requires Node >= 10.7.**

## dateFields
Type: `...number`
```js
PreciseDate.fullUTC(2019, 1, 8, 10, 34, 29, 481, 145, 231);
// => 1549622069481145231n
```

## date
`PreciseDate` instance.

## date.getFullTimeString()
Returns a string of the specified date represented in nanoseconds according to universal time.

## date.getFullTime()
Like `date.getFullTimeString()` but returns a native [`BigInt`][big_int] instead of a string. **Requires Node >= 10.7.**

## date.getMicroseconds()
Returns the microseconds in the specified date according to universal time.

## date.getNanoseconds()
Returns the nanoseconds in the specified date according to universal time.

## date.setMicroseconds(microseconds)
Sets the microseconds for a specified date according to universal time. Returns a string representing the nanoseconds in the specified date according to universal time.

## microseconds
Type: `number`

## date.setNanoseconds(nanoseconds)
Sets the nanoseconds for a specified date according to universal time. Returns a string representing the nanoseconds in the specified date according to universal time.

## nanoseconds
Type: `number`

## date.setFullTime(time)
Sets the time to the number of supplied nanoseconds since January 1, 1970, 00:00:00 UTC. Returns a string representing the nanoseconds in the specified date according to universal time (effectively, the value of the argument).

## time
Type: `number` `string` [`BigInt`][big_int]

## date.toStruct()
Returns an object representing the specified date according to universal time.
Refer to [`google.protobuf.Timestamp`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp|google.protobuf.Timestamp) for more information about this format.
```js
const {seconds, nanos} = date.toStruct();
```

## date.toTuple()
Like `date.toStruct()` but returns the `seconds` and `nanos` as a tuple.
```js
const [seconds, nanos] = date.toTuple();
```
[big_int]: https://github.com/tc39/proposal-bigint

## Versioning
This library follows [Semantic Versioning](http://semver.org/).

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googlecloudplatform/google-cloud-node/blob/master/.github/CONTRIBUTING.md).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googlecloudplatform/google-cloud-node/blob/master/LICENSE)

---

# iCloud: web-app/node_modules/@google-cloud/paginator/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@google-cloud/paginator/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:46.888Z

## Changelog
[npm history][1]
[1]: https://www.npmjs.com/package/nodejs-paginator?activeTab=versions

## Bug Fixes
* Query should be on the list of extra args ([#365](https://github.com/googleapis/nodejs-paginator/issues/365)) ([50e40d0](https://github.com/googleapis/nodejs-paginator/commit/50e40d064aed1bd0d5f93a51ad54112343086644))

## Bug Fixes
* Should pass extra callback arguments back to consumer ([#361](https://github.com/googleapis/nodejs-paginator/issues/361)) ([cc5c48b](https://github.com/googleapis/nodejs-paginator/commit/cc5c48b95b21e9c6a4e555ff98de267258657b6e))

## ⚠ BREAKING CHANGES
* update to Node 14 ([#346](https://github.com/googleapis/nodejs-paginator/issues/346))

## Miscellaneous Chores
* Update to Node 14 ([#346](https://github.com/googleapis/nodejs-paginator/issues/346)) ([262ad70](https://github.com/googleapis/nodejs-paginator/commit/262ad70d3cc5e1aa8a67ece54c04920b24ceea09))

## Bug Fixes
* Remove pip install statements ([#1546](https://github.com/googleapis/nodejs-paginator/issues/1546)) ([#329](https://github.com/googleapis/nodejs-paginator/issues/329)) ([697567b](https://github.com/googleapis/nodejs-paginator/commit/697567bdd86226b740304734b9562a2f2241a96f))

## ⚠ BREAKING CHANGES
* update library to use Node 12 (#325)

## Build System
* update library to use Node 12 ([#325](https://github.com/googleapis/nodejs-paginator/issues/325)) ([02887ae](https://github.com/googleapis/nodejs-paginator/commit/02887ae2b370bff18cae7fe1d434ecdf663b5748))

## Bug Fixes
* update signature of end to comply with update node types definition ([#311](https://github.com/googleapis/nodejs-paginator/issues/311)) ([79e6fbd](https://github.com/googleapis/nodejs-paginator/commit/79e6fbdae5008d874613d2919a6cf723708fc919))

## Bug Fixes
* **build:** switch primary branch to main ([#287](https://www.github.com/googleapis/nodejs-paginator/issues/287)) ([1b796f3](https://www.github.com/googleapis/nodejs-paginator/commit/1b796f3377174354a62b7475d16f52213197f650))

## Bug Fixes
* add configs by running synthtool ([#241](https://www.github.com/googleapis/nodejs-paginator/issues/241)) ([643593a](https://www.github.com/googleapis/nodejs-paginator/commit/643593ae9ffb8febff69a7bdae19239f5bcb1266))

## Bug Fixes
* destroy ResourceStream with pre-flight error ([#236](https://www.github.com/googleapis/nodejs-paginator/issues/236)) ([d57beb4](https://www.github.com/googleapis/nodejs-paginator/commit/d57beb424d875a7bf502d458cc208f1bbe47a42a))

## Bug Fixes
* move gitattributes files to node templates ([#234](https://www.github.com/googleapis/nodejs-paginator/issues/234)) ([30e881c](https://www.github.com/googleapis/nodejs-paginator/commit/30e881ce7415749b93b6b7e4e71745ea3fb248b6))

## Bug Fixes
* update node issue template ([#221](https://www.github.com/googleapis/nodejs-paginator/issues/221)) ([088153c](https://www.github.com/googleapis/nodejs-paginator/commit/088153c4fca6d53e2e5ef4bb42365ce5493b913d))

## Bug Fixes
* apache license URL ([#468](https://www.github.com/googleapis/nodejs-paginator/issues/468)) ([#211](https://www.github.com/googleapis/nodejs-paginator/issues/211)) ([f343b7f](https://www.github.com/googleapis/nodejs-paginator/commit/f343b7f7e184fd1b453f20ac1463d17520aac7ad))

## ⚠ BREAKING CHANGES
* **dep:** upgrade gts 2.0.0 (#194)
* **deps:** deprecated node 8 to 10; upgrade typescript

## Miscellaneous Chores
* **dep:** upgrade gts 2.0.0 ([#194](https://www.github.com/googleapis/nodejs-paginator/issues/194)) ([4eaf9be](https://www.github.com/googleapis/nodejs-paginator/commit/4eaf9bed1fcfd0f10e877ff15c1d0e968e3356c8))
* **deps:** deprecated node 8 to 10; upgrade typescript ([f6434ab](https://www.github.com/googleapis/nodejs-paginator/commit/f6434ab9cacb6ab804c070f19c38b6072ca326b5))

## Bug Fixes
* **deps:** pin TypeScript below 3.7.0 ([e06e1b0](https://www.github.com/googleapis/nodejs-paginator/commit/e06e1b0a2e2bb1cf56fc806c1703b8b5e468b954))

## Bug Fixes
* **docs:** add jsdoc-region-tag plugin ([#155](https://www.github.com/googleapis/nodejs-paginator/issues/155)) ([b983799](https://www.github.com/googleapis/nodejs-paginator/commit/b98379905848fd179c6268aff3e1cfaf2bf76663))

## Bug Fixes
* **deps:** use the latest extend ([#141](https://www.github.com/googleapis/nodejs-paginator/issues/141)) ([61b383e](https://www.github.com/googleapis/nodejs-paginator/commit/61b383e))

## ⚠ BREAKING CHANGES
* rewrite streaming logic (#136)

## Code Refactoring
* rewrite streaming logic ([#136](https://www.github.com/googleapis/nodejs-paginator/issues/136)) ([641d82d](https://www.github.com/googleapis/nodejs-paginator/commit/641d82d))

## Bug Fixes
* **docs:** link to reference docs section on googleapis.dev ([#132](https://www.github.com/googleapis/nodejs-paginator/issues/132)) ([be231be](https://www.github.com/googleapis/nodejs-paginator/commit/be231be))

## Bug Fixes
* **docs:** move to new client docs URL ([#129](https://www.github.com/googleapis/nodejs-paginator/issues/129)) ([689f483](https://www.github.com/googleapis/nodejs-paginator/commit/689f483))

## Bug Fixes
* **deps:** update dependency arrify to v2 ([#109](https://www.github.com/googleapis/nodejs-paginator/issues/109)) ([9f06c83](https://www.github.com/googleapis/nodejs-paginator/commit/9f06c83))

## Build System
* upgrade engines field to >=8.10.0 ([#115](https://www.github.com/googleapis/nodejs-paginator/issues/115)) ([0921076](https://www.github.com/googleapis/nodejs-paginator/commit/0921076))

## BREAKING CHANGES
* upgrade engines field to >=8.10.0 (#115)

## v0.2.0
03-08-2019 12:15 PST

## New Features
- feat: handle promise based functions ([#91](https://github.com/googleapis/nodejs-paginator/pull/91))
- refactor(ts): create generic for object streams ([#101](https://github.com/googleapis/nodejs-paginator/pull/101))

## Dependencies
- chore(deps): update dependency through2 to v3 ([#53](https://github.com/googleapis/nodejs-paginator/pull/53))
- chore(deps): update dependency @types/is to v0.0.21 ([#55](https://github.com/googleapis/nodejs-paginator/pull/55))
- chore(deps): update dependency gts to ^0.9.0 ([#57](https://github.com/googleapis/nodejs-paginator/pull/57))
- fix: Pin @types/sinon to last compatible version ([#61](https://github.com/googleapis/nodejs-paginator/pull/61))
- refactor: trim a few dependencies ([#60](https://github.com/googleapis/nodejs-paginator/pull/60))
- chore(deps): update dependency @types/sinon to v5.0.7 ([#62](https://github.com/googleapis/nodejs-paginator/pull/62))
- chore(deps): update dependency @types/sinon to v7 ([#81](https://github.com/googleapis/nodejs-paginator/pull/81))
- chore(deps): update dependency mocha to v6

## Documentation
- docs: add lint/fix example to contributing guide ([#85](https://github.com/googleapis/nodejs-paginator/pull/85))
- chore: move CONTRIBUTING.md to root ([#87](https://github.com/googleapis/nodejs-paginator/pull/87))
- docs: update links in contrib guide ([#94](https://github.com/googleapis/nodejs-paginator/pull/94))
- docs: update contributing path in README ([#88](https://github.com/googleapis/nodejs-paginator/pull/88))

## Internal / Testing Changes
- chore: include build in eslintignore ([#49](https://github.com/googleapis/nodejs-paginator/pull/49))
- chore: update CircleCI config ([#52](https://github.com/googleapis/nodejs-paginator/pull/52))
- chore: use latest npm on Windows ([#54](https://github.com/googleapis/nodejs-paginator/pull/54))
- chore: update eslintignore config ([#56](https://github.com/googleapis/nodejs-paginator/pull/56))
- chore: add synth.metadata
- fix(build): fix system key decryption ([#64](https://github.com/googleapis/nodejs-paginator/pull/64))
- chore: update license file ([#68](https://github.com/googleapis/nodejs-paginator/pull/68))
- chore(build): update prettier config ([#69](https://github.com/googleapis/nodejs-paginator/pull/69))
- chore: nyc ignore build/test by default ([#71](https://github.com/googleapis/nodejs-paginator/pull/71))
- chore: always nyc report before calling codecov ([#72](https://github.com/googleapis/nodejs-paginator/pull/72))
- build: add Kokoro configs for autorelease ([#75](https://github.com/googleapis/nodejs-paginator/pull/75))
- fix(build): fix Kokoro release script ([#76](https://github.com/googleapis/nodejs-paginator/pull/76))
- chore: fix publish.sh permission +x ([#77](https://github.com/googleapis/nodejs-paginator/pull/77))
- chore: update nyc and eslint configs ([#79](https://github.com/googleapis/nodejs-paginator/pull/79))
- chore(build): inject yoshi automation key ([#80](https://github.com/googleapis/nodejs-paginator/pull/80))
- build: check broken links in generated docs ([#82](https://github.com/googleapis/nodejs-paginator/pull/82))
- build: ignore googleapis.com in doc link check ([#84](https://github.com/googleapis/nodejs-paginator/pull/84))
- build: test using @grpc/grpc-js in CI ([#89](https://github.com/googleapis/nodejs-paginator/pull/89))
- build: create docs test npm scripts ([#90](https://github.com/googleapis/nodejs-paginator/pull/90))
- build: use linkinator for docs test ([#93](https://github.com/googleapis/nodejs-paginator/pull/93))
- build: update release configuration
- build: fix types for sinon ([#98](https://github.com/googleapis/nodejs-paginator/pull/98))
- build: use node10 to run samples-test, system-test etc ([#97](https://github.com/googleapis/nodejs-paginator/pull/97))
- build: Add docuploader credentials to node publish jobs ([#99](https://github.com/googleapis/nodejs-paginator/pull/99))

## Bug fixes
- fix: call limiter.makeRequest() instead of original method ([#43](https://github.com/googleapis/nodejs-paginator/pull/43))

## Internal / Testing Changes
- chore: update issue templates ([#42](https://github.com/googleapis/nodejs-paginator/pull/42))
- chore: remove old issue template ([#40](https://github.com/googleapis/nodejs-paginator/pull/40))
- build: run tests on node11 ([#39](https://github.com/googleapis/nodejs-paginator/pull/39))
- chores(build): run codecov on continuous builds ([#36](https://github.com/googleapis/nodejs-paginator/pull/36))
- chores(build): do not collect sponge.xml from windows builds ([#37](https://github.com/googleapis/nodejs-paginator/pull/37))
- chore: update new issue template ([#35](https://github.com/googleapis/nodejs-paginator/pull/35))
- chore(deps): update dependency sinon to v7 ([#31](https://github.com/googleapis/nodejs-paginator/pull/31))
- build: fix codecov uploading on Kokoro ([#32](https://github.com/googleapis/nodejs-paginator/pull/32))
- Update kokoro config ([#29](https://github.com/googleapis/nodejs-paginator/pull/29))
- Update CI config ([#27](https://github.com/googleapis/nodejs-paginator/pull/27))
- Don't publish sourcemaps ([#25](https://github.com/googleapis/nodejs-paginator/pull/25))
- build: prevent system/sample-test from leaking credentials
- Update kokoro config ([#23](https://github.com/googleapis/nodejs-paginator/pull/23))
- test: remove appveyor config ([#22](https://github.com/googleapis/nodejs-paginator/pull/22))
- Update CI config ([#21](https://github.com/googleapis/nodejs-paginator/pull/21))
- Enable prefer-const in the eslint config ([#20](https://github.com/googleapis/nodejs-paginator/pull/20))
- Enable no-var in eslint ([#19](https://github.com/googleapis/nodejs-paginator/pull/19))
- Update CI config ([#18](https://github.com/googleapis/nodejs-paginator/pull/18))

## Internal / Testing Changes
- Add synth script and update CI config (#14)
- chore(deps): update dependency nyc to v13 (#12)
- chore: ignore package-lock.json (#11)
- chore(deps): lock file maintenance (#10)
- chore: update renovate config (#9)
- remove that whitespace (#8)
- chore(deps): lock file maintenance (#7)
- chore(deps): update dependency typescript to v3 (#6)
- chore: assert.deelEqual => assert.deepStrictEqual (#5)
- chore: move mocha options to mocha.opts (#4)

---

# iCloud: web-app/node_modules/@google-cloud/paginator/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/paginator/README.md
> **Analyzed At:** 2026-06-13T06:32:46.893Z

## [Google Cloud Common Paginator: Node.js Client](https://github.com/googleapis/nodejs-paginator)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/@google-cloud/paginator.svg)](https://www.npmjs.org/package/@google-cloud/paginator)
A result paging utility used by Google node.js modules
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/nodejs-paginator/blob/main/CHANGELOG.md).
* [Google Cloud Common Paginator Node.js Client API Reference][client-docs]
* [github.com/googleapis/nodejs-paginator](https://github.com/googleapis/nodejs-paginator)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Using the client library](#using-the-client-library)
* [Samples](#samples)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install @google-cloud/paginator
```

## Using the client library
```javascript
const {paginator} = require('@google-cloud/paginator');
console.log(paginator);

```

## Samples
Samples are in the [`samples/`](https://github.com/googleapis/nodejs-paginator/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.
| Sample                      | Source Code                       | Try it |
| --------------------------- | --------------------------------- | ------ |
| Quickstart | [source code](https://github.com/googleapis/nodejs-paginator/blob/main/samples/quickstart.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-paginator&page=editor&open_in_editor=samples/quickstart.js,samples/README.md) |
| Streamify | [source code](https://github.com/googleapis/nodejs-paginator/blob/main/samples/streamify.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/nodejs-paginator&page=editor&open_in_editor=samples/streamify.js,samples/README.md) |
The [Google Cloud Common Paginator Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install @google-cloud/paginator@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-paginator/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/nodejs-paginator/blob/main/LICENSE)
[client-docs]: https://cloud.google.com/nodejs/docs/reference/paginator/latest
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/getting-started

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-resource-util/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-resource-util/README.md
> **Analyzed At:** 2026-06-13T06:32:46.898Z

## OpenTelemetry Google Resource Util
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
This package provides utils used by other packages in this repo. It can map
OpenTelemetry resources to Google Cloud monitored resources. It is not intended
to be used directly by users.
To get started with instrumentation in Google Cloud, see [Generate traces and metrics with
Node.js](https://cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs).
To learn more about instrumentation and observability, including opinionated recommendations
for Google Cloud Observability, visit [Instrumentation and
observability](https://cloud.google.com/stackdriver/docs/instrumentation/overview).

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
[license-url]: https://github.com/GoogleCloudPlatform/opentelemetry-operations-js/blob/main/LICENSE
[npm-url]: https://www.npmjs.com/package/@google-cloud/opentelemetry-monitored-resource-utils
[npm-img]: https://badge.fury.io/js/%40google-cloud%2Fopentelemetry-monitored-resource-utils.svg
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-resource-util/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-resource-util/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.903Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-resource-util/node_modules/gcp-metadata/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-resource-util/node_modules/gcp-metadata/README.md
> **Analyzed At:** 2026-06-13T06:32:46.920Z

## [GCP Metadata: Node.js Client](https://github.com/googleapis/gcp-metadata)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/gcp-metadata.svg)](https://www.npmjs.org/package/gcp-metadata)
Get the metadata from a Google Cloud Platform environment
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/gcp-metadata/blob/main/CHANGELOG.md).
* [GCP Metadata Node.js Client API Reference][client-docs]
* [GCP Metadata Documentation][product-docs]
* [github.com/googleapis/gcp-metadata](https://github.com/googleapis/gcp-metadata)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Using the client library](#using-the-client-library)
* [Samples](#samples)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install gcp-metadata
```

## Using the client library
```javascript
const gcpMetadata = require('gcp-metadata');

async function quickstart() {
  // check to see if this code can access a metadata server
  const isAvailable = await gcpMetadata.isAvailable();
  console.log(`Is available: ${isAvailable}`);

  // Instance and Project level metadata will only be available if
  // running inside of a Google Cloud compute environment such as
  // Cloud Functions, App Engine, Kubernetes Engine, or Compute Engine.
  // To learn more about the differences between instance and project
  // level metadata, see:
  // https://cloud.google.com/compute/docs/storing-retrieving-metadata#project-instance-metadata
  if (isAvailable) {
    // grab all top level metadata from the service
    const instanceMetadata = await gcpMetadata.instance();
    console.log('Instance metadata:');
    console.log(instanceMetadata);

    // get all project level metadata
    const projectMetadata = await gcpMetadata.project();
    console.log('Project metadata:');
    console.log(projectMetadata);
  }
}

quickstart();

```

## Check to see if the metadata server is available
```js
const isAvailable = await gcpMetadata.isAvailable();
```

## Access all metadata
```js
const data = await gcpMetadata.instance();
console.log(data); // ... All metadata properties
```

## Access specific properties
```js
const data = await gcpMetadata.instance('hostname');
console.log(data); // ...Instance hostname
const projectId = await gcpMetadata.project('project-id');
console.log(projectId); // ...Project ID of the running instance
```

## Access nested properties with the relative path
```js
const data = await gcpMetadata.instance('service-accounts/default/email');
console.log(data); // ...Email address of the Compute identity service account
```

## Access specific properties with query parameters
```js
const data = await gcpMetadata.instance({
  property: 'tags',
  params: { alt: 'text' }
});
console.log(data) // ...Tags as newline-delimited list
```

## Access with custom headers
```js
await gcpMetadata.instance({
  headers: { 'no-trace': '1' }
}); // ...Request is untraced
```

## Take care with large number valued properties
In some cases number valued properties returned by the Metadata Service may be
too large to be representable as JavaScript numbers. In such cases we return
those values as `BigNumber` objects (from the [bignumber.js](https://github.com/MikeMcl/bignumber.js) library). Numbers
that fit within the JavaScript number range will be returned as normal number
values.
```js
const id = await gcpMetadata.instance('id');
console.log(id)  // ... BigNumber { s: 1, e: 18, c: [ 45200, 31799277581759 ] }
console.log(id.toString()) // ... 4520031799277581759
```

## Environment variables
* `GCE_METADATA_HOST`: provide an alternate host or IP to perform lookup against (useful, for example, you're connecting through a custom proxy server).
For example:
  ```
  export GCE_METADATA_HOST='169.254.169.254'
```
* `DETECT_GCP_RETRIES`: number representing number of retries that should be attempted on metadata lookup.
* `DEBUG_AUTH`: emit debugging logs
* `METADATA_SERVER_DETECTION`: configure desired metadata server availability check behavior.
* `assume-present`: don't try to ping the metadata server, but assume it's present
* `none`: don't try to ping the metadata server, but don't try to use it either
* `bios-only`: treat the result of a BIOS probe as canonical (don't fall back to pinging)
* `ping-only`: skip the BIOS probe, and go straight to pinging

## Samples
Samples are in the [`samples/`](https://github.com/googleapis/gcp-metadata/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.
| Sample                      | Source Code                       | Try it |
| --------------------------- | --------------------------------- | ------ |
| Quickstart | [source code](https://github.com/googleapis/gcp-metadata/blob/main/samples/quickstart.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/gcp-metadata&page=editor&open_in_editor=samples/quickstart.js,samples/README.md) |
The [GCP Metadata Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install gcp-metadata@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/gcp-metadata/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/gcp-metadata/blob/main/LICENSE)
[client-docs]: https://cloud.google.com/nodejs/docs/reference/gcp-metadata/latest
[product-docs]: https://cloud.google.com/compute/docs/storing-retrieving-metadata
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/external/set-up-adc-local

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-resource-util/node_modules/gaxios/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-resource-util/node_modules/gaxios/README.md
> **Analyzed At:** 2026-06-13T06:32:46.925Z

## gaxios
[![npm version](https://img.shields.io/npm/v/gaxios.svg)](https://www.npmjs.org/package/gaxios)
[![codecov](https://codecov.io/gh/googleapis/gaxios/branch/master/graph/badge.svg)](https://codecov.io/gh/googleapis/gaxios)
[![Code Style: Google](https://img.shields.io/badge/code%20style-google-blueviolet.svg)](https://github.com/google/gts)
> An HTTP request client that provides an `axios` like interface over top of `node-fetch`.

## Install
```sh
$ npm install gaxios
```

## Example
```js
const {request} = require('gaxios');
const res = await request({
  url: 'https://www.googleapis.com/discovery/v1/apis/',
});
```

## Setting Defaults
Gaxios supports setting default properties both on the default instance, and on additional instances. This is often useful when making many requests to the same domain with the same base settings. For example:
```js
const gaxios = require('gaxios');
gaxios.instance.defaults = {
  baseURL: 'https://example.com'
  headers: {
    Authorization: 'SOME_TOKEN'
  }
}
gaxios.request({url: '/data'}).then(...);
```
Note that setting default values will take precedence
over other authentication methods, i.e., application default credentials.

## Request Options
```ts
interface GaxiosOptions = {
  // The url to which the request should be sent.  Required.
  url: string,

  // The HTTP method to use for the request.  Defaults to `GET`.
  method: 'GET',

  // The base Url to use for the request. Prepended to the `url` property above.
  baseURL: 'https://example.com';

  // The HTTP methods to be sent with the request.
  headers: { 'some': 'header' },

  // The data to send in the body of the request. Data objects will be
  // serialized as JSON.
  //
  // Note: if you would like to provide a Content-Type header other than
  // application/json you you must provide a string or readable stream, rather
  // than an object:
  // data: JSON.stringify({some: 'data'})
  // data: fs.readFile('./some-data.jpeg')
  data: {
    some: 'data'
  },

  // The max size of the http response content in bytes allowed.
  // Defaults to `0`, which is the same as unset.
  maxContentLength: 2000,

  // The max number of HTTP redirects to follow.
  // Defaults to 100.
  maxRedirects: 100,

  // The querystring parameters that will be encoded using `qs` and
  // appended to the url
  params: {
    querystring: 'parameters'
  },

  // By default, we use the `querystring` package in node core to serialize
  // querystring parameters.  You can override that and provide your
  // own implementation.
  paramsSerializer: (params) => {
    return qs.stringify(params);
  },

  // The timeout for the HTTP request in milliseconds. Defaults to 0.
  timeout: 1000,

  // Optional method to override making the actual HTTP request. Useful
  // for writing tests and instrumentation
  adapter?: async (options, defaultAdapter) => {
    const res = await defaultAdapter(options);
    res.data = {
      ...res.data,
      extraProperty: 'your extra property',
    };
    return res;
  };

  // The expected return type of the request.  Options are:
  // json | stream | blob | arraybuffer | text | unknown
  // Defaults to `unknown`.
  responseType: 'unknown',

  // The node.js http agent to use for the request.
  agent: someHttpsAgent,

  // Custom function to determine if the response is valid based on the
  // status code.  Defaults to (>= 200 && < 300)
  validateStatus: (status: number) => true,

  // Implementation of `fetch` to use when making the API call. By default,
  // will use the browser context if available, and fall back to `node-fetch`
  // in node.js otherwise.
  fetchImplementation?: typeof fetch;

  // Configuration for retrying of requests.
  retryConfig: {
    // The number of times to retry the request.  Defaults to 3.
    retry?: number;

    // The number of retries already attempted.
    currentRetryAttempt?: number;

    // The HTTP Methods that will be automatically retried.
    // Defaults to ['GET','PUT','HEAD','OPTIONS','DELETE']
    httpMethodsToRetry?: string[];

    // The HTTP response status codes that will automatically be retried.
    // Defaults to: [[100, 199], [408, 408], [429, 429], [500, 599]]
    statusCodesToRetry?: number[][];

    // Function to invoke when a retry attempt is made.
    onRetryAttempt?: (err: GaxiosError) => Promise<void> | void;

    // Function to invoke which determines if you should retry
    shouldRetry?: (err: GaxiosError) => Promise<boolean> | boolean;

    // When there is no response, the number of retries to attempt. Defaults to 2.
    noResponseRetries?: number;

    // The amount of time to initially delay the retry, in ms.  Defaults to 100ms.
    retryDelay?: number;
  },

  // Enables default configuration for retries.
  retry: boolean,

  // Cancelling a request requires the `abort-controller` library.
  // See https://github.com/bitinn/node-fetch#request-cancellation-with-abortsignal
  signal?: AbortSignal

  /**
   * A collection of parts to send as a `Content-Type: multipart/related` request.
   */
  multipart?: GaxiosMultipartOptions;

  /**
   * An optional proxy to use for requests.
   * Available via `process.env.HTTP_PROXY` and `process.env.HTTPS_PROXY` as well - with a preference for the this config option when multiple are available.
   * The `agent` option overrides this.
   *
   * @see {@link GaxiosOptions.noProxy}
   * @see {@link GaxiosOptions.agent}
   */
  proxy?: string | URL;
  /**
   * A list for excluding traffic for proxies.
   * Available via `process.env.NO_PROXY` as well as a common-separated list of strings - merged with any local `noProxy` rules.
   *
   * - When provided a string, it is matched by
   *   - Wildcard `*.` and `.` matching are available. (e.g. `.example.com` or `*.example.com`)
   * - When provided a URL, it is matched by the `.origin` property.
   *   - For example, requesting `https://example.com` with the following `noProxy`s would result in a no proxy use:
   *     - new URL('https://example.com')
   *     - new URL('https://example.com:443')
   *   - The following would be used with a proxy:
   *     - new URL('http://example.com:80')
   *     - new URL('https://example.com:8443')
   * - When provided a regular expression it is used to match the stringified URL
   *
   * @see {@link GaxiosOptions.proxy}
   */
  noProxy?: (string | URL | RegExp)[];

  /**
   * An experimental, customizable error redactor.
   *
   * Set `false` to disable.
   *
   * @remarks
   *
   * This does not replace the requirement for an active Data Loss Prevention (DLP) provider. For DLP suggestions, see:
   * - https://cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data#dlp_deidentify_replace_infotype-nodejs
   * - https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets
   *
   * @experimental
   */
  errorRedactor?: typeof defaultErrorRedactor | false;
}
```

## License
[Apache-2.0](https://github.com/googleapis/gaxios/blob/master/LICENSE)

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/README.md
> **Analyzed At:** 2026-06-13T06:32:46.931Z

## OpenTelemetry Google Cloud Monitoring Exporter
[![NPM Published Version][npm-img]][npm-url]
[![Apache License][license-image]][license-image]
OpenTelemetry Google Cloud Monitoring Exporter allows the user to send collected metrics to
[Google Cloud Monitoring](https://cloud.google.com/monitoring).
To get started with instrumentation in Google Cloud, see [Generate traces and metrics with
Node.js](https://cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs).
To learn more about instrumentation and observability, including opinionated recommendations
for Google Cloud Observability, visit [Instrumentation and
observability](https://cloud.google.com/stackdriver/docs/instrumentation/overview).

## Installation
```bash
npm install --save @opentelemetry/sdk-metrics
npm install --save @google-cloud/opentelemetry-cloud-monitoring-exporter
```

## Usage
```js
const { MeterProvider, PeriodicExportingMetricReader } = require("@opentelemetry/sdk-metrics");
const { resourceFromAttributes } = require("@opentelemetry/resources");
const { MetricExporter } = require("@google-cloud/opentelemetry-cloud-monitoring-exporter");
const { GcpDetectorSync } = require("@google-cloud/opentelemetry-resource-util");

// Create MeterProvider
const meterProvider = new MeterProvider({
  // Create a resource. Fill the `service.*` attributes in with real values for your service.
  // GcpDetectorSync will add in resource information about the current environment if you are
  // running on GCP. These resource attributes will be translated to a specific GCP monitored
  // resource if running on GCP. Otherwise, metrics will be sent with monitored resource
  // `generic_task`.
  resource: resourceFromAttributes({
    "service.name": "example-metric-service",
    "service.namespace": "samples",
    "service.instance.id": "12345",
  }).merge(new GcpDetectorSync().detect()),
});
// Register the exporter
meterProvider.addMetricReader(
  new PeriodicExportingMetricReader({
    // Export metrics every 10 seconds. 5 seconds is the smallest sample period allowed by
    // Cloud Monitoring.
    exportIntervalMillis: 10_000,
    exporter: new MetricExporter(),
  })
);

// Create a meter
const meter = meterProvider.getMeter("metrics-sample");

// Create a counter instrument
const counter = meter.createCounter("metric_name");
// Record a measurement
counter.add(10, { key: "value" });

// Wait for the metric to be exported
new Promise((resolve) => {
  setTimeout(resolve, 11_000);
});
```

## Enabling Exponential Histograms
This exporter can send OpenTelemetry Exponential Histograms to Google Cloud Monitoring. To use
this feature, add a metric [View][views] to configure `Histogram` instruments to use the
`ExponentialHistogram` aggregation:
```js
const {
  Aggregation,
  InstrumentType,
  MeterProvider,
  View
} = require("@opentelemetry/sdk-metrics");

const meterProvider = new MeterProvider({
  // ...
  views: [
    // To use ExponentialHistogram aggregation for all Histograms:
    new View({
      aggregation: Aggregation.ExponentialHistogram(),
      instrumentType: InstrumentType.HISTOGRAM,
    }),

    // Or if you'd only like to target a specific instrument:
    new View({
      aggregation: Aggregation.ExponentialHistogram(),
      instrumentType: InstrumentType.HISTOGRAM,
      instrumentName: "http.client.duration",
    }),
  ],
});
```
For more information on metric Views, see [Configure Metric Views][views].

## Viewing your metrics:
With the above you should now be able to navigate to the Google Cloud Monitoring UI at:

## Useful links
- For more information on OpenTelemetry, visit: 
- For more about OpenTelemetry JavaScript: 
- Learn more about Google Cloud Monitoring at https://cloud.google.com/monitoring
[views]: https://opentelemetry.io/docs/instrumentation/js/manual/#configure-metric-views
[license-url]: https://github.com/GoogleCloudPlatform/opentelemetry-operations-js/blob/main/LICENSE
[npm-url]: https://www.npmjs.com/package/@google-cloud/opentelemetry-cloud-monitoring-exporter
[npm-img]: https://badge.fury.io/js/%40google-cloud%2Fopentelemetry-cloud-monitoring-exporter.svg
[license-image]: https://img.shields.io/badge/license-Apache_2.0-green.svg?style=flat

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/uuid/CONTRIBUTING.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/uuid/CONTRIBUTING.md
> **Analyzed At:** 2026-06-13T06:32:46.936Z

## Contributing
Please feel free to file GitHub Issues or propose Pull Requests. We're always happy to discuss improvements to this library!

## Testing
```shell
npm test
```

## Releasing
Releases are supposed to be done from master, version bumping is automated through [`standard-version`](https://github.com/conventional-changelog/standard-version):
```shell
npm run release -- --dry-run  # verify output manually
npm run release               # follow the instructions from the output of this command
```

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/googleapis-common/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/googleapis-common/README.md
> **Analyzed At:** 2026-06-13T06:32:46.953Z

## [Google APIs Common Module: Node.js Client](https://github.com/googleapis/nodejs-googleapis-common)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/googleapis-common.svg)](https://www.npmjs.org/package/googleapis-common)
A common tooling library used by the googleapis npm module. You probably don't want to use this directly.
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/nodejs-googleapis-common/blob/main/CHANGELOG.md).
* [Google APIs Common Module Node.js Client API Reference][client-docs]
* [github.com/googleapis/nodejs-googleapis-common](https://github.com/googleapis/nodejs-googleapis-common)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install googleapis-common
```
The [Google APIs Common Module Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install googleapis-common@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/nodejs-googleapis-common/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/nodejs-googleapis-common/blob/main/LICENSE)
[client-docs]: https://cloud.google.com/nodejs/docs/reference/googleapis-common/latest
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/getting-started

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/gcp-metadata/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/gcp-metadata/README.md
> **Analyzed At:** 2026-06-13T06:32:47.023Z

## [GCP Metadata: Node.js Client](https://github.com/googleapis/gcp-metadata)
[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages)
[![npm version](https://img.shields.io/npm/v/gcp-metadata.svg)](https://www.npmjs.org/package/gcp-metadata)
Get the metadata from a Google Cloud Platform environment
A comprehensive list of changes in each version may be found in
[the CHANGELOG](https://github.com/googleapis/gcp-metadata/blob/main/CHANGELOG.md).
* [GCP Metadata Node.js Client API Reference][client-docs]
* [GCP Metadata Documentation][product-docs]
* [github.com/googleapis/gcp-metadata](https://github.com/googleapis/gcp-metadata)
Read more about the client libraries for Cloud APIs, including the older
Google APIs Client Libraries, in [Client Libraries Explained][explained].
[explained]: https://cloud.google.com/apis/docs/client-libraries-explained
**Table of contents:**
* [Quickstart](#quickstart)
* [Installing the client library](#installing-the-client-library)
* [Using the client library](#using-the-client-library)
* [Samples](#samples)
* [Versioning](#versioning)
* [Contributing](#contributing)
* [License](#license)

## Installing the client library
```bash
npm install gcp-metadata
```

## Using the client library
```javascript
const gcpMetadata = require('gcp-metadata');

async function quickstart() {
  // check to see if this code can access a metadata server
  const isAvailable = await gcpMetadata.isAvailable();
  console.log(`Is available: ${isAvailable}`);

  // Instance and Project level metadata will only be available if
  // running inside of a Google Cloud compute environment such as
  // Cloud Functions, App Engine, Kubernetes Engine, or Compute Engine.
  // To learn more about the differences between instance and project
  // level metadata, see:
  // https://cloud.google.com/compute/docs/storing-retrieving-metadata#project-instance-metadata
  if (isAvailable) {
    // grab all top level metadata from the service
    const instanceMetadata = await gcpMetadata.instance();
    console.log('Instance metadata:');
    console.log(instanceMetadata);

    // get all project level metadata
    const projectMetadata = await gcpMetadata.project();
    console.log('Project metadata:');
    console.log(projectMetadata);
  }
}

quickstart();

```

## Check to see if the metadata server is available
```js
const isAvailable = await gcpMetadata.isAvailable();
```

## Access all metadata
```js
const data = await gcpMetadata.instance();
console.log(data); // ... All metadata properties
```

## Access specific properties
```js
const data = await gcpMetadata.instance('hostname');
console.log(data); // ...Instance hostname
const projectId = await gcpMetadata.project('project-id');
console.log(projectId); // ...Project ID of the running instance
```

## Access nested properties with the relative path
```js
const data = await gcpMetadata.instance('service-accounts/default/email');
console.log(data); // ...Email address of the Compute identity service account
```

## Access specific properties with query parameters
```js
const data = await gcpMetadata.instance({
  property: 'tags',
  params: { alt: 'text' }
});
console.log(data) // ...Tags as newline-delimited list
```

## Access with custom headers
```js
await gcpMetadata.instance({
  headers: { 'no-trace': '1' }
}); // ...Request is untraced
```

## Take care with large number valued properties
In some cases number valued properties returned by the Metadata Service may be
too large to be representable as JavaScript numbers. In such cases we return
those values as `BigNumber` objects (from the [bignumber.js](https://github.com/MikeMcl/bignumber.js) library). Numbers
that fit within the JavaScript number range will be returned as normal number
values.
```js
const id = await gcpMetadata.instance('id');
console.log(id)  // ... BigNumber { s: 1, e: 18, c: [ 45200, 31799277581759 ] }
console.log(id.toString()) // ... 4520031799277581759
```

## Environment variables
* `GCE_METADATA_HOST`: provide an alternate host or IP to perform lookup against (useful, for example, you're connecting through a custom proxy server).
For example:
  ```
  export GCE_METADATA_HOST='169.254.169.254'
```
* `DETECT_GCP_RETRIES`: number representing number of retries that should be attempted on metadata lookup.
* `DEBUG_AUTH`: emit debugging logs
* `METADATA_SERVER_DETECTION`: configure desired metadata server availability check behavior.
* `assume-present`: don't try to ping the metadata server, but assume it's present
* `none`: don't try to ping the metadata server, but don't try to use it either
* `bios-only`: treat the result of a BIOS probe as canonical (don't fall back to pinging)
* `ping-only`: skip the BIOS probe, and go straight to pinging

## Samples
Samples are in the [`samples/`](https://github.com/googleapis/gcp-metadata/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.
| Sample                      | Source Code                       | Try it |
| --------------------------- | --------------------------------- | ------ |
| Quickstart | [source code](https://github.com/googleapis/gcp-metadata/blob/main/samples/quickstart.js) | [![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/gcp-metadata&page=editor&open_in_editor=samples/quickstart.js,samples/README.md) |
The [GCP Metadata Node.js Client API Reference][client-docs] documentation
also contains samples.

## Supported Node.js Versions
Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule).
Libraries are compatible with all current _active_ and _maintenance_ versions of
Node.js.
If you are using an end-of-life version of Node.js, we recommend that you update
as soon as possible to an actively supported LTS version.
Google's client libraries support legacy versions of Node.js runtimes on a
best-efforts basis with the following warnings:
* Legacy versions are not tested in continuous integration.
* Some security patches and features cannot be backported.
* Dependencies cannot be kept up-to-date.
Client libraries targeting some end-of-life versions of Node.js are available, and
can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag).
The dist-tags follow the naming convention `legacy-(version)`.
For example, `npm install gcp-metadata@legacy-8` installs client libraries
for versions compatible with Node.js 8.

## Versioning
This library follows [Semantic Versioning](http://semver.org/).
This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways
unless absolutely necessary (e.g. because of critical security issues) or with
an extensive deprecation period. Issues and requests against **stable** libraries
are addressed with the highest priority.
More Information: [Google Cloud Platform Launch Stages][launch_stages]
[launch_stages]: https://cloud.google.com/terms/launch-stages

## Contributing
Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/gcp-metadata/blob/main/CONTRIBUTING.md).
Please note that this `README.md`, the `samples/README.md`,
and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`)
are generated from a central template. To edit one of these files, make an edit
to its templates in
[directory](https://github.com/googleapis/synthtool).

## License
Apache Version 2.0
See [LICENSE](https://github.com/googleapis/gcp-metadata/blob/main/LICENSE)
[client-docs]: https://cloud.google.com/nodejs/docs/reference/gcp-metadata/latest
[product-docs]: https://cloud.google.com/compute/docs/storing-retrieving-metadata
[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[projects]: https://console.cloud.google.com/project
[billing]: https://support.google.com/cloud/answer/6293499#enable-billing
[auth]: https://cloud.google.com/docs/authentication/external/set-up-adc-local

---

# iCloud: web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/gaxios/README.md

> **Source:** icloud://web-app/node_modules/@google-cloud/opentelemetry-cloud-monitoring-exporter/node_modules/gaxios/README.md
> **Analyzed At:** 2026-06-13T06:32:47.030Z

## gaxios
[![npm version](https://img.shields.io/npm/v/gaxios.svg)](https://www.npmjs.org/package/gaxios)
[![codecov](https://codecov.io/gh/googleapis/gaxios/branch/master/graph/badge.svg)](https://codecov.io/gh/googleapis/gaxios)
[![Code Style: Google](https://img.shields.io/badge/code%20style-google-blueviolet.svg)](https://github.com/google/gts)
> An HTTP request client that provides an `axios` like interface over top of `node-fetch`.

## Install
```sh
$ npm install gaxios
```

## Example
```js
const {request} = require('gaxios');
const res = await request({
  url: 'https://www.googleapis.com/discovery/v1/apis/',
});
```

## Setting Defaults
Gaxios supports setting default properties both on the default instance, and on additional instances. This is often useful when making many requests to the same domain with the same base settings. For example:
```js
const gaxios = require('gaxios');
gaxios.instance.defaults = {
  baseURL: 'https://example.com'
  headers: {
    Authorization: 'SOME_TOKEN'
  }
}
gaxios.request({url: '/data'}).then(...);
```
Note that setting default values will take precedence
over other authentication methods, i.e., application default credentials.

## Request Options
```ts
interface GaxiosOptions = {
  // The url to which the request should be sent.  Required.
  url: string,

  // The HTTP method to use for the request.  Defaults to `GET`.
  method: 'GET',

  // The base Url to use for the request. Prepended to the `url` property above.
  baseURL: 'https://example.com';

  // The HTTP methods to be sent with the request.
  headers: { 'some': 'header' },

  // The data to send in the body of the request. Data objects will be
  // serialized as JSON.
  //
  // Note: if you would like to provide a Content-Type header other than
  // application/json you you must provide a string or readable stream, rather
  // than an object:
  // data: JSON.stringify({some: 'data'})
  // data: fs.readFile('./some-data.jpeg')
  data: {
    some: 'data'
  },

  // The max size of the http response content in bytes allowed.
  // Defaults to `0`, which is the same as unset.
  maxContentLength: 2000,

  // The max number of HTTP redirects to follow.
  // Defaults to 100.
  maxRedirects: 100,

  // The querystring parameters that will be encoded using `qs` and
  // appended to the url
  params: {
    querystring: 'parameters'
  },

  // By default, we use the `querystring` package in node core to serialize
  // querystring parameters.  You can override that and provide your
  // own implementation.
  paramsSerializer: (params) => {
    return qs.stringify(params);
  },

  // The timeout for the HTTP request in milliseconds. Defaults to 0.
  timeout: 1000,

  // Optional method to override making the actual HTTP request. Useful
  // for writing tests and instrumentation
  adapter?: async (options, defaultAdapter) => {
    const res = await defaultAdapter(options);
    res.data = {
      ...res.data,
      extraProperty: 'your extra property',
    };
    return res;
  };

  // The expected return type of the request.  Options are:
  // json | stream | blob | arraybuffer | text | unknown
  // Defaults to `unknown`.
  responseType: 'unknown',

  // The node.js http agent to use for the request.
  agent: someHttpsAgent,

  // Custom function to determine if the response is valid based on the
  // status code.  Defaults to (>= 200 && < 300)
  validateStatus: (status: number) => true,

  // Implementation of `fetch` to use when making the API call. By default,
  // will use the browser context if available, and fall back to `node-fetch`
  // in node.js otherwise.
  fetchImplementation?: typeof fetch;

  // Configuration for retrying of requests.
  retryConfig: {
    // The number of times to retry the request.  Defaults to 3.
    retry?: number;

    // The number of retries already attempted.
    currentRetryAttempt?: number;

    // The HTTP Methods that will be automatically retried.
    // Defaults to ['GET','PUT','HEAD','OPTIONS','DELETE']
    httpMethodsToRetry?: string[];

    // The HTTP response status codes that will automatically be retried.
    // Defaults to: [[100, 199], [408, 408], [429, 429], [500, 599]]
    statusCodesToRetry?: number[][];

    // Function to invoke when a retry attempt is made.
    onRetryAttempt?: (err: GaxiosError) => Promise<void> | void;

    // Function to invoke which determines if you should retry
    shouldRetry?: (err: GaxiosError) => Promise<boolean> | boolean;

    // When there is no response, the number of retries to attempt. Defaults to 2.
    noResponseRetries?: number;

    // The amount of time to initially delay the retry, in ms.  Defaults to 100ms.
    retryDelay?: number;
  },

  // Enables default configuration for retries.
  retry: boolean,

  // Cancelling a request requires the `abort-controller` library.
  // See https://github.com/bitinn/node-fetch#request-cancellation-with-abortsignal
  signal?: AbortSignal

  /**
   * A collection of parts to send as a `Content-Type: multipart/related` request.
   */
  multipart?: GaxiosMultipartOptions;

  /**
   * An optional proxy to use for requests.
   * Available via `process.env.HTTP_PROXY` and `process.env.HTTPS_PROXY` as well - with a preference for the this config option when multiple are available.
   * The `agent` option overrides this.
   *
   * @see {@link GaxiosOptions.noProxy}
   * @see {@link GaxiosOptions.agent}
   */
  proxy?: string | URL;
  /**
   * A list for excluding traffic for proxies.
   * Available via `process.env.NO_PROXY` as well as a common-separated list of strings - merged with any local `noProxy` rules.
   *
   * - When provided a string, it is matched by
   *   - Wildcard `*.` and `.` matching are available. (e.g. `.example.com` or `*.example.com`)
   * - When provided a URL, it is matched by the `.origin` property.
   *   - For example, requesting `https://example.com` with the following `noProxy`s would result in a no proxy use:
   *     - new URL('https://example.com')
   *     - new URL('https://example.com:443')
   *   - The following would be used with a proxy:
   *     - new URL('http://example.com:80')
   *     - new URL('https://example.com:8443')
   * - When provided a regular expression it is used to match the stringified URL
   *
   * @see {@link GaxiosOptions.proxy}
   */
  noProxy?: (string | URL | RegExp)[];

  /**
   * An experimental, customizable error redactor.
   *
   * Set `false` to disable.
   *
   * @remarks
   *
   * This does not replace the requirement for an active Data Loss Prevention (DLP) provider. For DLP suggestions, see:
   * - https://cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data#dlp_deidentify_replace_infotype-nodejs
   * - https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets
   *
   * @experimental
   */
  errorRedactor?: typeof defaultErrorRedactor | false;
}
```

## License
[Apache-2.0](https://github.com/googleapis/gaxios/blob/master/LICENSE)

---

# iCloud: web-app/node_modules/@google/generative-ai/README.md

> **Source:** icloud://web-app/node_modules/@google/generative-ai/README.md
> **Analyzed At:** 2026-06-13T06:32:47.035Z

## [Deprecated] Google AI JavaScript SDK for the Gemini API
With Gemini 2.0, we took the chance to create a single unified SDK for all developers who want to use Google's GenAI models (Gemini, Veo, Imagen, etc). As part of that process, we took all of the feedback from this SDK and what developers like about other SDKs in the ecosystem to create the [Google Gen AI SDK](https://github.com/googleapis/js-genai).
The full migration guide from the old SDK to new SDK is available in the [Gemini API docs](https://ai.google.dev/gemini-api/docs/migrate).
The Gemini API docs are fully updated to show examples of the new Google Gen AI SDK. We know how disruptive an SDK change can be and don't take this change lightly, but our goal is to create an extremely simple and clear path for developers to build with our models so it felt necessary to make this change.
Thank you for building with Gemini and [let us know](https://discuss.ai.google.dev/c/gemini-api/4) if you need any help!
**Please be advised that this repository is now considered legacy.** For the latest features, performance improvements, and active development, we strongly recommend migrating to the official **[Google Generative AI SDK for JavaScript](https://github.com/googleapis/js-genai)**.
**Support Plan for this Repository:**
*   **Limited Maintenance:** Development is now restricted to **critical bug fixes only**. No new features will be added.
*   **Purpose:** This limited support aims to provide stability for users while they transition to the new SDK.
*   **End-of-Life Date:** All support for this repository (including bug fixes) will permanently end on **August 31st, 2025**.
We encourage all users to begin planning their migration to the [Google Generative AI SDK](https://github.com/googleapis/js-genai) to ensure continued access to the latest capabilities and support.

---

# iCloud: web-app/node_modules/@google/genai/node_modules/p-retry/readme.md

> **Source:** icloud://web-app/node_modules/@google/genai/node_modules/p-retry/readme.md
> **Analyzed At:** 2026-06-13T06:32:47.044Z

## p-retry
> Retry a promise-returning or async function
It does exponential backoff and supports custom retry strategies for failed operations.

## Install
```
$ npm install p-retry
```

## Usage
```js
const pRetry = require('p-retry');
const fetch = require('node-fetch');

const run = async () => {
	const response = await fetch('https://sindresorhus.com/unicorn');

	// Abort retrying if the resource doesn't exist
	if (response.status === 404) {
		throw new pRetry.AbortError(response.statusText);
	}

	return response.blob();
};

(async () => {
	console.log(await pRetry(run, {retries: 5}));
})();
```

## pRetry(input, options?)
Returns a `Promise` that is fulfilled when calling `input` returns a fulfilled promise. If calling `input` returns a rejected promise, `input` is called again until the maximum number of retries is reached. It then rejects with the last rejection reason.
Does not retry on most `TypeErrors`, with the exception of network errors. This is done on a best case basis as different browsers have different [messages](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#Checking_that_the_fetch_was_successful) to indicate this. See [whatwg/fetch#526 (comment)](https://github.com/whatwg/fetch/issues/526#issuecomment-554604080)

## input
Type: `Function`
Receives the current attempt number as the first argument and is expected to return a `Promise` or any value.

## options
Type: `object`
Options are passed to the [`retry`](https://github.com/tim-kos/node-retry#retryoperationoptions) module.

## onFailedAttempt(error)
Type: `Function`
Callback invoked on each retry. Receives the error thrown by `input` as the first argument with properties `attemptNumber` and `retriesLeft` which indicate the current attempt number and the number of attempts left, respectively.
```js
const run = async () => {
	const response = await fetch('https://sindresorhus.com/unicorn');

	if (!response.ok) {
		throw new Error(response.statusText);
	}

	return response.json();
};

(async () => {
	const result = await pRetry(run, {
		onFailedAttempt: error => {
			console.log(`Attempt ${error.attemptNumber} failed. There are ${error.retriesLeft} retries left.`);
			// 1st request => Attempt 1 failed. There are 4 retries left.
			// 2nd request => Attempt 2 failed. There are 3 retries left.
			// …
		},
		retries: 5
	});

	console.log(result);
})();
```
The `onFailedAttempt` function can return a promise. For example, you can do some async logging:
```js
const pRetry = require('p-retry');
const logger = require('./some-logger');

const run = async () => { … };

(async () => {
	const result = await pRetry(run, {
		onFailedAttempt: async error => {
			await logger.log(error);
		}
	});
})();
```
If the `onFailedAttempt` function throws, all retries will be aborted and the original promise will reject with the thrown error.

## pRetry.AbortError(error)
Abort retrying and reject the promise.

## message
Type: `string`
Error message.

## error
Type: `Error`
Custom error.

## Tip
You can pass arguments to the function being retried by wrapping it in an inline arrow function:
```js
const pRetry = require('p-retry');

const run = async emoji => {
	// …
};

(async () => {
	// Without arguments
	await pRetry(run, {retries: 5});

	// With arguments
	await pRetry(() => run('🦄'), {retries: 5});
})();
```

## Related
- [p-timeout](https://github.com/sindresorhus/p-timeout) - Timeout a promise after a specified amount of time
- [More…](https://github.com/sindresorhus/promise-fun)

---

# iCloud: web-app/node_modules/@google/adk/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/README.md
> **Analyzed At:** 2026-06-13T06:32:47.049Z

## @google/adk
Please see README for adk-js at https://github.com/google/adk-js

---

# iCloud: web-app/node_modules/@google/adk/node_modules/type-is/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/type-is/README.md
> **Analyzed At:** 2026-06-13T06:32:47.060Z

## type-is
[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][travis-image]][travis-url]
[![Test Coverage][coveralls-image]][coveralls-url]
Infer the content-type of a request.

## Install
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```sh
$ npm install type-is
```

## API
```js
var http = require('http')
var typeis = require('type-is')

http.createServer(function (req, res) {
  var istext = typeis(req, ['text/*'])
  res.end('you ' + (istext ? 'sent' : 'did not send') + ' me text')
})
```

## typeis(request, types)
Checks if the `request` is one of the `types`. If the request has no body,
even if there is a `Content-Type` header, then `null` is returned. If the
`Content-Type` header is invalid or does not matches any of the `types`, then
`false` is returned. Otherwise, a string of the type that matched is returned.
The `request` argument is expected to be a Node.js HTTP request. The `types`
argument is an array of type strings.
Each type in the `types` array can be one of the following:
- A file extension name such as `json`. This name will be returned if matched.
- A mime type such as `application/json`.
- A mime type with a wildcard such as `*/*` or `*/json` or `application/*`.
The full mime type will be returned if matched.
- A suffix such as `+json`. This can be combined with a wildcard such as
`*/vnd+json` or `application/*+json`. The full mime type will be returned
if matched.
Some examples to illustrate the inputs and returned value:
```js
// req.headers.content-type = 'application/json'

typeis(req, ['json']) // => 'json'
typeis(req, ['html', 'json']) // => 'json'
typeis(req, ['application/*']) // => 'application/json'
typeis(req, ['application/json']) // => 'application/json'

typeis(req, ['html']) // => false
```

## typeis.hasBody(request)
Returns a Boolean if the given `request` has a body, regardless of the
`Content-Type` header.
Having a body has no relation to how large the body is (it may be 0 bytes).
This is similar to how file existence works. If a body does exist, then this
indicates that there is data to read from the Node.js request stream.
```js
if (typeis.hasBody(req)) {
  // read the body, since there is one

  req.on('data', function (chunk) {
    // ...
  })
}
```

## typeis.is(mediaType, types)
Checks if the `mediaType` is one of the `types`. If the `mediaType` is invalid
or does not matches any of the `types`, then `false` is returned. Otherwise, a
string of the type that matched is returned.
The `mediaType` argument is expected to be a
[media type](https://tools.ietf.org/html/rfc6838) string. The `types` argument
is an array of type strings.
Each type in the `types` array can be one of the following:
- A file extension name such as `json`. This name will be returned if matched.
- A mime type such as `application/json`.
- A mime type with a wildcard such as `*/*` or `*/json` or `application/*`.
The full mime type will be returned if matched.
- A suffix such as `+json`. This can be combined with a wildcard such as
`*/vnd+json` or `application/*+json`. The full mime type will be returned
if matched.
Some examples to illustrate the inputs and returned value:
```js
var mediaType = 'application/json'

typeis.is(mediaType, ['json']) // => 'json'
typeis.is(mediaType, ['html', 'json']) // => 'json'
typeis.is(mediaType, ['application/*']) // => 'application/json'
typeis.is(mediaType, ['application/json']) // => 'application/json'

typeis.is(mediaType, ['html']) // => false
```

## Example body parser
```js
var express = require('express')
var typeis = require('type-is')

var app = express()

app.use(function bodyParser (req, res, next) {
  if (!typeis.hasBody(req)) {
    return next()
  }

  switch (typeis(req, ['urlencoded', 'json', 'multipart'])) {
    case 'urlencoded':
      // parse urlencoded body
      throw new Error('implement urlencoded body parsing')
    case 'json':
      // parse json body
      throw new Error('implement json body parsing')
    case 'multipart':
      // parse multipart body
      throw new Error('implement multipart body parsing')
    default:
      // 415 error code
      res.statusCode = 415
      res.end()
      break
  }
})
```

## License
[MIT](LICENSE)
[coveralls-image]: https://badgen.net/coveralls/c/github/jshttp/type-is/master
[coveralls-url]: https://coveralls.io/r/jshttp/type-is?branch=master
[node-version-image]: https://badgen.net/npm/node/type-is
[node-version-url]: https://nodejs.org/en/download
[npm-downloads-image]: https://badgen.net/npm/dm/type-is
[npm-url]: https://npmjs.org/package/type-is
[npm-version-image]: https://badgen.net/npm/v/type-is
[travis-image]: https://badgen.net/travis/jshttp/type-is/master
[travis-url]: https://travis-ci.org/jshttp/type-is

---

# iCloud: web-app/node_modules/@google/adk/node_modules/serve-static/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/serve-static/README.md
> **Analyzed At:** 2026-06-13T06:32:47.071Z

## serve-static
[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-url]
[![Linux Build][github-actions-ci-image]][github-actions-ci-url]
[![Windows Build][appveyor-image]][appveyor-url]
[![Test Coverage][coveralls-image]][coveralls-url]

## Install
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```sh
$ npm install serve-static
```

## API
```js
var serveStatic = require('serve-static')
```

## serveStatic(root, options)
Create a new middleware function to serve files from within a given root
directory. The file to serve will be determined by combining `req.url`
with the provided root directory. When a file is not found, instead of
sending a 404 response, this module will instead call `next()` to move on
to the next middleware, allowing for stacking and fall-backs.

## acceptRanges
Enable or disable accepting ranged requests, defaults to true.
Disabling this will not send `Accept-Ranges` and ignore the contents
of the `Range` request header.

## cacheControl
Enable or disable setting `Cache-Control` response header, defaults to
true. Disabling this will ignore the `immutable` and `maxAge` options.

## dotfiles
Set how "dotfiles" are treated when encountered. A dotfile is a file
or directory that begins with a dot ("."). Note this check is done on
the path itself without checking if the path actually exists on the
disk. If `root` is specified, only the dotfiles above the root are
checked (i.e. the root itself can be within a dotfile when set
to "deny").
- `'allow'` No special treatment for dotfiles.
- `'deny'` Deny a request for a dotfile and 403/`next()`.
- `'ignore'` Pretend like the dotfile does not exist and 404/`next()`.
The default value is similar to `'ignore'`, with the exception that this
default will not ignore the files within a directory that begins with a dot.

## etag
Enable or disable etag generation, defaults to true.

## extensions
Set file extension fallbacks. When set, if a file is not found, the given
extensions will be added to the file name and search for. The first that
exists will be served. Example: `['html', 'htm']`.
The default value is `false`.

## fallthrough
Set the middleware to have client errors fall-through as just unhandled
requests, otherwise forward a client error. The difference is that client
errors like a bad request or a request to a non-existent file will cause
this middleware to simply `next()` to your next middleware when this value
is `true`. When this value is `false`, these errors (even 404s), will invoke
`next(err)`.
Typically `true` is desired such that multiple physical directories can be
mapped to the same web address or for routes to fill in non-existent files.
The value `false` can be used if this middleware is mounted at a path that
is designed to be strictly a single file system directory, which allows for
short-circuiting 404s for less overhead. This middleware will also reply to
all methods.
The default value is `true`.

## immutable
Enable or disable the `immutable` directive in the `Cache-Control` response
header, defaults to `false`. If set to `true`, the `maxAge` option should
also be specified to enable caching. The `immutable` directive will prevent
supported clients from making conditional requests during the life of the
`maxAge` option to check if the file has changed.

## index
By default this module will send "index.html" files in response to a request
on a directory. To disable this set `false` or to supply a new index pass a
string or an array in preferred order.

## lastModified
Enable or disable `Last-Modified` header, defaults to true. Uses the file
system's last modified value.

## maxAge
Provide a max-age in milliseconds for http caching, defaults to 0. This
can also be a string accepted by the [ms](https://www.npmjs.org/package/ms#readme)
module.

## redirect
Redirect to trailing "/" when the pathname is a dir. Defaults to `true`.

## setHeaders
Function to set custom headers on response. Alterations to the headers need to
occur synchronously. The function is called as `fn(res, path, stat)`, where
the arguments are:
- `res` the response object
- `path` the file path that is being sent
- `stat` the stat object of the file that is being sent

## Serve files with vanilla node.js http server
```js
var finalhandler = require('finalhandler')
var http = require('http')
var serveStatic = require('serve-static')

// Serve up public/ftp folder
var serve = serveStatic('public/ftp', { index: ['index.html', 'index.htm'] })

// Create server
var server = http.createServer(function onRequest (req, res) {
  serve(req, res, finalhandler(req, res))
})

// Listen
server.listen(3000)
```

## Serve all files as downloads
```js
var contentDisposition = require('content-disposition')
var finalhandler = require('finalhandler')
var http = require('http')
var serveStatic = require('serve-static')

// Serve up public/ftp folder
var serve = serveStatic('public/ftp', {
  index: false,
  setHeaders: setHeaders
})

// Set header to force download
function setHeaders (res, path) {
  res.setHeader('Content-Disposition', contentDisposition(path))
}

// Create server
var server = http.createServer(function onRequest (req, res) {
  serve(req, res, finalhandler(req, res))
})

// Listen
server.listen(3000)
```

## Simple
This is a simple example of using Express.
```js
var express = require('express')
var serveStatic = require('serve-static')

var app = express()

app.use(serveStatic('public/ftp', { index: ['default.html', 'default.htm'] }))
app.listen(3000)
```

## Multiple roots
This example shows a simple way to search through multiple directories.
Files are searched for in `public-optimized/` first, then `public/` second
as a fallback.
```js
var express = require('express')
var path = require('path')
var serveStatic = require('serve-static')

var app = express()

app.use(serveStatic(path.join(__dirname, 'public-optimized')))
app.use(serveStatic(path.join(__dirname, 'public')))
app.listen(3000)
```

## Different settings for paths
This example shows how to set a different max age depending on the served
file type. In this example, HTML files are not cached, while everything else
is for 1 day.
```js
var express = require('express')
var path = require('path')
var serveStatic = require('serve-static')

var app = express()

app.use(serveStatic(path.join(__dirname, 'public'), {
  maxAge: '1d',
  setHeaders: setCustomCacheControl
}))

app.listen(3000)

function setCustomCacheControl (res, path) {
  if (serveStatic.mime.lookup(path) === 'text/html') {
    // Custom Cache-Control for HTML files
    res.setHeader('Cache-Control', 'public, max-age=0')
  }
}
```

## License
[MIT](LICENSE)
[appveyor-image]: https://badgen.net/appveyor/ci/dougwilson/serve-static/master?label=windows
[appveyor-url]: https://ci.appveyor.com/project/dougwilson/serve-static
[coveralls-image]: https://badgen.net/coveralls/c/github/expressjs/serve-static/master
[coveralls-url]: https://coveralls.io/r/expressjs/serve-static?branch=master
[github-actions-ci-image]: https://badgen.net/github/checks/expressjs/serve-static/master?label=linux
[github-actions-ci-url]: https://github.com/expressjs/serve-static/actions/workflows/ci.yml
[node-image]: https://badgen.net/npm/node/serve-static
[node-url]: https://nodejs.org/en/download/
[npm-downloads-image]: https://badgen.net/npm/dm/serve-static
[npm-url]: https://npmjs.org/package/serve-static
[npm-version-image]: https://badgen.net/npm/v/serve-static

---

# iCloud: web-app/node_modules/@google/adk/node_modules/send/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/send/README.md
> **Analyzed At:** 2026-06-13T06:32:47.081Z

## send
[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-url]
[![Linux Build][github-actions-ci-image]][github-actions-ci-url]
[![Windows Build][appveyor-image]][appveyor-url]
[![Test Coverage][coveralls-image]][coveralls-url]
Send is a library for streaming files from the file system as a http response
supporting partial responses (Ranges), conditional-GET negotiation (If-Match,
If-Unmodified-Since, If-None-Match, If-Modified-Since), high test coverage,
and granular events which may be leveraged to take appropriate actions in your
application or framework.
Looking to serve up entire folders mapped to URLs? Try [serve-static](https://www.npmjs.org/package/serve-static).

## Installation
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```bash
$ npm install send
```

## API
```js
var send = require('send')
```

## send(req, path, [options])
Create a new `SendStream` for the given path to send to a `res`. The `req` is
the Node.js HTTP request and the `path` is a urlencoded path to send (urlencoded,
not the actual file-system path).

## acceptRanges
Enable or disable accepting ranged requests, defaults to true.
Disabling this will not send `Accept-Ranges` and ignore the contents
of the `Range` request header.

## cacheControl
Enable or disable setting `Cache-Control` response header, defaults to
true. Disabling this will ignore the `immutable` and `maxAge` options.

## dotfiles
Set how "dotfiles" are treated when encountered. A dotfile is a file
or directory that begins with a dot ("."). Note this check is done on
the path itself without checking if the path actually exists on the
disk. If `root` is specified, only the dotfiles above the root are
checked (i.e. the root itself can be within a dotfile when when set
to "deny").
- `'allow'` No special treatment for dotfiles.
- `'deny'` Send a 403 for any request for a dotfile.
- `'ignore'` Pretend like the dotfile does not exist and 404.
The default value is _similar_ to `'ignore'`, with the exception that
this default will not ignore the files within a directory that begins
with a dot, for backward-compatibility.

## end
Byte offset at which the stream ends, defaults to the length of the file
minus 1. The end is inclusive in the stream, meaning `end: 3` will include
the 4th byte in the stream.

## etag
Enable or disable etag generation, defaults to true.

## extensions
If a given file doesn't exist, try appending one of the given extensions,
in the given order. By default, this is disabled (set to `false`). An
example value that will serve extension-less HTML files: `['html', 'htm']`.
This is skipped if the requested file already has an extension.

## immutable
Enable or disable the `immutable` directive in the `Cache-Control` response
header, defaults to `false`. If set to `true`, the `maxAge` option should
also be specified to enable caching. The `immutable` directive will prevent
supported clients from making conditional requests during the life of the
`maxAge` option to check if the file has changed.

## index
By default send supports "index.html" files, to disable this
set `false` or to supply a new index pass a string or an array
in preferred order.

## lastModified
Enable or disable `Last-Modified` header, defaults to true. Uses the file
system's last modified value.

## maxAge
Provide a max-age in milliseconds for http caching, defaults to 0.
This can also be a string accepted by the
[ms](https://www.npmjs.org/package/ms#readme) module.

## root
Serve files relative to `path`.

## start
Byte offset at which the stream starts, defaults to 0. The start is inclusive,
meaning `start: 2` will include the 3rd byte in the stream.

## Events
The `SendStream` is an event emitter and will emit the following events:
- `error` an error occurred `(err)`
- `directory` a directory was requested `(res, path)`
- `file` a file was requested `(path, stat)`
- `headers` the headers are about to be set on a file `(res, path, stat)`
- `stream` file streaming has started `(stream)`
- `end` streaming has completed

## .pipe
The `pipe` method is used to pipe the response into the Node.js HTTP response
object, typically `send(req, path, options).pipe(res)`.

## .mime
The `mime` export is the global instance of of the
[`mime` npm module](https://www.npmjs.com/package/mime).
This is used to configure the MIME types that are associated with file extensions
as well as other options for how to resolve the MIME type of a file (like the
default type to use for an unknown file extension).

## Error-handling
By default when no `error` listeners are present an automatic response will be
made, otherwise you have full control over the response, aka you may show a 5xx
page etc.

## Caching
It does _not_ perform internal caching, you should use a reverse proxy cache
such as Varnish for this, or those fancy things called CDNs. If your
application is small enough that it would benefit from single-node memory
caching, it's small enough that it does not need caching at all ;).

## Debugging
To enable `debug()` instrumentation output export __DEBUG__:
```
$ DEBUG=send node app
```

## Running tests
```
$ npm install
$ npm test
```

## Serve a specific file
This simple example will send a specific file to all requests.
```js
var http = require('http')
var send = require('send')

var server = http.createServer(function onRequest (req, res) {
  send(req, '/path/to/index.html')
    .pipe(res)
})

server.listen(3000)
```

## Serve all files from a directory
This simple example will just serve up all the files in a
given directory as the top-level. For example, a request
`GET /foo.txt` will send back `/www/public/foo.txt`.
```js
var http = require('http')
var parseUrl = require('parseurl')
var send = require('send')

var server = http.createServer(function onRequest (req, res) {
  send(req, parseUrl(req).pathname, { root: '/www/public' })
    .pipe(res)
})

server.listen(3000)
```

## Custom file types
```js
var http = require('http')
var parseUrl = require('parseurl')
var send = require('send')

// Default unknown types to text/plain
send.mime.default_type = 'text/plain'

// Add a custom type
send.mime.define({
  'application/x-my-type': ['x-mt', 'x-mtt']
})

var server = http.createServer(function onRequest (req, res) {
  send(req, parseUrl(req).pathname, { root: '/www/public' })
    .pipe(res)
})

server.listen(3000)
```

## Custom directory index view
This is a example of serving up a structure of directories with a
custom function to render a listing of a directory.
```js
var http = require('http')
var fs = require('fs')
var parseUrl = require('parseurl')
var send = require('send')

// Transfer arbitrary files from within /www/example.com/public/*
// with a custom handler for directory listing
var server = http.createServer(function onRequest (req, res) {
  send(req, parseUrl(req).pathname, { index: false, root: '/www/public' })
    .once('directory', directory)
    .pipe(res)
})

server.listen(3000)

// Custom directory handler
function directory (res, path) {
  var stream = this

  // redirect to trailing slash for consistent url
  if (!stream.hasTrailingSlash()) {
    return stream.redirect(path)
  }

  // get directory list
  fs.readdir(path, function onReaddir (err, list) {
    if (err) return stream.error(err)

    // render an index for the directory
    res.setHeader('Content-Type', 'text/plain; charset=UTF-8')
    res.end(list.join('\n') + '\n')
  })
}
```

## Serving from a root directory with custom error-handling
```js
var http = require('http')
var parseUrl = require('parseurl')
var send = require('send')

var server = http.createServer(function onRequest (req, res) {
  // your custom error-handling logic:
  function error (err) {
    res.statusCode = err.status || 500
    res.end(err.message)
  }

  // your custom headers
  function headers (res, path, stat) {
    // serve all files for download
    res.setHeader('Content-Disposition', 'attachment')
  }

  // your custom directory handling logic:
  function redirect () {
    res.statusCode = 301
    res.setHeader('Location', req.url + '/')
    res.end('Redirecting to ' + req.url + '/')
  }

  // transfer arbitrary files from within
  // /www/example.com/public/*
  send(req, parseUrl(req).pathname, { root: '/www/public' })
    .on('error', error)
    .on('directory', redirect)
    .on('headers', headers)
    .pipe(res)
})

server.listen(3000)
```

## License
[MIT](LICENSE)
[appveyor-image]: https://badgen.net/appveyor/ci/dougwilson/send/master?label=windows
[appveyor-url]: https://ci.appveyor.com/project/dougwilson/send
[coveralls-image]: https://badgen.net/coveralls/c/github/pillarjs/send/master
[coveralls-url]: https://coveralls.io/r/pillarjs/send?branch=master
[github-actions-ci-image]: https://badgen.net/github/checks/pillarjs/send/master?label=linux
[github-actions-ci-url]: https://github.com/pillarjs/send/actions/workflows/ci.yml
[node-image]: https://badgen.net/npm/node/send
[node-url]: https://nodejs.org/en/download/
[npm-downloads-image]: https://badgen.net/npm/dm/send
[npm-url]: https://npmjs.org/package/send
[npm-version-image]: https://badgen.net/npm/v/send

---

# iCloud: web-app/node_modules/@google/adk/node_modules/send/SECURITY.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/send/SECURITY.md
> **Analyzed At:** 2026-06-13T06:32:47.087Z

## Reporting a Bug
The `send` team and community take all security bugs seriously. Thank you
for improving the security of Express. We appreciate your efforts and
responsible disclosure and will make every effort to acknowledge your
contributions.
Report security bugs by emailing the current owner(s) of `send`. This information
can be found in the npm registry using the command `npm owner ls send`.
If unsure or unable to get the information from the above, open an issue
in the [project issue tracker](https://github.com/pillarjs/send/issues)
asking for the current contact information.
To ensure the timely response to your report, please ensure that the entirety
of the report is contained within the email body and not solely behind a web
link or an attachment.
At least one owner will acknowledge your email within 48 hours, and will send a
more detailed response within 48 hours indicating the next steps in handling
your report. After the initial reply to your report, the owners will
endeavor to keep you informed of the progress towards a fix and full
announcement, and may ask for additional information or guidance.

---

# iCloud: web-app/node_modules/@google/adk/node_modules/raw-body/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/raw-body/README.md
> **Analyzed At:** 2026-06-13T06:32:47.093Z

## raw-body
[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build status][github-actions-ci-image]][github-actions-ci-url]
[![Test coverage][coveralls-image]][coveralls-url]
Gets the entire buffer of a stream either as a `Buffer` or a string.
Validates the stream's length against an expected length and maximum limit.
Ideal for parsing request bodies.

## Install
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```sh
$ npm install raw-body
```

## TypeScript
This module includes a [TypeScript](https://www.typescriptlang.org/)
declaration file to enable auto complete in compatible editors and type
information for TypeScript projects. This module depends on the Node.js
types, so install `@types/node`:
```sh
$ npm install @types/node
```

## API
```js
var getRawBody = require('raw-body')
```

## getRawBody(stream, [options], [callback])
**Returns a promise if no callback specified and global `Promise` exists.**
Options:
- `length` - The length of the stream.
If the contents of the stream do not add up to this length,
an `400` error code is returned.
- `limit` - The byte limit of the body.
This is the number of bytes or any string format supported by
[bytes](https://www.npmjs.com/package/bytes),
for example `1000`, `'500kb'` or `'3mb'`.
If the body ends up being larger than this limit,
a `413` error code is returned.
- `encoding` - The encoding to use to decode the body into a string.
By default, a `Buffer` instance will be returned when no encoding is specified.
Most likely, you want `utf-8`, so setting `encoding` to `true` will decode as `utf-8`.
You can use any type of encoding supported by [iconv-lite](https://www.npmjs.org/package/iconv-lite#readme).
You can also pass a string in place of options to just specify the encoding.
If an error occurs, the stream will be paused, everything unpiped,
and you are responsible for correctly disposing the stream.
For HTTP requests, you may need to finish consuming the stream if
you want to keep the socket open for future requests. For streams
that use file descriptors, you should `stream.destroy()` or
`stream.close()` to prevent leaks.

## Errors
This module creates errors depending on the error condition during reading.
The error may be an error from the underlying Node.js implementation, but is
otherwise an error created by this module, which has the following attributes:
* `limit` - the limit in bytes
* `length` and `expected` - the expected length of the stream
* `received` - the received bytes
* `encoding` - the invalid encoding
* `status` and `statusCode` - the corresponding status code for the error
* `type` - the error type

## Types
The errors from this module have a `type` property which allows for the programmatic
determination of the type of error returned.

## encoding.unsupported
This error will occur when the `encoding` option is specified, but the value does
not map to an encoding supported by the [iconv-lite](https://www.npmjs.org/package/iconv-lite#readme)
module.

## entity.too.large
This error will occur when the `limit` option is specified, but the stream has
an entity that is larger.

## request.aborted
This error will occur when the request stream is aborted by the client before
reading the body has finished.

## request.size.invalid
This error will occur when the `length` option is specified, but the stream has
emitted more bytes.

## stream.encoding.set
This error will occur when the given stream has an encoding set on it, making it
a decoded stream. The stream should not have an encoding set and is expected to
emit `Buffer` objects.

## stream.not.readable
This error will occur when the given stream is not readable.

## Simple Express example
```js
var contentType = require('content-type')
var express = require('express')
var getRawBody = require('raw-body')

var app = express()

app.use(function (req, res, next) {
  getRawBody(req, {
    length: req.headers['content-length'],
    limit: '1mb',
    encoding: contentType.parse(req).parameters.charset
  }, function (err, string) {
    if (err) return next(err)
    req.text = string
    next()
  })
})

// now access req.text
```

## Simple Koa example
```js
var contentType = require('content-type')
var getRawBody = require('raw-body')
var koa = require('koa')

var app = koa()

app.use(function * (next) {
  this.text = yield getRawBody(this.req, {
    length: this.req.headers['content-length'],
    limit: '1mb',
    encoding: contentType.parse(this.req).parameters.charset
  })
  yield next
})

// now access this.text
```

## Using as a promise
To use this library as a promise, simply omit the `callback` and a promise is
returned, provided that a global `Promise` is defined.
```js
var getRawBody = require('raw-body')
var http = require('http')

var server = http.createServer(function (req, res) {
  getRawBody(req)
    .then(function (buf) {
      res.statusCode = 200
      res.end(buf.length + ' bytes submitted')
    })
    .catch(function (err) {
      res.statusCode = 500
      res.end(err.message)
    })
})

server.listen(3000)
```

## Using with TypeScript
```ts
import * as getRawBody from 'raw-body';
import * as http from 'http';

const server = http.createServer((req, res) => {
  getRawBody(req)
  .then((buf) => {
    res.statusCode = 200;
    res.end(buf.length + ' bytes submitted');
  })
  .catch((err) => {
    res.statusCode = err.statusCode;
    res.end(err.message);
  });
});

server.listen(3000);
```

## License
[MIT](LICENSE)
[npm-image]: https://img.shields.io/npm/v/raw-body.svg
[npm-url]: https://npmjs.org/package/raw-body
[node-version-image]: https://img.shields.io/node/v/raw-body.svg
[node-version-url]: https://nodejs.org/en/download/
[coveralls-image]: https://img.shields.io/coveralls/stream-utils/raw-body/master.svg
[coveralls-url]: https://coveralls.io/r/stream-utils/raw-body?branch=master
[downloads-image]: https://img.shields.io/npm/dm/raw-body.svg
[downloads-url]: https://npmjs.org/package/raw-body
[github-actions-ci-image]: https://img.shields.io/github/actions/workflow/status/stream-utils/raw-body/ci.yml?branch=master&label=ci
[github-actions-ci-url]: https://github.com/jshttp/stream-utils/raw-body?query=workflow%3Aci

---

# iCloud: web-app/node_modules/@google/adk/node_modules/qs/.github/SECURITY.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/qs/.github/SECURITY.md
> **Analyzed At:** 2026-06-13T06:32:47.105Z

## Security
Please file a private vulnerability report via GitHub, email [@ljharb](https://github.com/ljharb), or see https://tidelift.com/security if you have a potential security vulnerability to report.

## Incident Response Plan
Please see our [Incident Response Plan](https://github.com/ljharb/.github/blob/main/INCIDENT_RESPONSE_PLAN.md).

## Threat Model
Please see [THREAT_MODEL.md](./THREAT_MODEL.md).

---

# iCloud: web-app/node_modules/@google/adk/node_modules/qs/.github/THREAT_MODEL.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/qs/.github/THREAT_MODEL.md
> **Analyzed At:** 2026-06-13T06:32:47.111Z

## 1. Library Overview
- **Library Name:** qs
- **Brief Description:** A JavaScript library for parsing and stringifying URL query strings, supporting nested objects and arrays. It is widely used in Node.js and web applications for processing query parameters[2][6][8].
- **Key Public APIs/Functions:** `qs.parse()`, `qs.stringify()`

## 2. Define Scope
This threat model focuses on the core parsing and stringifying functionality, specifically the handling of nested objects and arrays, option validation, and cycle management in stringification.

## 3. Conceptual System Diagram
```
Caller Application → qs.parse(input, options) → Parsing Engine → Output Object
                           │
                           └→ Options Handling

Caller Application → qs.stringify(obj, options) → Stringifying Engine → Output String
                           │
                           └→ Options Handling
                           └→ Cycle Tracking
```
**Trust Boundaries:**
- **Input string (parse):** May come from untrusted sources (e.g., user input, network requests)
- **Input object (stringify):** May contain cycles, which can lead to infinite loops during stringification
- **Options:** Provided by the caller
- **Cycle Tracking:** Used only during stringification to detect and handle circular references

## 4. Identify Assets
- **Integrity of parsed output:** Prevent malicious manipulation of the output object structure, especially ensuring builtins/globals are not modified as a result of parse[3][4][8].
- **Confidentiality of processed data:** Avoid leaking sensitive information through errors or output.
- **Availability/performance for host application:** Prevent crashes or resource exhaustion in the consuming application.
- **Security of host application:** Prevent the library from being a vector for attacks (e.g., prototype pollution, DoS).
- **Reputation of library:** Maintain trust by avoiding supply chain attacks and vulnerabilities[1].

## 5. Identify Threats
| Component / API / Interaction         | S  | T  | R  | I  | D  | E  |
|---------------------------------------|----|----|----|----|----|----|
| Public API Call (`parse`)             | –  | ✓  | –  | ✓  | ✓  | ✓  |
| Public API Call (`stringify`)         | –  | ✓  | –  | ✓  | ✓  | –  |
| Options Handling                      | ✓  | ✓  | –  | ✓  | –  | ✓  |
| Dependency Interaction                | –  | –  | –  | –  | ✓  | –  |
**Key Threats:**
- **Tampering:** Malicious input can, if not prevented, alter parsed output (e.g., prototype pollution via `__proto__`, modification of builtins/globals)[3][4][8].
- **Information Disclosure:** Error messages may expose internal details or sensitive data.
- **Denial of Service:** Large or malformed input can exhaust memory or CPU.
- **Elevation of Privilege:** Prototype pollution can lead to unintended privilege escalation in the host application[3][4][8].

## 6. Mitigation/Countermeasures
| Threat Identified                                 | Proposed Mitigation |
|---------------------------------------------------|---------------------|
| Tampering (malicious input, prototype pollution)  | Strict input validation; keep `allowPrototypes: false` by default; use `plainObjects` for output; ensure builtins/globals are never modified by parse[4][8]. |
| Information Disclosure (error messages)           | Generic error messages without stack traces or internal paths. |
| Denial of Service (memory/CPU exhaustion)         | Enforce `arrayLimit` and `parameterLimit` with safe defaults; enable `throwOnLimitExceeded`; limit nesting depth[7]. |
| Elevation of Privilege (prototype pollution)      | Keep `allowPrototypes: false`; validate options against allowlist; use `plainObjects` to avoid prototype pollution[4][8]. |

## 7. Risk Ranking
- **High:** Denial of Service via array parsing or malformed input (historical vulnerability)
- **Medium:** Prototype pollution via options or input (if `allowPrototypes` enabled)
- **Low:** Information disclosure in errors

## 8. Next Steps & Review
1. **Audit option validation logic.**
2. **Add depth limiting to nested parsing and stringification.**
3. **Implement fuzz testing for parser and stringifier edge cases.**
4. **Regularly review dependencies for vulnerabilities.**
5. **Keep documentation and threat model up to date.**
6. **Ensure builtins/globals are never modified as a result of parse.**
7. **Support round-trip consistency between parse and stringify as a non-security goal, with the right options[5][9].**

---

# iCloud: web-app/node_modules/@google/adk/node_modules/path-to-regexp/Readme.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/path-to-regexp/Readme.md
> **Analyzed At:** 2026-06-13T06:32:47.117Z

## Path-to-RegExp
Turn an Express-style path string such as `/user/:name` into a regular expression.
**Note:** This is a legacy branch. You should upgrade to `1.x`.

## Usage
```javascript
var pathToRegexp = require('path-to-regexp');
```

## pathToRegexp(path, keys, options)
- **path** A string in the express format, an array of such strings, or a regular expression
- **keys** An array to be populated with the keys present in the url.  Once the function completes, this will be an array of strings.
- **options**
- **options.sensitive** Defaults to false, set this to true to make routes case sensitive
- **options.strict** Defaults to false, set this to true to make the trailing slash matter.
- **options.end** Defaults to true, set this to false to only match the prefix of the URL.
```javascript
var keys = [];
var exp = pathToRegexp('/foo/:bar', keys);
//keys = ['bar']
//exp = /^\/foo\/(?:([^\/]+?))\/?$/i
```

## Live Demo
You can see a live demo of this library in use at [express-route-tester](http://forbeslindesay.github.com/express-route-tester/).

---

# iCloud: web-app/node_modules/@google/adk/node_modules/negotiator/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/negotiator/README.md
> **Analyzed At:** 2026-06-13T06:32:47.128Z

## negotiator
[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][github-actions-ci-image]][github-actions-ci-url]
[![Test Coverage][coveralls-image]][coveralls-url]
An HTTP content negotiator for Node.js

## Installation
```sh
$ npm install negotiator
```

## API
```js
var Negotiator = require('negotiator')
```

## Accept Negotiation
```js
availableMediaTypes = ['text/html', 'text/plain', 'application/json']

// The negotiator constructor receives a request object
negotiator = new Negotiator(request)

// Let's say Accept header is 'text/html, application/*;q=0.2, image/jpeg;q=0.8'

negotiator.mediaTypes()
// -> ['text/html', 'image/jpeg', 'application/*']

negotiator.mediaTypes(availableMediaTypes)
// -> ['text/html', 'application/json']

negotiator.mediaType(availableMediaTypes)
// -> 'text/html'
```
You can check a working example at `examples/accept.js`.

## mediaType()
Returns the most preferred media type from the client.

## mediaType(availableMediaType)
Returns the most preferred media type from a list of available media types.

## mediaTypes()
Returns an array of preferred media types ordered by the client preference.

## mediaTypes(availableMediaTypes)
Returns an array of preferred media types ordered by priority from a list of
available media types.

## Accept-Language Negotiation
```js
negotiator = new Negotiator(request)

availableLanguages = ['en', 'es', 'fr']

// Let's say Accept-Language header is 'en;q=0.8, es, pt'

negotiator.languages()
// -> ['es', 'pt', 'en']

negotiator.languages(availableLanguages)
// -> ['es', 'en']

language = negotiator.language(availableLanguages)
// -> 'es'
```
You can check a working example at `examples/language.js`.

## language()
Returns the most preferred language from the client.

## language(availableLanguages)
Returns the most preferred language from a list of available languages.

## languages()
Returns an array of preferred languages ordered by the client preference.

## languages(availableLanguages)
Returns an array of preferred languages ordered by priority from a list of
available languages.

## Accept-Charset Negotiation
```js
availableCharsets = ['utf-8', 'iso-8859-1', 'iso-8859-5']

negotiator = new Negotiator(request)

// Let's say Accept-Charset header is 'utf-8, iso-8859-1;q=0.8, utf-7;q=0.2'

negotiator.charsets()
// -> ['utf-8', 'iso-8859-1', 'utf-7']

negotiator.charsets(availableCharsets)
// -> ['utf-8', 'iso-8859-1']

negotiator.charset(availableCharsets)
// -> 'utf-8'
```
You can check a working example at `examples/charset.js`.

## charset()
Returns the most preferred charset from the client.

## charset(availableCharsets)
Returns the most preferred charset from a list of available charsets.

## charsets()
Returns an array of preferred charsets ordered by the client preference.

## charsets(availableCharsets)
Returns an array of preferred charsets ordered by priority from a list of
available charsets.

## Accept-Encoding Negotiation
```js
availableEncodings = ['identity', 'gzip']

negotiator = new Negotiator(request)

// Let's say Accept-Encoding header is 'gzip, compress;q=0.2, identity;q=0.5'

negotiator.encodings()
// -> ['gzip', 'identity', 'compress']

negotiator.encodings(availableEncodings)
// -> ['gzip', 'identity']

negotiator.encoding(availableEncodings)
// -> 'gzip'
```
You can check a working example at `examples/encoding.js`.

## encoding()
Returns the most preferred encoding from the client.

## encoding(availableEncodings)
Returns the most preferred encoding from a list of available encodings.

## encodings()
Returns an array of preferred encodings ordered by the client preference.

## encodings(availableEncodings)
Returns an array of preferred encodings ordered by priority from a list of
available encodings.

## See Also
The [accepts](https://npmjs.org/package/accepts#readme) module builds on
this module and provides an alternative interface, mime type validation,
and more.

## License
[MIT](LICENSE)
[npm-image]: https://img.shields.io/npm/v/negotiator.svg
[npm-url]: https://npmjs.org/package/negotiator
[node-version-image]: https://img.shields.io/node/v/negotiator.svg
[node-version-url]: https://nodejs.org/en/download/
[coveralls-image]: https://img.shields.io/coveralls/jshttp/negotiator/master.svg
[coveralls-url]: https://coveralls.io/r/jshttp/negotiator?branch=master
[downloads-image]: https://img.shields.io/npm/dm/negotiator.svg
[downloads-url]: https://npmjs.org/package/negotiator
[github-actions-ci-image]: https://img.shields.io/github/workflow/status/jshttp/negotiator/ci/master?label=ci
[github-actions-ci-url]: https://github.com/jshttp/negotiator/actions/workflows/ci.yml

---

# iCloud: web-app/node_modules/@google/adk/node_modules/mime-types/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/mime-types/README.md
> **Analyzed At:** 2026-06-13T06:32:47.140Z

## mime-types
[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][ci-image]][ci-url]
[![Test Coverage][coveralls-image]][coveralls-url]
The ultimate javascript content-type utility.
Similar to [the `mime@1.x` module](https://www.npmjs.com/package/mime), except:
- __No fallbacks.__ Instead of naively returning the first available type,
`mime-types` simply returns `false`, so do
`var type = mime.lookup('unrecognized') || 'application/octet-stream'`.
- No `new Mime()` business, so you could do `var lookup = require('mime-types').lookup`.
- No `.define()` functionality
- Bug fixes for `.lookup(path)`
Otherwise, the API is compatible with `mime` 1.x.

## Install
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```sh
$ npm install mime-types
```

## Adding Types
All mime types are based on [mime-db](https://www.npmjs.com/package/mime-db),
so open a PR there if you'd like to add mime types.

## API
```js
var mime = require('mime-types')
```
All functions return `false` if input is invalid or not found.

## mime.lookup(path)
Lookup the content-type associated with a file.
```js
mime.lookup('json') // 'application/json'
mime.lookup('.md') // 'text/markdown'
mime.lookup('file.html') // 'text/html'
mime.lookup('folder/file.js') // 'application/javascript'
mime.lookup('folder/.htaccess') // false

mime.lookup('cats') // false
```

## mime.contentType(type)
Create a full content-type header given a content-type or extension.
When given an extension, `mime.lookup` is used to get the matching
content-type, otherwise the given content-type is used. Then if the
content-type does not already have a `charset` parameter, `mime.charset`
is used to get the default charset and add to the returned content-type.
```js
mime.contentType('markdown') // 'text/x-markdown; charset=utf-8'
mime.contentType('file.json') // 'application/json; charset=utf-8'
mime.contentType('text/html') // 'text/html; charset=utf-8'
mime.contentType('text/html; charset=iso-8859-1') // 'text/html; charset=iso-8859-1'

// from a full path
mime.contentType(path.extname('/path/to/file.json')) // 'application/json; charset=utf-8'
```

## mime.extension(type)
Get the default extension for a content-type.
```js
mime.extension('application/octet-stream') // 'bin'
```

## mime.charset(type)
Lookup the implied default charset of a content-type.
```js
mime.charset('text/markdown') // 'UTF-8'
```

## var type = mime.types[extension]
A map of content-types by extension.

## [extensions...] = mime.extensions[type]
A map of extensions by content-type.

## License
[MIT](LICENSE)
[ci-image]: https://badgen.net/github/checks/jshttp/mime-types/master?label=ci
[ci-url]: https://github.com/jshttp/mime-types/actions/workflows/ci.yml
[coveralls-image]: https://badgen.net/coveralls/c/github/jshttp/mime-types/master
[coveralls-url]: https://coveralls.io/r/jshttp/mime-types?branch=master
[node-version-image]: https://badgen.net/npm/node/mime-types
[node-version-url]: https://nodejs.org/en/download
[npm-downloads-image]: https://badgen.net/npm/dm/mime-types
[npm-url]: https://npmjs.org/package/mime-types
[npm-version-image]: https://badgen.net/npm/v/mime-types

---

# iCloud: web-app/node_modules/@google/adk/node_modules/mime-db/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/mime-db/README.md
> **Analyzed At:** 2026-06-13T06:32:47.152Z

## mime-db
[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-url]
[![Node.js Version][node-image]][node-url]
[![Build Status][ci-image]][ci-url]
[![Coverage Status][coveralls-image]][coveralls-url]
This is a large database of mime types and information about them.
It consists of a single, public JSON file and does not include any logic,
allowing it to remain as un-opinionated as possible with an API.
It aggregates data from the following sources:
- http://www.iana.org/assignments/media-types/media-types.xhtml
- http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types
- http://hg.nginx.org/nginx/raw-file/default/conf/mime.types

## Installation
```bash
npm install mime-db
```

## Database Download
If you're crazy enough to use this in the browser, you can just grab the
JSON file using [jsDelivr](https://www.jsdelivr.com/). It is recommended to
replace `master` with [a release tag](https://github.com/jshttp/mime-db/tags)
as the JSON format may change in the future.
```
https://cdn.jsdelivr.net/gh/jshttp/mime-db@master/db.json
```

## Usage
```js
var db = require('mime-db')

// grab data on .js files
var data = db['application/javascript']
```

## Data Structure
The JSON file is a map lookup for lowercased mime types.
Each mime type has the following properties:
- `.source` - where the mime type is defined.
If not set, it's probably a custom media type.
- `apache` - [Apache common media types](http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/conf/mime.types)
- `iana` - [IANA-defined media types](http://www.iana.org/assignments/media-types/media-types.xhtml)
- `nginx` - [nginx media types](http://hg.nginx.org/nginx/raw-file/default/conf/mime.types)
- `.extensions[]` - known extensions associated with this mime type.
- `.compressible` - whether a file of this type can be gzipped.
- `.charset` - the default charset associated with this type, if any.
If unknown, every property could be `undefined`.

## Contributing
To edit the database, only make PRs against `src/custom-types.json` or
`src/custom-suffix.json`.
The `src/custom-types.json` file is a JSON object with the MIME type as the
keys and the values being an object with the following keys:
- `compressible` - leave out if you don't know, otherwise `true`/`false` to
indicate whether the data represented by the type is typically compressible.
- `extensions` - include an array of file extensions that are associated with
the type.
- `notes` - human-readable notes about the type, typically what the type is.
- `sources` - include an array of URLs of where the MIME type and the associated
extensions are sourced from. This needs to be a [primary source](https://en.wikipedia.org/wiki/Primary_source);
links to type aggregating sites and Wikipedia are _not acceptable_.
To update the build, run `npm run build`.

## Adding Custom Media Types
The best way to get new media types included in this library is to register
them with the IANA. The community registration procedure is outlined in
[RFC 6838 section 5](http://tools.ietf.org/html/rfc6838#section-5). Types
registered with the IANA are automatically pulled into this library.
If that is not possible / feasible, they can be added directly here as a
"custom" type. To do this, it is required to have a primary source that
definitively lists the media type. If an extension is going to be listed as
associateed with this media type, the source must definitively link the
media type and extension as well.
[ci-image]: https://badgen.net/github/checks/jshttp/mime-db/master?label=ci
[ci-url]: https://github.com/jshttp/mime-db/actions?query=workflow%3Aci
[coveralls-image]: https://badgen.net/coveralls/c/github/jshttp/mime-db/master
[coveralls-url]: https://coveralls.io/r/jshttp/mime-db?branch=master
[node-image]: https://badgen.net/npm/node/mime-db
[node-url]: https://nodejs.org/en/download
[npm-downloads-image]: https://badgen.net/npm/dm/mime-db
[npm-url]: https://npmjs.org/package/mime-db
[npm-version-image]: https://badgen.net/npm/v/mime-db

---

# iCloud: web-app/node_modules/@google/adk/node_modules/merge-descriptors/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/merge-descriptors/README.md
> **Analyzed At:** 2026-06-13T06:32:47.165Z

## merge-descriptors
[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Build Status][travis-image]][travis-url]
[![Test Coverage][coveralls-image]][coveralls-url]
Merge objects using descriptors.
```js
var thing = {
  get name() {
    return 'jon'
  }
}

var animal = {

}

merge(animal, thing)

animal.name === 'jon'
```

## merge(destination, source)
Redefines `destination`'s descriptors with `source`'s. The return value is the
`destination` object.

## merge(destination, source, false)
Defines `source`'s descriptors on `destination` if `destination` does not have
a descriptor by the same name. The return value is the `destination` object.

## License
[MIT](LICENSE)
[npm-image]: https://img.shields.io/npm/v/merge-descriptors.svg
[npm-url]: https://npmjs.org/package/merge-descriptors
[travis-image]: https://img.shields.io/travis/component/merge-descriptors/master.svg
[travis-url]: https://travis-ci.org/component/merge-descriptors
[coveralls-image]: https://img.shields.io/coveralls/component/merge-descriptors/master.svg
[coveralls-url]: https://coveralls.io/r/component/merge-descriptors?branch=master
[downloads-image]: https://img.shields.io/npm/dm/merge-descriptors.svg
[downloads-url]: https://npmjs.org/package/merge-descriptors

---

# iCloud: web-app/node_modules/@google/adk/node_modules/media-typer/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/media-typer/README.md
> **Analyzed At:** 2026-06-13T06:32:47.175Z

## media-typer
[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][travis-image]][travis-url]
[![Test Coverage][coveralls-image]][coveralls-url]
Simple RFC 6838 media type parser

## Installation
```sh
$ npm install media-typer
```

## API
```js
var typer = require('media-typer')
```

## typer.parse(string)
```js
var obj = typer.parse('image/svg+xml; charset=utf-8')
```
Parse a media type string. This will return an object with the following
properties (examples are shown for the string `'image/svg+xml; charset=utf-8'`):
- `type`: The type of the media type (always lower case). Example: `'image'`
- `subtype`: The subtype of the media type (always lower case). Example: `'svg'`
- `suffix`: The suffix of the media type (always lower case). Example: `'xml'`

## typer.parse(req)
```js
var obj = typer.parse(req)
```
Parse the `content-type` header from the given `req`. Short-cut for
`typer.parse(req.headers['content-type'])`.

## typer.parse(res)
```js
var obj = typer.parse(res)
```
Parse the `content-type` header set on the given `res`. Short-cut for
`typer.parse(res.getHeader('content-type'))`.

## typer.format(obj)
```js
var obj = typer.format({type: 'image', subtype: 'svg', suffix: 'xml'})
```
Format an object into a media type string. This will return a string of the
mime type for the given object. For the properties of the object, see the
documentation for `typer.parse(string)`.

## License
[MIT](LICENSE)
[npm-image]: https://img.shields.io/npm/v/media-typer.svg?style=flat
[npm-url]: https://npmjs.org/package/media-typer
[node-version-image]: https://img.shields.io/badge/node.js-%3E%3D_0.6-brightgreen.svg?style=flat
[node-version-url]: http://nodejs.org/download/
[travis-image]: https://img.shields.io/travis/jshttp/media-typer.svg?style=flat
[travis-url]: https://travis-ci.org/jshttp/media-typer
[coveralls-image]: https://img.shields.io/coveralls/jshttp/media-typer.svg?style=flat
[coveralls-url]: https://coveralls.io/r/jshttp/media-typer
[downloads-image]: https://img.shields.io/npm/dm/media-typer.svg?style=flat
[downloads-url]: https://npmjs.org/package/media-typer

---

# iCloud: web-app/node_modules/@google/adk/node_modules/iconv-lite/Changelog.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/iconv-lite/Changelog.md
> **Analyzed At:** 2026-06-13T06:32:47.180Z

## 0.4.24 / 2018-08-22
* Added MIK encoding (#196, by @Ivan-Kalatchev)

## 0.4.23 / 2018-05-07
* Fix deprecation warning in Node v10 due to the last usage of `new Buffer` (#185, by @felixbuenemann)
* Switched from NodeBuffer to Buffer in typings (#155 by @felixfbecker, #186 by @larssn)

## 0.4.22 / 2018-05-05
* Use older semver style for dependencies to be compatible with Node version 0.10 (#182, by @dougwilson)
* Fix tests to accomodate fixes in Node v10 (#182, by @dougwilson)

## 0.4.21 / 2018-04-06
* Fix encoding canonicalization (#156)
* Fix the paths in the "browser" field in package.json (#174 by @LMLB)
* Removed "contributors" section in package.json - see Git history instead.

## 0.4.20 / 2018-04-06
* Updated `new Buffer()` usages with recommended replacements as it's being deprecated in Node v10 (#176, #178 by @ChALkeR)

## 0.4.19 / 2017-09-09
* Fixed iso8859-1 codec regression in handling untranslatable characters (#162, caused by #147)
* Re-generated windows1255 codec, because it was updated in iconv project
* Fixed grammar in error message when iconv-lite is loaded with encoding other than utf8

## 0.4.18 / 2017-06-13
* Fixed CESU-8 regression in Node v8.

## 0.4.17 / 2017-04-22
* Updated typescript definition file to support Angular 2 AoT mode (#153 by @larssn)

## 0.4.16 / 2017-04-22
* Added support for React Native (#150)
* Changed iso8859-1 encoding to usine internal 'binary' encoding, as it's the same thing (#147 by @mscdex)
* Fixed typo in Readme (#138 by @jiangzhuo)
* Fixed build for Node v6.10+ by making correct version comparison
* Added a warning if iconv-lite is loaded not as utf-8 (see #142)

## 0.4.15 / 2016-11-21
* Fixed typescript type definition (#137)

## 0.4.14 / 2016-11-20
* Preparation for v1.0
* Added Node v6 and latest Node versions to Travis CI test rig
* Deprecated Node v0.8 support
* Typescript typings (@larssn)
* Fix encoding of Euro character in GB 18030 (inspired by @lygstate)
* Add ms prefix to dbcs windows encodings (@rokoroku)

## 0.4.13 / 2015-10-01
* Fix silly mistake in deprecation notice.

## 0.4.12 / 2015-09-26
* Node v4 support:
* Added CESU-8 decoding (#106)
* Added deprecation notice for `extendNodeEncodings`
* Added Travis tests for Node v4 and io.js latest (#105 by @Mithgol)

## 0.4.11 / 2015-07-03
* Added CESU-8 encoding.

## 0.4.10 / 2015-05-26
* Changed UTF-16 endianness heuristic to take into account any ASCII chars, not
just spaces. This should minimize the importance of "default" endianness.

## 0.4.9 / 2015-05-24
* Streamlined BOM handling: strip BOM by default, add BOM when encoding if
addBOM: true. Added docs to Readme.
* UTF16 now uses UTF16-LE by default.
* Fixed minor issue with big5 encoding.
* Added io.js testing on Travis; updated node-iconv version to test against.
Now we just skip testing SBCS encodings that node-iconv doesn't support.
* (internal refactoring) Updated codec interface to use classes.
* Use strict mode in all files.

## 0.4.8 / 2015-04-14
* added alias UNICODE-1-1-UTF-7 for UTF-7 encoding (#94)

## 0.4.7 / 2015-02-05
* stop official support of Node.js v0.8. Should still work, but no guarantees.
reason: Packages needed for testing are hard to get on Travis CI.
* work in environment where Object.prototype is monkey patched with enumerable
props (#89).

## 0.4.6 / 2015-01-12
* fix rare aliases of single-byte encodings (thanks @mscdex)
* double the timeout for dbcs tests to make them less flaky on travis

## 0.4.5 / 2014-11-20
* fix windows-31j and x-sjis encoding support (@nleush)
* minor fix: undefined variable reference when internal error happens

## 0.4.4 / 2014-07-16
* added encodings UTF-7 (RFC2152) and UTF-7-IMAP (RFC3501 Section 5.1.3)
* fixed streaming base64 encoding

## 0.4.3 / 2014-06-14
* added encodings UTF-16BE and UTF-16 with BOM

## 0.4.2 / 2014-06-12
* don't throw exception if `extendNodeEncodings()` is called more than once

## 0.4.1 / 2014-06-11
* codepage 808 added

## 0.4.0 / 2014-06-10
* code is rewritten from scratch
* all widespread encodings are supported
* streaming interface added
* browserify compatibility added
* (optional) extend core primitive encodings to make usage even simpler
* moved from vows to mocha as the testing framework

---

# iCloud: web-app/node_modules/@google/adk/node_modules/iconv-lite/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/iconv-lite/README.md
> **Analyzed At:** 2026-06-13T06:32:47.186Z

## Pure JS character encoding conversion [![Build Status](https://travis-ci.org/ashtuchkin/iconv-lite.svg?branch=master)](https://travis-ci.org/ashtuchkin/iconv-lite)
* Doesn't need native code compilation. Works on Windows and in sandboxed environments like [Cloud9](http://c9.io).
* Used in popular projects like [Express.js (body_parser)](https://github.com/expressjs/body-parser),
[Grunt](http://gruntjs.com/), [Nodemailer](http://www.nodemailer.com/), [Yeoman](http://yeoman.io/) and others.
* Faster than [node-iconv](https://github.com/bnoordhuis/node-iconv) (see below for performance comparison).
* Intuitive encode/decode API
* Streaming support for Node v0.10+
* [Deprecated] Can extend Node.js primitives (buffers, streams) to support all iconv-lite encodings.
* In-browser usage via [Browserify](https://github.com/substack/node-browserify) (~180k gzip compressed with Buffer shim included).
* Typescript [type definition file](https://github.com/ashtuchkin/iconv-lite/blob/master/lib/index.d.ts) included.
* React Native is supported (need to explicitly `npm install` two more modules: `buffer` and `stream`).
* License: MIT.
[![NPM Stats](https://nodei.co/npm/iconv-lite.png?downloads=true&downloadRank=true)](https://npmjs.org/packages/iconv-lite/)

## Basic API
```javascript
var iconv = require('iconv-lite');

// Convert from an encoded buffer to js string.
str = iconv.decode(Buffer.from([0x68, 0x65, 0x6c, 0x6c, 0x6f]), 'win1251');

// Convert from js string to an encoded buffer.
buf = iconv.encode("Sample input string", 'win1251');

// Check if encoding is supported
iconv.encodingExists("us-ascii")
```

## Streaming API (Node v0.10+)
```javascript

// Decode stream (from binary stream to js strings)
http.createServer(function(req, res) {
    var converterStream = iconv.decodeStream('win1251');
    req.pipe(converterStream);

    converterStream.on('data', function(str) {
        console.log(str); // Do something with decoded strings, chunk-by-chunk.
    });
});

// Convert encoding streaming example
fs.createReadStream('file-in-win1251.txt')
    .pipe(iconv.decodeStream('win1251'))
    .pipe(iconv.encodeStream('ucs2'))
    .pipe(fs.createWriteStream('file-in-ucs2.txt'));

// Sugar: all encode/decode streams have .collect(cb) method to accumulate data.
http.createServer(function(req, res) {
    req.pipe(iconv.decodeStream('win1251')).collect(function(err, body) {
        assert(typeof body == 'string');
        console.log(body); // full request body string
    });
});
```

## [Deprecated] Extend Node.js own encodings
> NOTE: This doesn't work on latest Node versions. See [details](https://github.com/ashtuchkin/iconv-lite/wiki/Node-v4-compatibility).
```javascript
// After this call all Node basic primitives will understand iconv-lite encodings.
iconv.extendNodeEncodings();

// Examples:
buf = new Buffer(str, 'win1251');
buf.write(str, 'gbk');
str = buf.toString('latin1');
assert(Buffer.isEncoding('iso-8859-15'));
Buffer.byteLength(str, 'us-ascii');

http.createServer(function(req, res) {
    req.setEncoding('big5');
    req.collect(function(err, body) {
        console.log(body);
    });
});

fs.createReadStream("file.txt", "shift_jis");

// External modules are also supported (if they use Node primitives, which they probably do).
request = require('request');
request({
    url: "http://github.com/", 
    encoding: "cp932"
});

// To remove extensions
iconv.undoExtendNodeEncodings();
```

## Supported encodings
*  All node.js native encodings: utf8, ucs2 / utf16-le, ascii, binary, base64, hex.
*  Additional unicode encodings: utf16, utf16-be, utf-7, utf-7-imap.
*  All widespread singlebyte encodings: Windows 125x family, ISO-8859 family,
IBM/DOS codepages, Macintosh family, KOI8 family, all others supported by iconv library.
Aliases like 'latin1', 'us-ascii' also supported.
*  All widespread multibyte encodings: CP932, CP936, CP949, CP950, GB2312, GBK, GB18030, Big5, Shift_JIS, EUC-JP.
See [all supported encodings on wiki](https://github.com/ashtuchkin/iconv-lite/wiki/Supported-Encodings).
Most singlebyte encodings are generated automatically from [node-iconv](https://github.com/bnoordhuis/node-iconv). Thank you Ben Noordhuis and libiconv authors!
Multibyte encodings are generated from [Unicode.org mappings](http://www.unicode.org/Public/MAPPINGS/) and [WHATWG Encoding Standard mappings](http://encoding.spec.whatwg.org/). Thank you, respective authors!

## Encoding/decoding speed
Comparison with node-iconv module (1000x256kb, on MacBook Pro, Core i5/2.6 GHz, Node v0.12.0).
Note: your results may vary, so please always check on your hardware.
operation             iconv@2.1.4   iconv-lite@0.4.7
----------------------------------------------------------
encode('win1251')     ~96 Mb/s      ~320 Mb/s
decode('win1251')     ~95 Mb/s      ~246 Mb/s

## BOM handling
* Decoding: BOM is stripped by default, unless overridden by passing `stripBOM: false` in options
A callback might also be given as a `stripBOM` parameter - it'll be called if BOM character was actually found.
* If you want to detect UTF-8 BOM when decoding other encodings, use [node-autodetect-decoder-stream](https://github.com/danielgindi/node-autodetect-decoder-stream) module.
* Encoding: No BOM added, unless overridden by `addBOM: true` option.

## UTF-16 Encodings
This library supports UTF-16LE, UTF-16BE and UTF-16 encodings. First two are straightforward, but UTF-16 is trying to be
smart about endianness in the following ways:
* Decoding: uses BOM and 'spaces heuristic' to determine input endianness. Default is UTF-16LE, but can be
overridden with `defaultEncoding: 'utf-16be'` option. Strips BOM unless `stripBOM: false`.
* Encoding: uses UTF-16LE and writes BOM by default. Use `addBOM: false` to override.

## Other notes
When decoding, be sure to supply a Buffer to decode() method, otherwise [bad things usually happen](https://github.com/ashtuchkin/iconv-lite/wiki/Use-Buffers-when-decoding).
Untranslatable characters are set to � or ?. No transliteration is currently supported.
Node versions 0.10.31 and 0.11.13 are buggy, don't use them (see #65, #77).

## Testing
```bash
$ git clone git@github.com:ashtuchkin/iconv-lite.git
$ cd iconv-lite
$ npm install
$ npm test
    
$ # To view performance:
$ node test/performance.js

$ # To view test coverage:
$ npm run coverage
$ open coverage/lcov-report/index.html
```

---

# iCloud: web-app/node_modules/@google/adk/node_modules/fresh/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/fresh/README.md
> **Analyzed At:** 2026-06-13T06:32:47.200Z

## fresh
[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][travis-image]][travis-url]
[![Test Coverage][coveralls-image]][coveralls-url]
HTTP response freshness testing

## Installation
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```
$ npm install fresh
```

## API
```js
var fresh = require('fresh')
```

## fresh(reqHeaders, resHeaders)
Check freshness of the response using request and response headers.
When the response is still "fresh" in the client's cache `true` is
returned, otherwise `false` is returned to indicate that the client
cache is now stale and the full response should be sent.
When a client sends the `Cache-Control: no-cache` request header to
indicate an end-to-end reload request, this module will return `false`
to make handling these requests transparent.

## Known Issues
This module is designed to only follow the HTTP specifications, not
to work-around all kinda of client bugs (especially since this module
typically does not recieve enough information to understand what the
client actually is).
There is a known issue that in certain versions of Safari, Safari
will incorrectly make a request that allows this module to validate
freshness of the resource even when Safari does not have a
representation of the resource in the cache. The module
[jumanji](https://www.npmjs.com/package/jumanji) can be used in
an Express application to work-around this issue and also provides
links to further reading on this Safari bug.

## API usage
```js
var reqHeaders = { 'if-none-match': '"foo"' }
var resHeaders = { 'etag': '"bar"' }
fresh(reqHeaders, resHeaders)
// => false

var reqHeaders = { 'if-none-match': '"foo"' }
var resHeaders = { 'etag': '"foo"' }
fresh(reqHeaders, resHeaders)
// => true
```

## Using with Node.js http server
```js
var fresh = require('fresh')
var http = require('http')

var server = http.createServer(function (req, res) {
  // perform server logic
  // ... including adding ETag / Last-Modified response headers

  if (isFresh(req, res)) {
    // client has a fresh copy of resource
    res.statusCode = 304
    res.end()
    return
  }

  // send the resource
  res.statusCode = 200
  res.end('hello, world!')
})

function isFresh (req, res) {
  return fresh(req.headers, {
    'etag': res.getHeader('ETag'),
    'last-modified': res.getHeader('Last-Modified')
  })
}

server.listen(3000)
```

## License
[MIT](LICENSE)
[npm-image]: https://img.shields.io/npm/v/fresh.svg
[npm-url]: https://npmjs.org/package/fresh
[node-version-image]: https://img.shields.io/node/v/fresh.svg
[node-version-url]: https://nodejs.org/en/
[travis-image]: https://img.shields.io/travis/jshttp/fresh/master.svg
[travis-url]: https://travis-ci.org/jshttp/fresh
[coveralls-image]: https://img.shields.io/coveralls/jshttp/fresh/master.svg
[coveralls-url]: https://coveralls.io/r/jshttp/fresh?branch=master
[downloads-image]: https://img.shields.io/npm/dm/fresh.svg
[downloads-url]: https://npmjs.org/package/fresh

---

# iCloud: web-app/node_modules/@google/adk/node_modules/finalhandler/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/finalhandler/README.md
> **Analyzed At:** 2026-06-13T06:32:47.212Z

## finalhandler
[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Node.js Version][node-image]][node-url]
[![Build Status][github-actions-ci-image]][github-actions-ci-url]
[![Test Coverage][coveralls-image]][coveralls-url]
Node.js function to invoke as the final step to respond to HTTP request.

## Installation
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```sh
$ npm install finalhandler
```

## API
```js
var finalhandler = require('finalhandler')
```

## finalhandler(req, res, [options])
Returns function to be invoked as the final step for the given `req` and `res`.
This function is to be invoked as `fn(err)`. If `err` is falsy, the handler will
write out a 404 response to the `res`. If it is truthy, an error response will
be written out to the `res` or `res` will be terminated if a response has already
started.
When an error is written, the following information is added to the response:
* The `res.statusCode` is set from `err.status` (or `err.statusCode`). If
this value is outside the 4xx or 5xx range, it will be set to 500.
* The `res.statusMessage` is set according to the status code.
* The body will be the HTML of the status code message if `env` is
`'production'`, otherwise will be `err.stack`.
* Any headers specified in an `err.headers` object.
The final handler will also unpipe anything from `req` when it is invoked.

## options.env
By default, the environment is determined by `NODE_ENV` variable, but it can be
overridden by this option.

## options.onerror
Provide a function to be called with the `err` when it exists. Can be used for
writing errors to a central location without excessive function generation. Called
as `onerror(err, req, res)`.

## always 404
```js
var finalhandler = require('finalhandler')
var http = require('http')

var server = http.createServer(function (req, res) {
  var done = finalhandler(req, res)
  done()
})

server.listen(3000)
```

## perform simple action
```js
var finalhandler = require('finalhandler')
var fs = require('fs')
var http = require('http')

var server = http.createServer(function (req, res) {
  var done = finalhandler(req, res)

  fs.readFile('index.html', function (err, buf) {
    if (err) return done(err)
    res.setHeader('Content-Type', 'text/html')
    res.end(buf)
  })
})

server.listen(3000)
```

## use with middleware-style functions
```js
var finalhandler = require('finalhandler')
var http = require('http')
var serveStatic = require('serve-static')

var serve = serveStatic('public')

var server = http.createServer(function (req, res) {
  var done = finalhandler(req, res)
  serve(req, res, done)
})

server.listen(3000)
```

## keep log of all errors
```js
var finalhandler = require('finalhandler')
var fs = require('fs')
var http = require('http')

var server = http.createServer(function (req, res) {
  var done = finalhandler(req, res, { onerror: logerror })

  fs.readFile('index.html', function (err, buf) {
    if (err) return done(err)
    res.setHeader('Content-Type', 'text/html')
    res.end(buf)
  })
})

server.listen(3000)

function logerror (err) {
  console.error(err.stack || err.toString())
}
```

## License
[MIT](LICENSE)
[npm-image]: https://img.shields.io/npm/v/finalhandler.svg
[npm-url]: https://npmjs.org/package/finalhandler
[node-image]: https://img.shields.io/node/v/finalhandler.svg
[node-url]: https://nodejs.org/en/download
[coveralls-image]: https://img.shields.io/coveralls/pillarjs/finalhandler.svg
[coveralls-url]: https://coveralls.io/r/pillarjs/finalhandler?branch=master
[downloads-image]: https://img.shields.io/npm/dm/finalhandler.svg
[downloads-url]: https://npmjs.org/package/finalhandler
[github-actions-ci-image]: https://github.com/pillarjs/finalhandler/actions/workflows/ci.yml/badge.svg
[github-actions-ci-url]: https://github.com/pillarjs/finalhandler/actions/workflows/ci.yml

---

# iCloud: web-app/node_modules/@google/adk/node_modules/finalhandler/SECURITY.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/finalhandler/SECURITY.md
> **Analyzed At:** 2026-06-13T06:32:47.219Z

## Reporting a Bug
The `finalhandler` team and community take all security bugs seriously. Thank
you for improving the security of Express. We appreciate your efforts and
responsible disclosure and will make every effort to acknowledge your
contributions.
Report security bugs by emailing the current owner(s) of `finalhandler`. This
information can be found in the npm registry using the command
`npm owner ls finalhandler`.
If unsure or unable to get the information from the above, open an issue
in the [project issue tracker](https://github.com/pillarjs/finalhandler/issues)
asking for the current contact information.
To ensure the timely response to your report, please ensure that the entirety
of the report is contained within the email body and not solely behind a web
link or an attachment.
At least one owner will acknowledge your email within 48 hours, and will send a
more detailed response within 48 hours indicating the next steps in handling
your report. After the initial reply to your report, the owners will
endeavor to keep you informed of the progress towards a fix and full
announcement, and may ask for additional information or guidance.

---

# iCloud: web-app/node_modules/@google/adk/node_modules/express/Readme.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/express/Readme.md
> **Analyzed At:** 2026-06-13T06:32:47.224Z

## Table of contents
* [Installation](#Installation)
* [Features](#Features)
* [Docs & Community](#docs--community)
* [Quick Start](#Quick-Start)
* [Running Tests](#Running-Tests)
* [Philosophy](#Philosophy)
* [Examples](#Examples)
* [Contributing to Express](#Contributing)
* [TC (Technical Committee)](#tc-technical-committee)
* [Triagers](#triagers)
* [License](#license)
[![NPM Version][npm-version-image]][npm-url]
[![NPM Install Size][npm-install-size-image]][npm-install-size-url]
[![NPM Downloads][npm-downloads-image]][npm-downloads-url]
[![OpenSSF Scorecard Badge][ossf-scorecard-badge]][ossf-scorecard-visualizer]
```js
const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello World')
})

app.listen(3000)
```

## Installation
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/).
Before installing, [download and install Node.js](https://nodejs.org/en/download/).
Node.js 0.10 or higher is required.
If this is a brand new project, make sure to create a `package.json` first with
the [`npm init` command](https://docs.npmjs.com/creating-a-package-json-file).
Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```console
$ npm install express
```
Follow [our installing guide](http://expressjs.com/en/starter/installing.html)
for more information.

## Features
* Robust routing
* Focus on high performance
* Super-high test coverage
* HTTP helpers (redirection, caching, etc)
* View system supporting 14+ template engines
* Content negotiation
* Executable for generating applications quickly

## Docs & Community
* [Website and Documentation](http://expressjs.com/) - [[website repo](https://github.com/expressjs/expressjs.com)]
* [#express](https://web.libera.chat/#express) on [Libera Chat](https://libera.chat) IRC
* [GitHub Organization](https://github.com/expressjs) for Official Middleware & Modules
* Visit the [Wiki](https://github.com/expressjs/express/wiki)
* [Google Group](https://groups.google.com/group/express-js) for discussion
* [Gitter](https://gitter.im/expressjs/express) for support and discussion
**PROTIP** Be sure to read [Migrating from 3.x to 4.x](https://github.com/expressjs/express/wiki/Migrating-from-3.x-to-4.x) as well as [New features in 4.x](https://github.com/expressjs/express/wiki/New-features-in-4.x).

## Quick Start
The quickest way to get started with express is to utilize the executable [`express(1)`](https://github.com/expressjs/generator) to generate an application as shown below:
Install the executable. The executable's major version will match Express's:
```console
$ npm install -g express-generator@4
```
Create the app:
```console
$ express /tmp/foo && cd /tmp/foo
```
Install dependencies:
```console
$ npm install
```
Start the server:
```console
$ npm start
```
View the website at: http://localhost:3000

## Philosophy
The Express philosophy is to provide small, robust tooling for HTTP servers, making
it a great solution for single page applications, websites, hybrids, or public
HTTP APIs.
Express does not force you to use any specific ORM or template engine. With support for over
14 template engines via [Consolidate.js](https://github.com/tj/consolidate.js),
you can quickly craft your perfect framework.

## Examples
To view the examples, clone the Express repo and install the dependencies:
```console
$ git clone https://github.com/expressjs/express.git --depth 1
$ cd express
$ npm install
```
Then run whichever example you want:
```console
$ node examples/content-negotiation
```

## Contributing
[![Linux Build][github-actions-ci-image]][github-actions-ci-url]
[![Windows Build][appveyor-image]][appveyor-url]
[![Test Coverage][coveralls-image]][coveralls-url]
The Express.js project welcomes all constructive contributions. Contributions take many forms,
from code for bug fixes and enhancements, to additions and fixes to documentation, additional
tests, triaging incoming pull requests and issues, and more!
See the [Contributing Guide](Contributing.md) for more technical details on contributing.

## Security Issues
If you discover a security vulnerability in Express, please see [Security Policies and Procedures](Security.md).

## Running Tests
To run the test suite, first install the dependencies, then run `npm test`:
```console
$ npm install
$ npm test
```

## People
The original author of Express is [TJ Holowaychuk](https://github.com/tj)
[List of all contributors](https://github.com/expressjs/express/graphs/contributors)

## TC (Technical Committee)
* [UlisesGascon](https://github.com/UlisesGascon) - **Ulises Gascón** (he/him)
* [jonchurch](https://github.com/jonchurch) - **Jon Church**
* [wesleytodd](https://github.com/wesleytodd) - **Wes Todd**
* [LinusU](https://github.com/LinusU) - **Linus Unnebäck**
* [blakeembrey](https://github.com/blakeembrey) - **Blake Embrey**
* [sheplu](https://github.com/sheplu) - **Jean Burellier**
* [crandmck](https://github.com/crandmck) - **Rand McKinney**
* [ctcpip](https://github.com/ctcpip) - **Chris de Almeida**
TC emeriti members

## TC emeriti members
* [dougwilson](https://github.com/dougwilson) - **Douglas Wilson**
* [hacksparrow](https://github.com/hacksparrow) - **Hage Yaapa**
* [jonathanong](https://github.com/jonathanong) - **jongleberry**
* [niftylettuce](https://github.com/niftylettuce) - **niftylettuce**
* [troygoode](https://github.com/troygoode) - **Troy Goode**

## Triagers
* [aravindvnair99](https://github.com/aravindvnair99) - **Aravind Nair**
* [carpasse](https://github.com/carpasse) - **Carlos Serrano**
* [CBID2](https://github.com/CBID2) - **Christine Belzie**
* [enyoghasim](https://github.com/enyoghasim) - **David Enyoghasim**
* [UlisesGascon](https://github.com/UlisesGascon) - **Ulises Gascón** (he/him)
* [mertcanaltin](https://github.com/mertcanaltin) - **Mert Can Altin**
* [0ss](https://github.com/0ss) - **Salah**
* [import-brain](https://github.com/import-brain) - **Eric Cheng** (he/him)
* [3imed-jaberi](https://github.com/3imed-jaberi) - **Imed Jaberi**
* [dakshkhetan](https://github.com/dakshkhetan) - **Daksh Khetan** (he/him)
* [lucasraziel](https://github.com/lucasraziel) - **Lucas Soares Do Rego**
* [IamLizu](https://github.com/IamLizu) - **S M Mahmudul Hasan** (he/him)
* [Sushmeet](https://github.com/Sushmeet) - **Sushmeet Sunger**
Triagers emeriti members

## Emeritus Triagers
* [AuggieH](https://github.com/AuggieH) - **Auggie Hudak**
* [G-Rath](https://github.com/G-Rath) - **Gareth Jones**
* [MohammadXroid](https://github.com/MohammadXroid) - **Mohammad Ayashi**
* [NawafSwe](https://github.com/NawafSwe) - **Nawaf Alsharqi**
* [NotMoni](https://github.com/NotMoni) - **Moni**
* [VigneshMurugan](https://github.com/VigneshMurugan) - **Vignesh Murugan**
* [davidmashe](https://github.com/davidmashe) - **David Ashe**
* [digitaIfabric](https://github.com/digitaIfabric) - **David**
* [e-l-i-s-e](https://github.com/e-l-i-s-e) - **Elise Bonner**
* [fed135](https://github.com/fed135) - **Frederic Charette**
* [firmanJS](https://github.com/firmanJS) - **Firman Abdul Hakim**
* [getspooky](https://github.com/getspooky) - **Yasser Ameur**
* [ghinks](https://github.com/ghinks) - **Glenn**
* [ghousemohamed](https://github.com/ghousemohamed) - **Ghouse Mohamed**
* [gireeshpunathil](https://github.com/gireeshpunathil) - **Gireesh Punathil**
* [jake32321](https://github.com/jake32321) - **Jake Reed**
* [jonchurch](https://github.com/jonchurch) - **Jon Church**
* [lekanikotun](https://github.com/lekanikotun) - **Troy Goode**
* [marsonya](https://github.com/marsonya) - **Lekan Ikotun**
* [mastermatt](https://github.com/mastermatt) - **Matt R. Wilson**
* [maxakuru](https://github.com/maxakuru) - **Max Edell**
* [mlrawlings](https://github.com/mlrawlings) - **Michael Rawlings**
* [rodion-arr](https://github.com/rodion-arr) - **Rodion Abdurakhimov**
* [sheplu](https://github.com/sheplu) - **Jean Burellier**
* [tarunyadav1](https://github.com/tarunyadav1) - **Tarun yadav**
* [tunniclm](https://github.com/tunniclm) - **Mike Tunnicliffe**

## License
[MIT](LICENSE)
[appveyor-image]: https://badgen.net/appveyor/ci/dougwilson/express/master?label=windows
[appveyor-url]: https://ci.appveyor.com/project/dougwilson/express
[coveralls-image]: https://badgen.net/coveralls/c/github/expressjs/express/master
[coveralls-url]: https://coveralls.io/r/expressjs/express?branch=master
[github-actions-ci-image]: https://badgen.net/github/checks/expressjs/express/master?label=linux
[github-actions-ci-url]: https://github.com/expressjs/express/actions/workflows/ci.yml
[npm-downloads-image]: https://badgen.net/npm/dm/express
[npm-downloads-url]: https://npmcharts.com/compare/express?minimal=true
[npm-install-size-image]: https://badgen.net/packagephobia/install/express
[npm-install-size-url]: https://packagephobia.com/result?p=express
[npm-url]: https://npmjs.org/package/express
[npm-version-image]: https://badgen.net/npm/v/express
[ossf-scorecard-badge]: https://api.scorecard.dev/projects/github.com/expressjs/express/badge
[ossf-scorecard-visualizer]: https://ossf.github.io/scorecard-visualizer/#/projects/github.com/expressjs/express
[Code of Conduct]: https://github.com/expressjs/express/blob/master/Code-Of-Conduct.md

---

# iCloud: web-app/node_modules/@google/adk/node_modules/debug/node_modules/ms/readme.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/debug/node_modules/ms/readme.md
> **Analyzed At:** 2026-06-13T06:32:47.244Z

## ms
[![Build Status](https://travis-ci.org/zeit/ms.svg?branch=master)](https://travis-ci.org/zeit/ms)
[![Slack Channel](http://zeit-slackin.now.sh/badge.svg)](https://zeit.chat/)
Use this package to easily convert various time formats to milliseconds.

## Examples
```js
ms('2 days')  // 172800000
ms('1d')      // 86400000
ms('10h')     // 36000000
ms('2.5 hrs') // 9000000
ms('2h')      // 7200000
ms('1m')      // 60000
ms('5s')      // 5000
ms('1y')      // 31557600000
ms('100')     // 100
```

## Convert from milliseconds
```js
ms(60000)             // "1m"
ms(2 * 60000)         // "2m"
ms(ms('10 hours'))    // "10h"
```

## Time format written-out
```js
ms(60000, { long: true })             // "1 minute"
ms(2 * 60000, { long: true })         // "2 minutes"
ms(ms('10 hours'), { long: true })    // "10 hours"
```

## Features
- Works both in [node](https://nodejs.org) and in the browser.
- If a number is supplied to `ms`, a string with a unit is returned.
- If a string that contains the number is supplied, it returns it as a number (e.g.: it returns `100` for `'100'`).
- If you pass a string with a number and a valid unit, the number of equivalent ms is returned.

## Caught a bug?
1. [Fork](https://help.github.com/articles/fork-a-repo/) this repository to your own GitHub account and then [clone](https://help.github.com/articles/cloning-a-repository/) it to your local device
2. Link the package to the global module directory: `npm link`
3. Within the module you want to test your local development instance of ms, just link it to the dependencies: `npm link ms`. Instead of the default one from npm, node will now use your clone of ms!
As always, you can run the tests using: `npm test`

---

# iCloud: web-app/node_modules/@google/adk/node_modules/cookie-signature/Readme.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/cookie-signature/Readme.md
> **Analyzed At:** 2026-06-13T06:32:47.256Z

## cookie-signature
Sign and unsign cookies.

## Example
```js
var cookie = require('cookie-signature');

var val = cookie.sign('hello', 'tobiiscool');
val.should.equal('hello.DGDUkGlIkCzPz+C0B064FNgHdEjox7ch8tOBGslZ5QI');

var val = cookie.sign('hello', 'tobiiscool');
cookie.unsign(val, 'tobiiscool').should.equal('hello');
cookie.unsign(val, 'luna').should.be.false;
```

## License
(The MIT License)
Copyright (c) 2012 LearnBoost &lt;tj@learnboost.com&gt;
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

# iCloud: web-app/node_modules/@google/adk/node_modules/content-disposition/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/content-disposition/README.md
> **Analyzed At:** 2026-06-13T06:32:47.268Z

## content-disposition
[![NPM Version][npm-image]][npm-url]
[![NPM Downloads][downloads-image]][downloads-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][github-actions-ci-image]][github-actions-ci-url]
[![Test Coverage][coveralls-image]][coveralls-url]
Create and parse HTTP `Content-Disposition` header

## Installation
```sh
$ npm install content-disposition
```

## API
```js
var contentDisposition = require('content-disposition')
```

## contentDisposition(filename, options)
Create an attachment `Content-Disposition` header value using the given file name,
if supplied. The `filename` is optional and if no file name is desired, but you
want to specify `options`, set `filename` to `undefined`.
```js
res.setHeader('Content-Disposition', contentDisposition('∫ maths.pdf'))
```
**note** HTTP headers are of the ISO-8859-1 character set. If you are writing this
header through a means different from `setHeader` in Node.js, you'll want to specify
the `'binary'` encoding in Node.js.

## Options
`contentDisposition` accepts these properties in the options object.

## fallback
If the `filename` option is outside ISO-8859-1, then the file name is actually
stored in a supplemental field for clients that support Unicode file names and
a ISO-8859-1 version of the file name is automatically generated.
This specifies the ISO-8859-1 file name to override the automatic generation or
disables the generation all together, defaults to `true`.
- A string will specify the ISO-8859-1 file name to use in place of automatic
generation.
- `false` will disable including a ISO-8859-1 file name and only include the
Unicode version (unless the file name is already ISO-8859-1).
- `true` will enable automatic generation if the file name is outside ISO-8859-1.
If the `filename` option is ISO-8859-1 and this option is specified and has a
different value, then the `filename` option is encoded in the extended field
and this set as the fallback field, even though they are both ISO-8859-1.

## type
Specifies the disposition type, defaults to `"attachment"`. This can also be
`"inline"`, or any other value (all values except inline are treated like
`attachment`, but can convey additional information if both parties agree to
it). The type is normalized to lower-case.

## contentDisposition.parse(string)
```js
var disposition = contentDisposition.parse('attachment; filename="EURO rates.txt"; filename*=UTF-8\'\'%e2%82%ac%20rates.txt')
```
Parse a `Content-Disposition` header string. This automatically handles extended
("Unicode") parameters by decoding them and providing them under the standard
parameter name. This will return an object with the following properties (examples
are shown for the string `'attachment; filename="EURO rates.txt"; filename*=UTF-8\'\'%e2%82%ac%20rates.txt'`):
- `type`: The disposition type (always lower case). Example: `'attachment'`
- `parameters`: An object of the parameters in the disposition (name of parameter
always lower case and extended versions replace non-extended versions). Example:
`{filename: "€ rates.txt"}`

## Send a file for download
```js
var contentDisposition = require('content-disposition')
var destroy = require('destroy')
var fs = require('fs')
var http = require('http')
var onFinished = require('on-finished')

var filePath = '/path/to/public/plans.pdf'

http.createServer(function onRequest (req, res) {
  // set headers
  res.setHeader('Content-Type', 'application/pdf')
  res.setHeader('Content-Disposition', contentDisposition(filePath))

  // send file
  var stream = fs.createReadStream(filePath)
  stream.pipe(res)
  onFinished(res, function () {
    destroy(stream)
  })
})
```

## Testing
```sh
$ npm test
```

## References
- [RFC 2616: Hypertext Transfer Protocol -- HTTP/1.1][rfc-2616]
- [RFC 5987: Character Set and Language Encoding for Hypertext Transfer Protocol (HTTP) Header Field Parameters][rfc-5987]
- [RFC 6266: Use of the Content-Disposition Header Field in the Hypertext Transfer Protocol (HTTP)][rfc-6266]
- [Test Cases for HTTP Content-Disposition header field (RFC 6266) and the Encodings defined in RFCs 2047, 2231 and 5987][tc-2231]
[rfc-2616]: https://tools.ietf.org/html/rfc2616
[rfc-5987]: https://tools.ietf.org/html/rfc5987
[rfc-6266]: https://tools.ietf.org/html/rfc6266
[tc-2231]: http://greenbytes.de/tech/tc2231/

## License
[MIT](LICENSE)
[npm-image]: https://img.shields.io/npm/v/content-disposition.svg
[npm-url]: https://npmjs.org/package/content-disposition
[node-version-image]: https://img.shields.io/node/v/content-disposition.svg
[node-version-url]: https://nodejs.org/en/download
[coveralls-image]: https://img.shields.io/coveralls/jshttp/content-disposition.svg
[coveralls-url]: https://coveralls.io/r/jshttp/content-disposition?branch=master
[downloads-image]: https://img.shields.io/npm/dm/content-disposition.svg
[downloads-url]: https://npmjs.org/package/content-disposition
[github-actions-ci-image]: https://img.shields.io/github/workflow/status/jshttp/content-disposition/ci/master?label=ci
[github-actions-ci-url]: https://github.com/jshttp/content-disposition?query=workflow%3Aci

---

# iCloud: web-app/node_modules/@google/adk/node_modules/accepts/README.md

> **Source:** icloud://web-app/node_modules/@google/adk/node_modules/accepts/README.md
> **Analyzed At:** 2026-06-13T06:32:47.281Z

## accepts
[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-url]
[![Node.js Version][node-version-image]][node-version-url]
[![Build Status][github-actions-ci-image]][github-actions-ci-url]
[![Test Coverage][coveralls-image]][coveralls-url]
Higher level content negotiation based on [negotiator](https://www.npmjs.com/package/negotiator).
Extracted from [koa](https://www.npmjs.com/package/koa) for general use.
In addition to negotiator, it allows:
- Allows types as an array or arguments list, ie `(['text/html', 'application/json'])`
as well as `('text/html', 'application/json')`.
- Allows type shorthands such as `json`.
- Returns `false` when no types match
- Treats non-existent headers as `*`

## Installation
This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/). Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):
```sh
$ npm install accepts
```

## API
```js
var accepts = require('accepts')
```

## accepts(req)
Create a new `Accepts` object for the given `req`.

## .charset(charsets)
Return the first accepted charset. If nothing in `charsets` is accepted,
then `false` is returned.

## .charsets()
Return the charsets that the request accepts, in the order of the client's
preference (most preferred first).

## .encoding(encodings)
Return the first accepted encoding. If nothing in `encodings` is accepted,
then `false` is returned.

## .encodings()
Return the encodings that the request accepts, in the order of the client's
preference (most preferred first).

## .language(languages)
Return the first accepted language. If nothing in `languages` is accepted,
then `false` is returned.

## .languages()
Return the languages that the request accepts, in the order of the client's
preference (most preferred first).

## .type(types)
Return the first accepted type (and it is returned as the same text as what
appears in the `types` array). If nothing in `types` is accepted, then `false`
is returned.
The `types` array can contain full MIME types or file extensions. Any value
that is not a full MIME types is passed to `require('mime-types').lookup`.

## .types()
Return the types that the request accepts, in the order of the client's
preference (most preferred first).

## Simple type negotiation
This simple example shows how to use `accepts` to return a different typed
respond body based on what the client wants to accept. The server lists it's
preferences in order and will get back the best match between the client and
server.
```js
var accepts = require('accepts')
var http = require('http')

function app (req, res) {
  var accept = accepts(req)

  // the order of this list is significant; should be server preferred order
  switch (accept.type(['json', 'html'])) {
    case 'json':
      res.setHeader('Content-Type', 'application/json')
      res.write('{"hello":"world!"}')
      break
    case 'html':
      res.setHeader('Content-Type', 'text/html')
      res.write('<b>hello, world!</b>')
      break
    default:
      // the fallback is text/plain, so no need to specify it above
      res.setHeader('Content-Type', 'text/plain')
      res.write('hello, world!')
      break
  }

  res.end()
}

http.createServer(app).listen(3000)
```
You can test this out with the cURL program:
```sh
curl -I -H'Accept: text/html' http://localhost:3000/
```

## License
[MIT](LICENSE)
[coveralls-image]: https://badgen.net/coveralls/c/github/jshttp/accepts/master
[coveralls-url]: https://coveralls.io/r/jshttp/accepts?branch=master
[github-actions-ci-image]: https://badgen.net/github/checks/jshttp/accepts/master?label=ci
[github-actions-ci-url]: https://github.com/jshttp/accepts/actions/workflows/ci.yml
[node-version-image]: https://badgen.net/npm/node/accepts
[node-version-url]: https://nodejs.org/en/download
[npm-downloads-image]: https://badgen.net/npm/dm/accepts
[npm-url]: https://npmjs.org/package/accepts
[npm-version-image]: https://badgen.net/npm/v/accepts

---

# iCloud: web-app/node_modules/@eslint-community/regexpp/README.md

> **Source:** icloud://web-app/node_modules/@eslint-community/regexpp/README.md
> **Analyzed At:** 2026-06-13T06:32:47.316Z

## @eslint-community/regexpp
[![npm version](https://img.shields.io/npm/v/@eslint-community/regexpp.svg)](https://www.npmjs.com/package/@eslint-community/regexpp)
[![Downloads/month](https://img.shields.io/npm/dm/@eslint-community/regexpp.svg)](http://www.npmtrends.com/@eslint-community/regexpp)
[![Build Status](https://github.com/eslint-community/regexpp/workflows/CI/badge.svg)](https://github.com/eslint-community/regexpp/actions)
[![codecov](https://codecov.io/gh/eslint-community/regexpp/branch/main/graph/badge.svg)](https://codecov.io/gh/eslint-community/regexpp)
A regular expression parser for ECMAScript.

## 💿 Installation
```bash
$ npm install @eslint-community/regexpp
```
- require Node@^12.0.0 || ^14.0.0 || >=16.0.0.

## 📖 Usage
```ts
import {
    AST,
    RegExpParser,
    RegExpValidator,
    RegExpVisitor,
    parseRegExpLiteral,
    validateRegExpLiteral,
    visitRegExpAST
} from "@eslint-community/regexpp"
```

## parseRegExpLiteral(source, options?)
Parse a given regular expression literal then make AST object.
This is equivalent to `new RegExpParser(options).parseLiteral(source)`.
- **Parameters:**
- `source` (`string | RegExp`) The source code to parse.
- `options?` ([`RegExpParser.Options`]) The options to parse.
- **Return:**
- The AST of the regular expression.

## validateRegExpLiteral(source, options?)
Validate a given regular expression literal.
This is equivalent to `new RegExpValidator(options).validateLiteral(source)`.
- **Parameters:**
- `source` (`string`) The source code to validate.
- `options?` ([`RegExpValidator.Options`]) The options to validate.

## visitRegExpAST(ast, handlers)
Visit each node of a given AST.
This is equivalent to `new RegExpVisitor(handlers).visit(ast)`.
- **Parameters:**
- `ast` ([`AST.Node`]) The AST to visit.
- `handlers` ([`RegExpVisitor.Handlers`]) The callbacks.

## new RegExpParser(options?)
- **Parameters:**
- `options?` ([`RegExpParser.Options`]) The options to parse.

## parser.parseLiteral(source, start?, end?)
Parse a regular expression literal.
- **Parameters:**
- `source` (`string`) The source code to parse. E.g. `"/abc/g"`.
- `start?` (`number`) The start index in the source code. Default is `0`.
- `end?` (`number`) The end index in the source code. Default is `source.length`.
- **Return:**
- The AST of the regular expression.

## parser.parsePattern(source, start?, end?, flags?)
Parse a regular expression pattern.
- **Parameters:**
- `source` (`string`) The source code to parse. E.g. `"abc"`.
- `start?` (`number`) The start index in the source code. Default is `0`.
- `end?` (`number`) The end index in the source code. Default is `source.length`.
- **Return:**
- The AST of the regular expression pattern.

## parser.parseFlags(source, start?, end?)
Parse a regular expression flags.
- **Parameters:**
- `source` (`string`) The source code to parse. E.g. `"gim"`.
- `start?` (`number`) The start index in the source code. Default is `0`.
- `end?` (`number`) The end index in the source code. Default is `source.length`.
- **Return:**
- The AST of the regular expression flags.

## new RegExpValidator(options)
- **Parameters:**
- `options` ([`RegExpValidator.Options`]) The options to validate.

## validator.validateLiteral(source, start, end)
Validate a regular expression literal.
- **Parameters:**
- `source` (`string`) The source code to validate.
- `start?` (`number`) The start index in the source code. Default is `0`.
- `end?` (`number`) The end index in the source code. Default is `source.length`.

## validator.validatePattern(source, start, end, flags)
Validate a regular expression pattern.
- **Parameters:**
- `source` (`string`) The source code to validate.
- `start?` (`number`) The start index in the source code. Default is `0`.
- `end?` (`number`) The end index in the source code. Default is `source.length`.

## validator.validateFlags(source, start, end)
Validate a regular expression flags.
- **Parameters:**
- `source` (`string`) The source code to validate.
- `start?` (`number`) The start index in the source code. Default is `0`.
- `end?` (`number`) The end index in the source code. Default is `source.length`.

## new RegExpVisitor(handlers)
- **Parameters:**
- `handlers` ([`RegExpVisitor.Handlers`]) The callbacks.

## visitor.visit(ast)
Validate a regular expression literal.
- **Parameters:**
- `ast` ([`AST.Node`]) The AST to visit.

## 📰 Changelog
- [GitHub Releases](https://github.com/eslint-community/regexpp/releases)

## 🍻 Contributing
Welcome contributing!
Please use GitHub's Issues/PRs.

## Development Tools
- `npm test` runs tests and measures coverage.
- `npm run build` compiles TypeScript source code to `index.js`, `index.js.map`, and `index.d.ts`.
- `npm run clean` removes the temporary files which are created by `npm test` and `npm run build`.
- `npm run lint` runs ESLint.
- `npm run update:test` updates test fixtures.
- `npm run update:ids` updates `src/unicode/ids.ts`.
- `npm run watch` runs tests with `--watch` option.
[`AST.Node`]: src/ast.ts#L4
[`RegExpParser.Options`]: src/parser.ts#L743
[`RegExpValidator.Options`]: src/validator.ts#L220
[`RegExpVisitor.Handlers`]: src/visitor.ts#L291

---

# iCloud: web-app/node_modules/@eslint-community/eslint-utils/README.md

> **Source:** icloud://web-app/node_modules/@eslint-community/eslint-utils/README.md
> **Analyzed At:** 2026-06-13T06:32:47.323Z

## @eslint-community/eslint-utils
[![npm version](https://img.shields.io/npm/v/@eslint-community/eslint-utils.svg)](https://www.npmjs.com/package/@eslint-community/eslint-utils)
[![Downloads/month](https://img.shields.io/npm/dm/@eslint-community/eslint-utils.svg)](http://www.npmtrends.com/@eslint-community/eslint-utils)
[![Build Status](https://github.com/eslint-community/eslint-utils/workflows/CI/badge.svg)](https://github.com/eslint-community/eslint-utils/actions)
[![Coverage Status](https://codecov.io/gh/eslint-community/eslint-utils/branch/main/graph/badge.svg)](https://codecov.io/gh/eslint-community/eslint-utils)

## 🏁 Goal
This package provides utility functions and classes for make ESLint custom rules.
For examples:
-   [`getStaticValue`](https://eslint-community.github.io/eslint-utils/api/ast-utils.html#getstaticvalue) evaluates static value on AST.
-   [`ReferenceTracker`](https://eslint-community.github.io/eslint-utils/api/scope-utils.html#referencetracker-class) checks the members of modules/globals as handling assignments and destructuring.

## 📖 Usage
See [documentation](https://eslint-community.github.io/eslint-utils).

## 📰 Changelog
See [releases](https://github.com/eslint-community/eslint-utils/releases).

## ❤️ Contributing
Welcome contributing!
Please use GitHub's Issues/PRs.

## Development Tools
-   `npm run test-coverage` runs tests and measures coverage.
-   `npm run clean` removes the coverage result of `npm run test-coverage` command.
-   `npm run coverage` shows the coverage result of the last `npm run test-coverage` command.
-   `npm run lint` runs ESLint.
-   `npm run watch` runs tests on each file change.

---

# iCloud: web-app/node_modules/@eslint-community/eslint-utils/node_modules/eslint-visitor-keys/README.md

> **Source:** icloud://web-app/node_modules/@eslint-community/eslint-utils/node_modules/eslint-visitor-keys/README.md
> **Analyzed At:** 2026-06-13T06:32:47.329Z

## eslint-visitor-keys
[![npm version](https://img.shields.io/npm/v/eslint-visitor-keys.svg)](https://www.npmjs.com/package/eslint-visitor-keys)
[![Downloads/month](https://img.shields.io/npm/dm/eslint-visitor-keys.svg)](http://www.npmtrends.com/eslint-visitor-keys)
[![Build Status](https://github.com/eslint/eslint-visitor-keys/workflows/CI/badge.svg)](https://github.com/eslint/eslint-visitor-keys/actions)
Constants and utilities about visitor keys to traverse AST.

## 💿 Installation
Use [npm] to install.
```bash
$ npm install eslint-visitor-keys
```

## Requirements
- [Node.js] `^12.22.0`, `^14.17.0`, or `>=16.0.0`

## 📖 Usage
To use in an ESM file:
```js
import * as evk from "eslint-visitor-keys"
```
To use in a CommonJS file:
```js
const evk = require("eslint-visitor-keys")
```

## evk.KEYS
> type: `{ [type: string]: string[] | undefined }`
Visitor keys. This keys are frozen.
This is an object. Keys are the type of [ESTree] nodes. Their values are an array of property names which have child nodes.
For example:
```
console.log(evk.KEYS.AssignmentExpression) // → ["left", "right"]
```

## evk.getKeys(node)
> type: `(node: object) => string[]`
Get the visitor keys of a given AST node.
This is similar to `Object.keys(node)` of ES Standard, but some keys are excluded: `parent`, `leadingComments`, `trailingComments`, and names which start with `_`.
This will be used to traverse unknown nodes.
For example:
```js
const node = {
    type: "AssignmentExpression",
    left: { type: "Identifier", name: "foo" },
    right: { type: "Literal", value: 0 }
}
console.log(evk.getKeys(node)) // → ["type", "left", "right"]
```

## evk.unionWith(additionalKeys)
Make the union set with `evk.KEYS` and the given keys.
- The order of keys is, `additionalKeys` is at first, then `evk.KEYS` is concatenated after that.
- It removes duplicated keys as keeping the first one.
For example:
```js
console.log(evk.unionWith({
    MethodDefinition: ["decorators"]
})) // → { ..., MethodDefinition: ["decorators", "key", "value"], ... }
```

## 📰 Change log
See [GitHub releases](https://github.com/eslint/eslint-visitor-keys/releases).

## 🍻 Contributing
Welcome. See [ESLint contribution guidelines](https://eslint.org/docs/developer-guide/contributing/).

## Development commands
- `npm test` runs tests and measures code coverage.
- `npm run lint` checks source codes with ESLint.
- `npm run test:open-coverage` opens the code coverage report of the previous test with your default browser.
[npm]: https://www.npmjs.com/
[Node.js]: https://nodejs.org/
[ESTree]: https://github.com/estree/estree

---

# iCloud: web-app/node_modules/@eslint/plugin-kit/README.md

> **Source:** icloud://web-app/node_modules/@eslint/plugin-kit/README.md
> **Analyzed At:** 2026-06-13T06:32:47.336Z

## Description
A collection of utilities to help build ESLint plugins.

## Installation
For Node.js and compatible runtimes:
```shell
npm install @eslint/plugin-kit
# or
yarn add @eslint/plugin-kit
# or
pnpm install @eslint/plugin-kit
# or
bun add @eslint/plugin-kit
```
For Deno:
```shell
deno add @eslint/plugin-kit
```

## Usage
This package exports the following utilities:
- [`ConfigCommentParser`](#configcommentparser) - used to parse ESLint configuration comments (i.e., `/* eslint-disable rule */`)
- [`VisitNodeStep` and `CallMethodStep`](#visitnodestep-and-callmethodstep) - used to help implement `SourceCode#traverse()`
- [`Directive`](#directive) - used to help implement `SourceCode#getDisableDirectives()`
- [`TextSourceCodeBase`](#textsourcecodebase) - base class to help implement the `SourceCode` interface

## `ConfigCommentParser`
To use the `ConfigCommentParser` class, import it from the package and create a new instance, such as:
```js
import { ConfigCommentParser } from "@eslint/plugin-kit";

// create a new instance
const commentParser = new ConfigCommentParser();

// pass in a comment string without the comment delimiters
const directive = commentParser.parseDirective(
	"eslint-disable prefer-const, semi -- I don't want to use these.",
);

// will be undefined when a directive can't be parsed
if (directive) {
	console.log(directive.label); // "eslint-disable"
	console.log(directive.value); // "prefer-const, semi"
	console.log(directive.justification); // "I don't want to use these."
}
```
There are different styles of directive values that you'll need to parse separately to get the correct format:
```js
import { ConfigCommentParser } from "@eslint/plugin-kit";

// create a new instance
const commentParser = new ConfigCommentParser();

// list format
const list = commentParser.parseListConfig("prefer-const, semi");
console.log(Object.entries(list)); // [["prefer-const", true], ["semi", true]]

// string format
const strings = commentParser.parseStringConfig("foo:off, bar");
console.log(Object.entries(strings)); // [["foo", "off"], ["bar", null]]

// JSON-like config format
const jsonLike = commentParser.parseJSONLikeConfig(
	"semi:[error, never], prefer-const: warn",
);
console.log(Object.entries(jsonLike.config)); // [["semi", ["error", "never"]], ["prefer-const", "warn"]]
```

## `VisitNodeStep` and `CallMethodStep`
The `VisitNodeStep` and `CallMethodStep` classes represent steps in the traversal of source code. They implement the correct interfaces to return from the `SourceCode#traverse()` method.
The `VisitNodeStep` class is the more common of the two, where you are describing a visit to a particular node during the traversal. The constructor accepts three arguments:
- `target` - the node being visited. This is used to determine the method to call inside of a rule. For instance, if the node's type is `Literal` then ESLint will call a method named `Literal()` on the rule (if present).
- `phase` - either 1 for enter or 2 for exit.
- `args` - an array of arguments to pass into the visitor method of a rule.
For example:
```js
import { VisitNodeStep } from "@eslint/plugin-kit";

class MySourceCode {
	traverse() {
		const steps = [];

		for (const { node, parent, phase } of iterator(this.ast)) {
			steps.push(
				new VisitNodeStep({
					target: node,
					phase: phase === "enter" ? 1 : 2,
					args: [node, parent],
				}),
			);
		}

		return steps;
	}
}
```
The `CallMethodStep` class is less common and is used to tell ESLint to call a specific method on the rule. The constructor accepts two arguments:
- `target` - the name of the method to call, frequently beginning with `"on"` such as `"onCodePathStart"`.
- `args` - an array of arguments to pass to the method.
For example:
```js
import { VisitNodeStep, CallMethodStep } from "@eslint/plugin-kit";

class MySourceCode {
    traverse() {
        const steps = [];

        for (const { node, parent, phase } of iterator(this.ast)) {
            steps.push(
                new VisitNodeStep({
                    target: node,
                    phase: phase === "enter" ? 1 : 2,
                    args: [node, parent],
                }),
            );

            // call a method indicating how many times we've been through the loop
            steps.push(
                new CallMethodStep({
                    target: "onIteration",
                    args: [steps.length]
                });
            )
        }

        return steps;
    }
}
```

## `Directive`
The `Directive` class represents a disable directive in the source code and implements the `Directive` interface from `@eslint/core`. You can tell ESLint about disable directives using the `SourceCode#getDisableDirectives()` method, where part of the return value is an array of `Directive` objects. Here's an example:
```js
import { Directive, ConfigCommentParser } from "@eslint/plugin-kit";

class MySourceCode {
	getDisableDirectives() {
		const directives = [];
		const problems = [];
		const commentParser = new ConfigCommentParser();

		// read in the inline config nodes to check each one
		this.getInlineConfigNodes().forEach(comment => {
			// Step 1: Parse the directive
			const { label, value, justification } =
				commentParser.parseDirective(comment.value);

			// Step 2: Extract the directive value and create the `Directive` object
			switch (label) {
				case "eslint-disable":
				case "eslint-enable":
				case "eslint-disable-next-line":
				case "eslint-disable-line": {
					const directiveType = label.slice("eslint-".length);

					directives.push(
						new Directive({
							type: directiveType,
							node: comment,
							value,
							justification,
						}),
					);
				}

				// ignore any comments that don't begin with known labels
			}
		});

		return {
			directives,
			problems,
		};
	}
}
```

## `TextSourceCodeBase`
The `TextSourceCodeBase` class is intended to be a base class that has several of the common members found in `SourceCode` objects already implemented. Those members are:
- `lines` - an array of text lines that is created automatically when the constructor is called.
- `getLoc(nodeOrToken)` - gets the location of a node or token. Works for nodes that have the ESLint-style `loc` property and nodes that have the Unist-style [`position` property](https://github.com/syntax-tree/unist?tab=readme-ov-file#position). If you're using an AST with a different location format, you'll still need to implement this method yourself.
- `getRange(nodeOrToken)` - gets the range of a node or token within the source text. Works for nodes that have the ESLint-style `range` property and nodes that have the Unist-style [`position` property](https://github.com/syntax-tree/unist?tab=readme-ov-file#position). If you're using an AST with a different range format, you'll still need to implement this method yourself.
- `getText(node, beforeCount, afterCount)` - gets the source text for the given node that has range information attached. Optionally, can return additional characters before and after the given node. As long as `getRange()` is properly implemented, this method will just work.
- `getAncestors(node)` - returns the ancestry of the node. In order for this to work, you must implement the `getParent()` method yourself.
Here's an example:
```js
import { TextSourceCodeBase } from "@eslint/plugin-kit";

export class MySourceCode extends TextSourceCodeBase {
	#parents = new Map();

	constructor({ ast, text }) {
		super({ ast, text });
	}

	getParent(node) {
		return this.#parents.get(node);
	}

	traverse() {
		const steps = [];

		for (const { node, parent, phase } of iterator(this.ast)) {
			//save the parent information
			this.#parent.set(node, parent);

			steps.push(
				new VisitNodeStep({
					target: node,
					phase: phase === "enter" ? 1 : 2,
					args: [node, parent],
				}),
			);
		}

		return steps;
	}
}
```
In general, it's safe to collect the parent information during the `traverse()` method as `getParent()` and `getAncestor()` will only be called from rules once the AST has been traversed at least once.

## License
Apache 2.0

## Sponsors
The following companies, organizations, and individuals support ESLint's ongoing maintenance and development. [Become a Sponsor](https://eslint.org/donate)
to get your logo on our READMEs and [website](https://eslint.org/sponsors).
Platinum Sponsors
 Gold Sponsors
  Silver Sponsors
   Bronze Sponsors
         
Technology Sponsors
Technology sponsors allow us to use their products and services for free as part of a contribution to the open source ecosystem and our work.

---

# iCloud: web-app/node_modules/@eslint/object-schema/README.md

> **Source:** icloud://web-app/node_modules/@eslint/object-schema/README.md
> **Analyzed At:** 2026-06-13T06:32:47.344Z

## Overview
A JavaScript object merge/validation utility where you can define a different merge and validation strategy for each key. This is helpful when you need to validate complex data structures and then merge them in a way that is more complex than `Object.assign()`. This is used in the [`@eslint/config-array`](https://npmjs.com/package/@eslint/config-array) package but can also be used on its own.

## Installation
For Node.js and compatible runtimes:
```shell
npm install @eslint/object-schema
# or
yarn add @eslint/object-schema
# or
pnpm install @eslint/object-schema
# or
bun add @eslint/object-schema
```
For Deno:
```shell
deno add @eslint/object-schema
```

## Usage
Import the `ObjectSchema` constructor:
```js
// using ESM
import { ObjectSchema } from "@eslint/object-schema";

// using CommonJS
const { ObjectSchema } = require("@eslint/object-schema");

const schema = new ObjectSchema({
	// define a definition for the "downloads" key
	downloads: {
		required: true,
		merge(value1, value2) {
			return value1 + value2;
		},
		validate(value) {
			if (typeof value !== "number") {
				throw new Error("Expected downloads to be a number.");
			}
		},
	},

	// define a strategy for the "versions" key
	version: {
		required: true,
		merge(value1, value2) {
			return value1.concat(value2);
		},
		validate(value) {
			if (!Array.isArray(value)) {
				throw new Error("Expected versions to be an array.");
			}
		},
	},
});

const record1 = {
	downloads: 25,
	versions: ["v1.0.0", "v1.1.0", "v1.2.0"],
};

const record2 = {
	downloads: 125,
	versions: ["v2.0.0", "v2.1.0", "v3.0.0"],
};

// make sure the records are valid
schema.validate(record1);
schema.validate(record2);

// merge together (schema.merge() accepts any number of objects)
const result = schema.merge(record1, record2);

// result looks like this:

const result = {
	downloads: 75,
	versions: ["v1.0.0", "v1.1.0", "v1.2.0", "v2.0.0", "v2.1.0", "v3.0.0"],
};
```

## Named merge strategies
Instead of specifying a `merge()` method, you can specify one of the following strings to use a default merge strategy:
- `"assign"` - use `Object.assign()` to merge the two values into one object.
- `"overwrite"` - the second value always replaces the first.
- `"replace"` - the second value replaces the first if the second is not `undefined`.
For example:
```js
const schema = new ObjectSchema({
	name: {
		merge: "replace",
		validate() {},
	},
});
```

## Named validation strategies
Instead of specifying a `validate()` method, you can specify one of the following strings to use a default validation strategy:
- `"array"` - value must be an array.
- `"boolean"` - value must be a boolean.
- `"number"` - value must be a number.
- `"object"` - value must be an object.
- `"object?"` - value must be an object or null.
- `"string"` - value must be a string.
- `"string!"` - value must be a non-empty string.
For example:
```js
const schema = new ObjectSchema({
	name: {
		merge: "replace",
		validate: "string",
	},
});
```

## Subschemas
If you are defining a key that is, itself, an object, you can simplify the process by using a subschema. Instead of defining `merge()` and `validate()`, assign a `schema` key that contains a schema definition, like this:
```js
const schema = new ObjectSchema({
	name: {
		schema: {
			first: {
				merge: "replace",
				validate: "string",
			},
			last: {
				merge: "replace",
				validate: "string",
			},
		},
	},
});

schema.validate({
	name: {
		first: "n",
		last: "z",
	},
});
```

## Remove Keys During Merge
If the merge strategy for a key returns `undefined`, then the key will not appear in the final object. For example:
```js
const schema = new ObjectSchema({
	date: {
		merge() {
			return undefined;
		},
		validate(value) {
			Date.parse(value); // throws an error when invalid
		},
	},
});

const object1 = { date: "5/5/2005" };
const object2 = { date: "6/6/2006" };

const result = schema.merge(object1, object2);

console.log("date" in result); // false
```

## Requiring Another Key Be Present
If you'd like the presence of one key to require the presence of another key, you can use the `requires` property to specify an array of other properties that any key requires. For example:
```js
const schema = new ObjectSchema();

const schema = new ObjectSchema({
	date: {
		merge() {
			return undefined;
		},
		validate(value) {
			Date.parse(value); // throws an error when invalid
		},
	},
	time: {
		requires: ["date"],
		merge(first, second) {
			return second;
		},
		validate(value) {
			// ...
		},
	},
});

// throws error: Key "time" requires keys "date"
schema.validate({
	time: "13:45",
});
```
In this example, even though `date` is an optional key, it is required to be present whenever `time` is present.

## License
Apache 2.0

## Sponsors
The following companies, organizations, and individuals support ESLint's ongoing maintenance and development. [Become a Sponsor](https://eslint.org/donate)
to get your logo on our READMEs and [website](https://eslint.org/sponsors).
Platinum Sponsors
 Gold Sponsors
  Silver Sponsors
   Bronze Sponsors
        
Technology Sponsors
Technology sponsors allow us to use their products and services for free as part of a contribution to the open source ecosystem and our work.

---

# iCloud: web-app/node_modules/@eslint/js/README.md

> **Source:** icloud://web-app/node_modules/@eslint/js/README.md
> **Analyzed At:** 2026-06-13T06:32:47.353Z

## ESLint JavaScript Plugin
[Website](https://eslint.org) |
[Configure ESLint](https://eslint.org/docs/latest/use/configure) |
[Rules](https://eslint.org/docs/rules/) |
[Contribute to ESLint](https://eslint.org/docs/latest/contribute) |
[Report Bugs](https://eslint.org/docs/latest/contribute/report-bugs) |
[Code of Conduct](https://eslint.org/conduct) |
[X](https://x.com/geteslint) |
[Discord](https://eslint.org/chat) |
[Mastodon](https://fosstodon.org/@eslint) |
[Bluesky](https://bsky.app/profile/eslint.org)
The beginnings of separating out JavaScript-specific functionality from ESLint.
Right now, this plugin contains two configurations:
- `recommended` - enables the rules recommended by the ESLint team (the replacement for `"eslint:recommended"`)
- `all` - enables all ESLint rules (the replacement for `"eslint:all"`)

## Installation
You can install ESLint using npm or other package managers:
```shell
npm install eslint -D
# or
yarn add eslint -D
# or
pnpm install eslint -D
# or
bun add eslint -D
```
Then install this plugin:
```shell
npm install @eslint/js -D
# or
yarn add @eslint/js -D
# or
pnpm install @eslint/js -D
# or
bun add @eslint/js -D
```

## Usage
Use in your `eslint.config.js` file anytime you want to extend one of the configs:
```js
import { defineConfig } from "eslint/config";
import js from "@eslint/js";

export default defineConfig([
	// apply recommended rules to JS files
	{
		name: "your-project/recommended-rules",
		files: ["**/*.js"],
		plugins: {
			js,
		},
		extends: ["js/recommended"],
	},

	// apply recommended rules to JS files with an override
	{
		name: "your-project/recommended-rules-with-override",
		files: ["**/*.js"],
		plugins: {
			js,
		},
		extends: ["js/recommended"],
		rules: {
			"no-unused-vars": "warn",
		},
	},

	// apply all rules to JS files
	{
		name: "your-project/all-rules",
		files: ["**/*.js"],
		plugins: {
			js,
		},
		extends: ["js/all"],
		rules: {
			"no-unused-vars": "warn",
		},
	},
]);
```

---

# iCloud: web-app/node_modules/@eslint/eslintrc/README.md

> **Source:** icloud://web-app/node_modules/@eslint/eslintrc/README.md
> **Analyzed At:** 2026-06-13T06:32:47.360Z

## ESLintRC Library
This repository contains the legacy ESLintRC configuration file format for ESLint. This package is not intended for use outside of the ESLint ecosystem. It is ESLint-specific and not intended for use in other programs.
**Note:** This package is frozen except for critical bug fixes as ESLint moves to a new config system.

## Installation
You can install the package as follows:
```shell
npm install @eslint/eslintrc -D
# or
yarn add @eslint/eslintrc -D
# or
pnpm install @eslint/eslintrc -D
# or
bun install @eslint/eslintrc -D
```

## Usage (ESM)
The primary class in this package is `FlatCompat`, which is a utility to translate ESLintRC-style configs into flat configs. Here's how you use it inside of your `eslint.config.js` file:
```js
import { FlatCompat } from "@eslint/eslintrc";
import js from "@eslint/js";
import path from "path";
import { fileURLToPath } from "url";

// mimic CommonJS variables -- not needed if using CommonJS
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const compat = new FlatCompat({
    baseDirectory: __dirname,                  // optional; default: process.cwd()
    resolvePluginsRelativeTo: __dirname,       // optional
    recommendedConfig: js.configs.recommended, // optional unless you're using "eslint:recommended"
    allConfig: js.configs.all,                 // optional unless you're using "eslint:all"
});

export default [

    // mimic ESLintRC-style extends
    ...compat.extends("standard", "example", "plugin:react/recommended"),

    // mimic environments
    ...compat.env({
        es2020: true,
        node: true
    }),

    // mimic plugins
    ...compat.plugins("jsx-a11y", "react"),

    // translate an entire config
    ...compat.config({
        plugins: ["jsx-a11y", "react"],
        extends: "standard",
        env: {
            es2020: true,
            node: true
        },
        rules: {
            semi: "error"
        }
    })
];
```

## Usage (CommonJS)
Using `FlatCompat` in CommonJS files is similar to ESM, but you'll use `require()` and `module.exports` instead of `import` and `export`. Here's how you use it inside of your `eslint.config.js` CommonJS file:
```js
const { FlatCompat } = require("@eslint/eslintrc");
const js = require("@eslint/js");

const compat = new FlatCompat({
    baseDirectory: __dirname,                  // optional; default: process.cwd()
    resolvePluginsRelativeTo: __dirname,       // optional
    recommendedConfig: js.configs.recommended, // optional unless using "eslint:recommended"
    allConfig: js.configs.all,                 // optional unless using "eslint:all"
});

module.exports = [

    // mimic ESLintRC-style extends
    ...compat.extends("standard", "example", "plugin:react/recommended"),

    // mimic environments
    ...compat.env({
        es2020: true,
        node: true
    }),

    // mimic plugins
    ...compat.plugins("jsx-a11y", "react"),

    // translate an entire config
    ...compat.config({
        plugins: ["jsx-a11y", "react"],
        extends: "standard",
        env: {
            es2020: true,
            node: true
        },
        rules: {
            semi: "error"
        }
    })
];
```

## Troubleshooting
**TypeError: Missing parameter 'recommendedConfig' in FlatCompat constructor**
The `recommendedConfig` option is required when any config uses `eslint:recommended`, including any config in an `extends` clause. To fix this, follow the example above using `@eslint/js` to provide the `eslint:recommended` config.
**TypeError: Missing parameter 'allConfig' in FlatCompat constructor**
The `allConfig` option is required when any config uses `eslint:all`, including any config in an `extends` clause. To fix this, follow the example above using `@eslint/js` to provide the `eslint:all` config.

## Sponsors
The following companies, organizations, and individuals support ESLint's ongoing maintenance and development. [Become a Sponsor](https://eslint.org/donate)
to get your logo on our READMEs and [website](https://eslint.org/sponsors).
Platinum Sponsors
Gold Sponsors
Silver Sponsors
  Bronze Sponsors
         
Technology Sponsors
Technology sponsors allow us to use their products and services for free as part of a contribution to the open source ecosystem and our work.

---

# iCloud: web-app/node_modules/@eslint/eslintrc/node_modules/json-schema-traverse/README.md

> **Source:** icloud://web-app/node_modules/@eslint/eslintrc/node_modules/json-schema-traverse/README.md
> **Analyzed At:** 2026-06-13T06:32:47.367Z

## json-schema-traverse
Traverse JSON Schema passing each schema object to callback
[![Build Status](https://travis-ci.org/epoberezkin/json-schema-traverse.svg?branch=master)](https://travis-ci.org/epoberezkin/json-schema-traverse)
[![npm version](https://badge.fury.io/js/json-schema-traverse.svg)](https://www.npmjs.com/package/json-schema-traverse)
[![Coverage Status](https://coveralls.io/repos/github/epoberezkin/json-schema-traverse/badge.svg?branch=master)](https://coveralls.io/github/epoberezkin/json-schema-traverse?branch=master)

## Install
```
npm install json-schema-traverse
```

## Usage
```javascript
const traverse = require('json-schema-traverse');
const schema = {
  properties: {
    foo: {type: 'string'},
    bar: {type: 'integer'}
  }
};

traverse(schema, {cb});
// cb is called 3 times with:
// 1. root schema
// 2. {type: 'string'}
// 3. {type: 'integer'}

// Or:

traverse(schema, {cb: {pre, post}});
// pre is called 3 times with:
// 1. root schema
// 2. {type: 'string'}
// 3. {type: 'integer'}
//
// post is called 3 times with:
// 1. {type: 'string'}
// 2. {type: 'integer'}
// 3. root schema

```
Callback is passed these parameters:
- _schema_: the current schema object
- _JSON pointer_: from the root schema to the current schema object
- _root schema_: the schema passed to `traverse` object
- _parent JSON pointer_: from the root schema to the parent schema object (see below)
- _parent keyword_: the keyword inside which this schema appears (e.g. `properties`, `anyOf`, etc.)

## Traverse objects in all unknown keywords
```javascript
const traverse = require('json-schema-traverse');
const schema = {
  mySchema: {
    minimum: 1,
    maximum: 2
  }
};

traverse(schema, {allKeys: true, cb});
// cb is called 2 times with:
// 1. root schema
// 2. mySchema
```
Without option `allKeys: true` callback will be called only with root schema.

## License
[MIT](https://github.com/epoberezkin/json-schema-traverse/blob/master/LICENSE)

---

# iCloud: web-app/node_modules/@eslint/eslintrc/node_modules/js-yaml/README.md

> **Source:** icloud://web-app/node_modules/@eslint/eslintrc/node_modules/js-yaml/README.md
> **Analyzed At:** 2026-06-13T06:32:47.374Z

## Installation
------------

## YAML module for node.js
```
npm install js-yaml
```

## CLI executable
If you want to inspect your YAML files from CLI, install js-yaml globally:
```
npm install -g js-yaml
```

## Usage
```
usage: js-yaml [-h] [-v] [-c] [-t] file

Positional arguments:
  file           File with YAML document(s)

Optional arguments:
  -h, --help     Show this help message and exit.
  -v, --version  Show program's version number and exit.
  -c, --compact  Display errors in compact mode
  -t, --trace    Show stack trace on error
```

## API
---
Here we cover the most 'useful' methods. If you need advanced details (creating
your own tags), see [examples](https://github.com/nodeca/js-yaml/tree/master/examples)
for more info.
``` javascript
const yaml = require('js-yaml');
const fs   = require('fs');

// Get document, or throw exception on error
try {
  const doc = yaml.load(fs.readFileSync('/home/ixti/example.yml', 'utf8'));
  console.log(doc);
} catch (e) {
  console.log(e);
}
```

## load (string [ , options ])
Parses `string` as single YAML document. Returns either a
plain object, a string, a number, `null` or `undefined`, or throws `YAMLException` on error. By default, does
not support regexps, functions and undefined.
options:
- `filename` _(default: null)_ - string to be used as a file path in
error/warning messages.
- `onWarning` _(default: null)_ - function to call on warning messages.
Loader will call this function with an instance of `YAMLException` for each warning.
- `schema` _(default: `DEFAULT_SCHEMA`)_ - specifies a schema to use.
- `FAILSAFE_SCHEMA` - only strings, arrays and plain objects:
https://www.yaml.org/spec/1.2/spec.html#id2802346
- `JSON_SCHEMA` - all JSON-supported types:
https://www.yaml.org/spec/1.2/spec.html#id2803231
- `CORE_SCHEMA` - same as `JSON_SCHEMA`:
https://www.yaml.org/spec/1.2/spec.html#id2804923
- `DEFAULT_SCHEMA` - all supported YAML types.
- `json` _(default: false)_ - compatibility with JSON.parse behaviour. If true, then duplicate keys in a mapping will override values rather than throwing an error.
NOTE: This function **does not** understand multi-document sources, it throws
exception on those.
NOTE: JS-YAML **does not** support schema-specific tag resolution restrictions.
So, the JSON schema is not as strictly defined in the YAML specification.
It allows numbers in any notation, use `Null` and `NULL` as `null`, etc.
The core schema also has no such restrictions. It allows binary notation for integers.

## loadAll (string [, iterator] [, options ])
Same as `load()`, but understands multi-document sources. Applies
`iterator` to each document if specified, or returns array of documents.
``` javascript
const yaml = require('js-yaml');

yaml.loadAll(data, function (doc) {
  console.log(doc);
});
```

## dump (object [ , options ])
Serializes `object` as a YAML document. Uses `DEFAULT_SCHEMA`, so it will
throw an exception if you try to dump regexps or functions. However, you can
disable exceptions by setting the `skipInvalid` option to `true`.
options:
- `indent` _(default: 2)_ - indentation width to use (in spaces).
- `noArrayIndent` _(default: false)_ - when true, will not add an indentation level to array elements
- `skipInvalid` _(default: false)_ - do not throw on invalid types (like function
in the safe schema) and skip pairs and single values with such types.
- `flowLevel` _(default: -1)_ - specifies level of nesting, when to switch from
block to flow style for collections. -1 means block style everwhere
- `styles` - "tag" => "style" map. Each tag may have own set of styles.
- `schema` _(default: `DEFAULT_SCHEMA`)_ specifies a schema to use.
- `sortKeys` _(default: `false`)_ - if `true`, sort keys when dumping YAML. If a
function, use the function to sort the keys.
- `lineWidth` _(default: `80`)_ - set max line width. Set `-1` for unlimited width.
- `noRefs` _(default: `false`)_ - if `true`, don't convert duplicate objects into references
- `noCompatMode` _(default: `false`)_ - if `true` don't try to be compatible with older
yaml versions. Currently: don't quote "yes", "no" and so on, as required for YAML 1.1
- `quotingType` _(`'` or `"`, default: `'`)_ - strings will be quoted using this quoting style. If you specify single quotes, double quotes will still be used for non-printable characters.
- `forceQuotes` _(default: `false`)_ - if `true`, all non-key strings will be quoted even if they normally don't need to.
- `replacer` - callback `function (key, value)` called recursively on each key/value in source object (see `replacer` docs for `JSON.stringify`).
The following table show availlable styles (e.g. "canonical",
"binary"...) available for each tag (.e.g. !!null, !!int ...). Yaml
output is shown on the right side after `=>` (default setting) or `->`:
``` none
!!null
  "canonical"   -> "~"
  "lowercase"   => "null"
  "uppercase"   -> "NULL"
  "camelcase"   -> "Null"
  "empty"       -> ""

!!int
  "binary"      -> "0b1", "0b101010", "0b1110001111010"
  "octal"       -> "0o1", "0o52", "0o16172"
  "decimal"     => "1", "42", "7290"
  "hexadecimal" -> "0x1", "0x2A", "0x1C7A"

!!bool
  "lowercase"   => "true", "false"
  "uppercase"   -> "TRUE", "FALSE"
  "camelcase"   -> "True", "False"

!!float
  "lowercase"   => ".nan", '.inf'
  "uppercase"   -> ".NAN", '.INF'
  "camelcase"   -> ".NaN", '.Inf'
```
Example:
``` javascript
dump(object, {
  'styles': {
    '!!null': 'canonical' // dump null as ~
  },
  'sortKeys': true        // sort object keys
});
```

## Supported YAML types
--------------------
The list of standard YAML tags and corresponding JavaScript types. See also
[YAML tag discussion](https://pyyaml.org/wiki/YAMLTagDiscussion) and
[YAML types repository](https://yaml.org/type/).
```
!!null ''                   # null
!!bool 'yes'                # bool
!!int '3...'                # number
!!float '3.14...'           # number
!!binary '...base64...'     # buffer
!!timestamp 'YYYY-...'      # date
!!omap [ ... ]              # array of key-value pairs
!!pairs [ ... ]             # array or array pairs
!!set { ... }               # array of objects with given keys and null values
!!str '...'                 # string
!!seq [ ... ]               # array
!!map { ... }               # object
```
**JavaScript-specific tags**
See [js-yaml-js-types](https://github.com/nodeca/js-yaml-js-types) for
extra types.

## Caveats
-------
Note, that you use arrays or objects as key in JS-YAML. JS does not allow objects
or arrays as keys, and stringifies (by calling `toString()` method) them at the
moment of adding them.
``` yaml
---
? [ foo, bar ]
: - baz
? { foo: bar }
: - baz
  - baz
```
``` javascript
{ "foo,bar": ["baz"], "[object Object]": ["baz", "baz"] }
```
Also, reading of properties on implicit block mapping keys is not supported yet.
So, the following YAML document cannot be loaded.
``` yaml
&anchor foo:
  foo: bar
  *anchor: duplicate key
  baz: bat
  *anchor: duplicate key
```
js-yaml for enterprise
----------------------
Available as part of the Tidelift Subscription
The maintainers of js-yaml and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use. [Learn more.](https://tidelift.com/subscription/pkg/npm-js-yaml?utm_source=npm-js-yaml&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)

---

# iCloud: web-app/node_modules/@eslint/core/README.md

> **Source:** icloud://web-app/node_modules/@eslint/core/README.md
> **Analyzed At:** 2026-06-13T06:32:47.390Z

## Overview
This package is the future home of the rewritten, runtime-agnostic ESLint core.
Right now, it exports the core types necessary to implement language plugins.

## License
Apache 2.0

## Sponsors
The following companies, organizations, and individuals support ESLint's ongoing maintenance and development. [Become a Sponsor](https://eslint.org/donate)
to get your logo on our READMEs and [website](https://eslint.org/sponsors).
Platinum Sponsors
 Gold Sponsors
  Silver Sponsors
   Bronze Sponsors
         
Technology Sponsors
Technology sponsors allow us to use their products and services for free as part of a contribution to the open source ecosystem and our work.

---

# iCloud: web-app/node_modules/@eslint/config-helpers/README.md

> **Source:** icloud://web-app/node_modules/@eslint/config-helpers/README.md
> **Analyzed At:** 2026-06-13T06:32:47.397Z

## Description
Helper utilities for creating ESLint configuration.

## Installation
For Node.js and compatible runtimes:
```shell
npm install @eslint/config-helpers
# or
yarn add @eslint/config-helpers
# or
pnpm install @eslint/config-helpers
# or
bun add @eslint/config-helpers
```
For Deno:
```shell
deno add @eslint/config-helpers
```

## `defineConfig()`
The `defineConfig()` function allows you to specify an ESLint configuration with full type checking and additional capabilities, such as `extends`. Here's an example:
```js
// eslint.config.js
import { defineConfig } from "@eslint/config-helpers";
import js from "@eslint/js";

export default defineConfig([
	{
		files: ["src/**/*.js"],
		plugins: { js },
		extends: ["js/recommended"],
		rules: {
			semi: "error",
			"prefer-const": "error",
		},
	},
	{
		files: ["test/**/*.js"],
		rules: {
			"no-console": "off",
		},
	},
]);
```

## `globalIgnores()`
The `globalIgnores()` function allows you to specify patterns for files and directories that should be globally ignored by ESLint. This is useful for excluding files that you don't want to lint, such as build directories or third-party libraries. Here's an example:
```js
// eslint.config.js
import { defineConfig, globalIgnores } from "@eslint/config-helpers";

export default defineConfig([
	{
		files: ["src/**/*.js"],
		rules: {
			semi: "error",
			"prefer-const": "error",
		},
	},
	globalIgnores(["node_modules/", "dist/", "coverage/"]),
]);
```

## License
Apache 2.0

## Sponsors
The following companies, organizations, and individuals support ESLint's ongoing maintenance and development. [Become a Sponsor](https://eslint.org/donate)
to get your logo on our READMEs and [website](https://eslint.org/sponsors).
Platinum Sponsors
 Gold Sponsors
  Silver Sponsors
   Bronze Sponsors
         
Technology Sponsors
Technology sponsors allow us to use their products and services for free as part of a contribution to the open source ecosystem and our work.

---

# iCloud: web-app/node_modules/@dabh/diagnostics/CHANGELOG.md

> **Source:** icloud://web-app/node_modules/@dabh/diagnostics/CHANGELOG.md
> **Analyzed At:** 2026-06-13T06:32:47.412Z

## 2.0.2
- Bump to kuler 2.0, which removes colornames as dependency, which we
never used. So smaller install size, less dependencies for all.

## 2.0.1
- Use `storag-engine@3.0` which will automatically detect the correct
AsyncStorage implementation.
- The upgrade also fixes a bug where it the `debug` and `diagnostics` values
to be JSON encoded instead of regular plain text.

## 2.0.0
- Documentation improvements.
- Fixed a issue where async adapters were incorrectly detected.
- Correctly inherit colors after applying colors the browser's console.

## 2.0.0-alpha
- Complete rewrite of all internals, now comes with separate builds for `browser`
`node` and `react-native` as well as dedicated builds for `production` and
`development` environments. Various utility methods and properties have
been added to the returned logger to make your lives even easier.

---

# iCloud: web-app/node_modules/@dabh/diagnostics/README.md

> **Source:** icloud://web-app/node_modules/@dabh/diagnostics/README.md
> **Analyzed At:** 2026-06-13T06:32:47.420Z

## `diagnostics`
Diagnostics in the evolution of debug pattern that is used in the Node.js core,
this extremely small but powerful technique can best be compared as feature
flags for loggers. The created debug logger is disabled by default but can be
enabled without changing a line of code, using flags.
- Allows debugging in multiple JavaScript environments such as Node.js, browsers
and React-Native.
- Separated development and production builds to minimize impact on your
application when bundled.
- Allows for customization of logger, messages, and much more.
![Output Example](example.png)

## Installation
The module is released in the public npm registry and can be installed by
running:
```
npm install --save @dabh/diagnostics
```

## Usage
- [Introduction](#introduction)
- [Advanced usage](#advanced-usage)
- [Production and development builds](#production-and-development-builds)
- [WebPack](#webpack)
- [Node.js](#nodejs)
- [API](#api)
- [.enabled](#enabled)
- [.namespace](#namespace)
- [.dev/prod](#devprod)
- [set](#set)
- [modify](#modify)
- [use](#use)
- [Modifiers](#modifiers)
- [namespace](#namespace-1)
- [Adapters](#adapters)
- [process.env](#process-env)
- [hash](#hash)
- [localStorage](#localstorage)
- [AsyncStorage](#asyncstorage)
- [Loggers](#loggers)

## Introduction
To create a new logger simply `require` the `@dabh/diagnostics` module and call
the returned function. It accepts 2 arguments:
1. `namespace` **Required** This is the namespace of your logger so we know if we need to
enable your logger when a debug flag is used. Generally you use the name of
your library or application as first root namespace. For example if you're
building a parser in a library (example) you would set namespace
`example:parser`.
2. `options` An object with additional configuration for the logger.
following keys are recognized:
- `force` Force the logger to be enabled.
- `colors` Colors are enabled by default for the logs, but you can set this
option to `false` to disable it.
```js
const debug = require('@dabh/diagnostics')('foo:bar:baz');
const debug = require('@dabh/diagnostics')('foo:bar:baz', { options });

debug('this is a log message %s', 'that will only show up when enabled');
debug('that is pretty neat', { log: 'more', data: 1337 });
```
Unlike `console.log` statements that add and remove during your development
lifecycle you create meaningful log statements that will give you insight in
the library or application that you're developing.
The created debugger uses different "adapters" to extract the debug flag
out of the JavaScript environment. To learn more about enabling the debug flag
in your specific environment click on one of the enabled adapters below.
- **browser**: [localStorage](#localstorage), [hash](#hash)
- **node.js**: [environment variables](#processenv)
- **react-native**: [AsyncStorage](#asyncstorage)
Please note that the returned logger is fully configured out of the box, you
do not need to set any of the adapters/modifiers your self, they are there
for when you want more advanced control over the process. But if you want to
learn more about that, read the next section.

## Advanced usage
There are 2 specific usage patterns for `diagnostic`, library developers who
implement it as part of their modules and applications developers who either
use it in their application or are searching for ways to consume the messages.
With the simple log interface as discussed in the [introduction](#introduction)
section we make it easy for developers to add it as part of their libraries
and applications, and with powerful [API](#api) we allow infinite customization
by allowing custom adapters, loggers and modifiers to ensure that this library
maintains relevant. These methods not only allow introduction of new loggers,
but allow you think outside the box. For example you can maintain a history
of past log messages, and output those when an uncaught exception happens in
your application so you have additional context
```js
const diagnostics = require('@dabh/diagnostics');

let index = 0;
const limit = 200;
const history = new Array(limit);

//
// Force all `diagnostic` loggers to be enabled.
//
diagnostics.force = process.env.NODE_ENV === 'prod';
diagnostics.set(function customLogger(meta, message) {
  history[index]= { meta, message, now: Date.now() };
  if (index++ === limit) index = 0;

  //
  // We're running a development build, so output.
  //
  if (meta.dev) console.log.apply(console, message);
});

process.on('uncaughtException', async function (err) {
  await saveErrorToDisk(err, history);
  process.exit(1);
});
```
The small snippet above will maintain a 200 limited FIFO (First In First Out)
queue of all debug messages that can be referenced when your application crashes

## Production and development builds
When you `require` the `@dabh/diagnostics` module you will be given a logger that is
optimized for `development` so it can provide the best developer experience
possible.
The development logger enables all the [adapters](#adapters) for your
JavaScript environment, adds a logger that outputs the messages to `console.log`
and registers our message modifiers so log messages will be prefixed with the
supplied namespace so you know where the log messages originates from.
The development logger does not have any adapter, modifier and logger enabled
by default. This ensures that your log messages never accidentally show up in
production. However this does not mean that it's not possible to get debug
messages in production. You can `force` the debugger to be enabled, and
supply a [custom logger](#loggers).
```js
const diagnostics = require('@dabh/diagnostics');
const debug = debug('foo:bar', { force: true });

//
// Or enable _every_ diagnostic instance:
//
diagnostics.force = true;
```

## WebPack
WebPack has the concept of [mode](https://webpack.js.org/concepts/mode/#usage)'s
which creates different
```js
module.exports = {
  mode: 'development' // 'production'
}
```
When you are building your app using the WebPack CLI you can use the `--mode`
flag:
```
webpack --mode=production app.js -o /dist/bundle.js
```

## Node.js
When you are running your app using `Node.js` you should the `NODE_ENV`
environment variable to `production` to ensure that you libraries that you
import are optimized for production.
```
NODE_ENV=production node app.js
```

## API
The returned logger exposes some addition properties that can be used used in
your application or library:

## .enabled
The returned logger will have a `.enabled` property assigned to it. This boolean
can be used to check if the logger was enabled:
```js
const debug = require('@dabh/diagnostics')('foo:bar');

if (debug.enabled) {
  //
  // Do something special
  //
}
```
This property is exposed as:
- Property on the logger.
- Property on the meta/options object.

## .namespace
This is the namespace that you originally provided to the function.
```js
const debug = require('@dabh/diagnostics')('foo:bar');

console.log(debug.namespace); // foo:bar
```
This property is exposed as:
- Property on the logger.
- Property on the meta/options object.

## .dev/prod
There are different builds available of `diagnostics`, when you create a
production build of your application using `NODE_ENV=production` you will be
given an optimized, smaller build of `diagnostics` to reduce your bundle size.
The `dev` and `prod` booleans on the returned logger indicate if you have a
production or development version of the logger.
```js
const debug = require('@dabh/diagnostics')('foo:bar');

if (debug.prod) {
  // do stuff
}
```
This property is exposed as:
- Property on the logger.
- Property on the meta/options object.

## set
Sets a new logger as default for  **all** `diagnostic` instances. The passed
argument should be a function that write the log messages to where ever you
want. It receives 2 arguments:
1. `meta` An object with all the options that was provided to the original
logger that wants to write the log message as well as properties of the
debugger such as `prod`, `dev`, `namespace`, `enabled`. See [API](#api) for
all exposed properties.
2. `args` An array of the log messages that needs to be written.
```js
const debug = require('@dabh/diagnostics')('foo:more:namespaces');

debug.use(function logger(meta, args) {
  console.log(meta);
  console.debug(...args);
});
```
This method is exposed as:
- Method on the logger.
- Method on the meta/options object.
- Method on `diagnostics` module.

## modify
The modify method allows you add a new message modifier to **all** `diagnostic`
instances. The passed argument should be a function that returns the passed
message after modification. The function receives 2 arguments:
1. `message`, Array, the log message.
2. `options`, Object, the options that were passed into the logger when it was
initially created.
```js
const debug = require('@dabh/diagnostics')('example:modifiers');

debug.modify(function (message, options) {
  return messages;
});
```
This method is exposed as:
- Method on the logger.
- Method on the meta/options object.
- Method on `diagnostics` module.
See [modifiers](#modifiers) for more information.

## use
Adds a new `adapter` to **all** `diagnostic` instances. The passed argument
should be a function returns a boolean that indicates if the passed in
`namespace` is allowed to write log messages.
```js
const diagnostics = require('@dabh/diagnostics');
const debug = diagnostics('foo:bar');

debug.use(function (namespace) {
  return namespace === 'foo:bar';
});
```
This method is exposed as:
- Method on the logger.
- Method on the meta/options object.
- Method on `diagnostics` module.
See [adapters](#adapters) for more information.

## Modifiers
To be as flexible as possible when it comes to transforming messages we've
come up with the concept of `modifiers` which can enhance the debug messages.
This allows you to introduce functionality or details that you find important
for debug messages, and doesn't require us to add additional bloat to the
`diagnostic` core.
For example, you want the messages to be prefixed with the date-time of when
the log message occured:
```js
const diagnostics = require('@dabh/diagnostics');

diagnostics.modify(function datetime(args, options) {
  args.unshift(new Date());
  return args;
});
```
Now all messages will be prefixed with date that is outputted by `new Date()`.
The following modifiers are shipped with `diagnostics` and are enabled in
**development** mode only:
- [namespace](#namespace)

## namespace
This modifier is enabled for all debug instances and prefixes the messages
with the name of namespace under which it is logged. The namespace is colored
using the `colorspace` module which groups similar namespaces under the same
colorspace. You can have multiple namespaces for the debuggers where each
namespace should be separated by a `:`
```
foo
foo:bar
foo:bar:baz
```
For console based output the `namespace-ansi` is used.

## Adapters
Adapters allows `diagnostics` to pull the `DEBUG` and `DIAGNOSTICS` environment
variables from different sources. Not every JavaScript environment has a
`process.env` that we can leverage. Adapters allows us to have different
adapters for different environments. It means you can write your own custom
adapter if needed as well.
The `adapter` function should be passed a function as argument, this function
will receive the `namespace` of a logger as argument and it should return a
boolean that indicates if that logger should be enabled or not.
```js
const debug = require('@dabh/diagnostics')('example:namespace');

debug.adapter(require('@dabh/diagnostics/adapters/localstorage'));
```
The modifiers are only enabled for `development`. The following adapters are
available are available:

## process.env
This adapter is enabled for `node.js`.
Uses the `DEBUG` or `DIAGNOSTICS` (both are recognized) environment variables to
pass in debug flag:
**UNIX/Linux/Mac**
```
DEBUG=foo* node index.js
```
Using environment variables on Windows is a bit different, and also depends on
toolchain you are using:
**Windows**
```
set DEBUG=foo* & node index.js
```
**Powershell**
```
$env:DEBUG='foo*';node index.js
```

## hash
This adapter is enabled for `browsers`.
This adapter uses the `window.location.hash` of as source for the environment
variables. It assumes that hash is formatted using the same syntax as query
strings:
```js
http://example.com/foo/bar#debug=foo*
```
It triggers on both the `debug=` and `diagnostics=` names.

## localStorage
This adapter is enabled for `browsers`.
This adapter uses the `localStorage` of the browser to store the debug flags.
You can set the debug flag your self in your application code, but you can
also open browser WebInspector and enable it through the console.
```js
localStorage.setItem('debug', 'foo*');
```
It triggers on both the `debug` and `diagnostics` storage items. (Please note
that these keys should be entered in lowercase)

## AsyncStorage
This adapter is enabled for `react-native`.
This adapter uses the `AsyncStorage` API that is exposed by the `react-native`
library to store and read the `debug` or `diagnostics` storage items.
```js
import { AsyncStorage } from 'react-native';

AsyncStorage.setItem('debug', 'foo*');
```
Unlike other adapters, this is the only adapter that is `async` so that means
that we're not able to instantly determine if a created logger should be
enabled or disabled. So when a logger is created in `react-native` we initially
assume it's disabled, any message that send during period will be queued
internally.
Once we've received the data from the `AsyncStorage` API we will determine
if the logger should be enabled, flush the queued messages if needed and set
all `enabled` properties accordingly on the returned logger.

## Loggers
By default it will log all messages to `console.log` in when the logger is
enabled using the debug flag that is set using one of the adapters.

## License
[MIT](LICENSE)

---

# iCloud: web-app/node_modules/@colors/colors/README.md

> **Source:** icloud://web-app/node_modules/@colors/colors/README.md
> **Analyzed At:** 2026-06-13T06:32:47.427Z

## @colors/colors ("colors.js")
[![Build Status](https://github.com/DABH/colors.js/actions/workflows/ci.yml/badge.svg)](https://github.com/DABH/colors.js/actions/workflows/ci.yml)
[![version](https://img.shields.io/npm/v/@colors/colors.svg)](https://www.npmjs.org/package/@colors/colors)
Please check out the [roadmap](ROADMAP.md) for upcoming features and releases.  Please open Issues to provide feedback.

## get color and style in your node.js console
![Demo](https://raw.githubusercontent.com/DABH/colors.js/master/screenshots/colors.png)

## Installation
npm install @colors/colors

## text colors
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- gray
- grey

## bright text colors
- brightRed
- brightGreen
- brightYellow
- brightBlue
- brightMagenta
- brightCyan
- brightWhite

## background colors
- bgBlack
- bgRed
- bgGreen
- bgYellow
- bgBlue
- bgMagenta
- bgCyan
- bgWhite
- bgGray
- bgGrey

## bright background colors
- bgBrightRed
- bgBrightGreen
- bgBrightYellow
- bgBrightBlue
- bgBrightMagenta
- bgBrightCyan
- bgBrightWhite

## styles
- reset
- bold
- dim
- italic
- underline
- inverse
- hidden
- strikethrough

## extras
- rainbow
- zebra
- america
- trap
- random

## Usage
By popular demand, `@colors/colors` now ships with two types of usages!

## The super nifty way
```js
var colors = require('@colors/colors');

console.log('hello'.green); // outputs green text
console.log('i like cake and pies'.underline.red); // outputs red underlined text
console.log('inverse the color'.inverse); // inverses the color
console.log('OMG Rainbows!'.rainbow); // rainbow
console.log('Run the trap'.trap); // Drops the bass

```
or a slightly less nifty way which doesn't extend `String.prototype`
```js
var colors = require('@colors/colors/safe');

console.log(colors.green('hello')); // outputs green text
console.log(colors.red.underline('i like cake and pies')); // outputs red underlined text
console.log(colors.inverse('inverse the color')); // inverses the color
console.log(colors.rainbow('OMG Rainbows!')); // rainbow
console.log(colors.trap('Run the trap')); // Drops the bass

```
I prefer the first way. Some people seem to be afraid of extending `String.prototype` and prefer the second way.
If you are writing good code you will never have an issue with the first approach. If you really don't want to touch `String.prototype`, the second usage will not touch `String` native object.

## Enabling/Disabling Colors
The package will auto-detect whether your terminal can use colors and enable/disable accordingly. When colors are disabled, the color functions do nothing. You can override this with a command-line flag:
```bash
node myapp.js --no-color
node myapp.js --color=false

node myapp.js --color
node myapp.js --color=true
node myapp.js --color=always

FORCE_COLOR=1 node myapp.js
```
Or in code:
```javascript
var colors = require('@colors/colors');
colors.enable();
colors.disable();
```

## Console.log [string substitution](http://nodejs.org/docs/latest/api/console.html#console_console_log_data)
```js
var name = 'Beowulf';
console.log(colors.green('Hello %s'), name);
// outputs -> 'Hello Beowulf'
```

## Using standard API
```js

var colors = require('@colors/colors');

colors.setTheme({
  silly: 'rainbow',
  input: 'grey',
  verbose: 'cyan',
  prompt: 'grey',
  info: 'green',
  data: 'grey',
  help: 'cyan',
  warn: 'yellow',
  debug: 'blue',
  error: 'red'
});

// outputs red text
console.log("this is an error".error);

// outputs yellow text
console.log("this is a warning".warn);
```

## Using string safe API
```js
var colors = require('@colors/colors/safe');

// set single property
var error = colors.red;
error('this is red');

// set theme
colors.setTheme({
  silly: 'rainbow',
  input: 'grey',
  verbose: 'cyan',
  prompt: 'grey',
  info: 'green',
  data: 'grey',
  help: 'cyan',
  warn: 'yellow',
  debug: 'blue',
  error: 'red'
});

// outputs red text
console.log(colors.error("this is an error"));

// outputs yellow text
console.log(colors.warn("this is a warning"));

```

## Combining Colors
```javascript
var colors = require('@colors/colors');

colors.setTheme({
  custom: ['red', 'underline']
});

console.log('test'.custom);
```
*Protip: There is a secret undocumented style in `colors`. If you find the style you can summon him.*

---

# iCloud: web-app/node_modules/@builder.io/partytown/README.md

> **Source:** icloud://web-app/node_modules/@builder.io/partytown/README.md
> **Analyzed At:** 2026-06-13T06:32:47.434Z

## Partytown 🎉
- [Introducing Partytown: Run Third-Party Scripts From a Web Worker](https://dev.to/adamdbradley/introducing-partytown-run-third-party-scripts-from-a-web-worker-2cnp)
- [How Partytown's Sync Communication Works](https://dev.to/adamdbradley/how-partytown-s-sync-communication-works-4244)
- [How we cut 99% of our JavaScript with Qwik + Partytown](https://www.builder.io/blog/how-we-cut-99-percent-js-with-qwik-and-partytown)
- [Partytown is now in Beta](https://www.builder.io/blog/partytown-is-now-in-beta)
> A fun location for your third-party scripts to hang out
Partytown is a lazy-loaded library to help relocate resource intensive scripts into a [web worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API), and off of the [main thread](https://developer.mozilla.org/en-US/docs/Glossary/Main_thread). Its goal is to help speed up sites by dedicating the main thread to your code, and offloading third-party scripts to a web worker.
> Note: Partytown is still in beta and not guaranteed to work in every scenario. Please see our [FAQ](https://partytown.builder.io/faq) and [Trade-Off](https://partytown.builder.io/trade-offs) sections for more info.
The philosophy is that the main thread should be dedicated to your code, and any scripts that are not required to be in the [critical path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path) should be moved to a web worker. Main thread performance is, without question, more important than web worker thread performance.
- [Getting Started](https://partytown.builder.io/getting-started)
- [Integrations](https://partytown.builder.io/integrations)
- [Configuration](https://partytown.builder.io/configuration)
- [Releases](https://github.com/BuilderIO/partytown/releases)
- [FAQs](https://partytown.builder.io/faq)
![Without Partytown and With Partytown: Your code and third-party code compete for main thread resources](https://user-images.githubusercontent.com/452425/152393346-6f721a4f-3f66-410a-8878-a2b49e24307f.png)

## Community
- [@QwikDev](https://twitter.com/QwikDev)
- [@Builderio](https://twitter.com/builderio)
- [Local Development](https://github.com/BuilderIO/partytown/blob/main/CONTRIBUTING.md#local-development)
- [For Plugin Authors / Developers](https://github.com/BuilderIO/partytown/blob/main/CONTRIBUTING.md#plugin-authors-developers)

## Related Projects
- [Qwik](https://github.com/BuilderIO/qwik): An open-source framework designed for best possible time to interactive, by focusing on resumability of server-side-rendering of HTML, and fine-grained lazy-loading of code.
- [Mitosis](https://github.com/BuilderIO/mitosis): Write components once, run everywhere. Compiles to Vue, React, Solid, Angular, Svelte, and more.
- [Builder](https://github.com/BuilderIO/builder): Drag and drop page builder and CMS for React, Vue, Angular, and more.

---

# iCloud: web-app/node_modules/@babel/template/README.md

> **Source:** icloud://web-app/node_modules/@babel/template/README.md
> **Analyzed At:** 2026-06-13T06:32:47.442Z

## @babel/template
> Generate an AST from a string template.
See our website [@babel/template](https://babeljs.io/docs/babel-template) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20template%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/template
```
or using yarn:
```sh
yarn add @babel/template --dev
```

---

# iCloud: web-app/node_modules/@babel/template/node_modules/@babel/types/README.md

> **Source:** icloud://web-app/node_modules/@babel/template/node_modules/@babel/types/README.md
> **Analyzed At:** 2026-06-13T06:32:47.449Z

## @babel/types
> Babel Types is a Lodash-esque utility library for AST nodes
See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20types%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/types
```
or using yarn:
```sh
yarn add @babel/types --dev
```

---

# iCloud: web-app/node_modules/@babel/runtime/README.md

> **Source:** icloud://web-app/node_modules/@babel/runtime/README.md
> **Analyzed At:** 2026-06-13T06:32:47.462Z

## @babel/runtime
> babel's modular runtime helpers
See our website [@babel/runtime](https://babeljs.io/docs/babel-runtime) for more information.

## Install
Using npm:
```sh
npm install --save @babel/runtime
```
or using yarn:
```sh
yarn add @babel/runtime
```

---

# iCloud: web-app/node_modules/@babel/parser/README.md

> **Source:** icloud://web-app/node_modules/@babel/parser/README.md
> **Analyzed At:** 2026-06-13T06:32:47.477Z

## @babel/parser
> A JavaScript parser
See our website [@babel/parser](https://babeljs.io/docs/babel-parser) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20parser%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/parser
```
or using yarn:
```sh
yarn add @babel/parser --dev
```

---

# iCloud: web-app/node_modules/@babel/parser/node_modules/@babel/types/README.md

> **Source:** icloud://web-app/node_modules/@babel/parser/node_modules/@babel/types/README.md
> **Analyzed At:** 2026-06-13T06:32:47.483Z

## @babel/types
> Babel Types is a Lodash-esque utility library for AST nodes
See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20types%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/types
```
or using yarn:
```sh
yarn add @babel/types --dev
```

---

# iCloud: web-app/node_modules/@babel/helper-validator-option/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-validator-option/README.md
> **Analyzed At:** 2026-06-13T06:32:47.519Z

## @babel/helper-validator-option
> Validate plugin/preset options
See our website [@babel/helper-validator-option](https://babeljs.io/docs/babel-helper-validator-option) for more information.

## Install
Using npm:
```sh
npm install --save @babel/helper-validator-option
```
or using yarn:
```sh
yarn add @babel/helper-validator-option
```

---

# iCloud: web-app/node_modules/@babel/helper-validator-identifier/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-validator-identifier/README.md
> **Analyzed At:** 2026-06-13T06:32:47.526Z

## @babel/helper-validator-identifier
> Validate identifier/keywords name
See our website [@babel/helper-validator-identifier](https://babeljs.io/docs/babel-helper-validator-identifier) for more information.

## Install
Using npm:
```sh
npm install --save @babel/helper-validator-identifier
```
or using yarn:
```sh
yarn add @babel/helper-validator-identifier
```

---

# iCloud: web-app/node_modules/@babel/helper-string-parser/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-string-parser/README.md
> **Analyzed At:** 2026-06-13T06:32:47.533Z

## @babel/helper-string-parser
> A utility package to parse strings
See our website [@babel/helper-string-parser](https://babeljs.io/docs/babel-helper-string-parser) for more information.

## Install
Using npm:
```sh
npm install --save @babel/helper-string-parser
```
or using yarn:
```sh
yarn add @babel/helper-string-parser
```

---

# iCloud: web-app/node_modules/@babel/helper-module-transforms/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-module-transforms/README.md
> **Analyzed At:** 2026-06-13T06:32:47.540Z

## @babel/helper-module-transforms
> Babel helper functions for implementing ES6 module transformations
See our website [@babel/helper-module-transforms](https://babeljs.io/docs/babel-helper-module-transforms) for more information.

## Install
Using npm:
```sh
npm install --save @babel/helper-module-transforms
```
or using yarn:
```sh
yarn add @babel/helper-module-transforms
```

---

# iCloud: web-app/node_modules/@babel/helper-module-transforms/node_modules/@babel/types/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-module-transforms/node_modules/@babel/types/README.md
> **Analyzed At:** 2026-06-13T06:32:47.547Z

## @babel/types
> Babel Types is a Lodash-esque utility library for AST nodes
See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20types%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/types
```
or using yarn:
```sh
yarn add @babel/types --dev
```

---

# iCloud: web-app/node_modules/@babel/helper-module-transforms/node_modules/@babel/traverse/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-module-transforms/node_modules/@babel/traverse/README.md
> **Analyzed At:** 2026-06-13T06:32:47.564Z

## @babel/traverse
> The Babel Traverse module maintains the overall tree state, and is responsible for replacing, removing, and adding nodes
See our website [@babel/traverse](https://babeljs.io/docs/babel-traverse) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20traverse%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/traverse
```
or using yarn:
```sh
yarn add @babel/traverse --dev
```

---

# iCloud: web-app/node_modules/@babel/helper-module-imports/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-module-imports/README.md
> **Analyzed At:** 2026-06-13T06:32:47.576Z

## @babel/helper-module-imports
> Babel helper functions for inserting module loads
See our website [@babel/helper-module-imports](https://babeljs.io/docs/babel-helper-module-imports) for more information.

## Install
Using npm:
```sh
npm install --save @babel/helper-module-imports
```
or using yarn:
```sh
yarn add @babel/helper-module-imports
```

---

# iCloud: web-app/node_modules/@babel/helper-module-imports/node_modules/@babel/types/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-module-imports/node_modules/@babel/types/README.md
> **Analyzed At:** 2026-06-13T06:32:47.584Z

## @babel/types
> Babel Types is a Lodash-esque utility library for AST nodes
See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20types%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/types
```
or using yarn:
```sh
yarn add @babel/types --dev
```

---

# iCloud: web-app/node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-module-imports/node_modules/@babel/traverse/README.md
> **Analyzed At:** 2026-06-13T06:32:47.595Z

## @babel/traverse
> The Babel Traverse module maintains the overall tree state, and is responsible for replacing, removing, and adding nodes
See our website [@babel/traverse](https://babeljs.io/docs/babel-traverse) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20traverse%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/traverse
```
or using yarn:
```sh
yarn add @babel/traverse --dev
```

---

# iCloud: web-app/node_modules/@babel/helper-globals/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-globals/README.md
> **Analyzed At:** 2026-06-13T06:32:47.604Z

## @babel/helper-globals
> A collection of JavaScript globals for Babel internal usage
See our website [@babel/helper-globals](https://babeljs.io/docs/babel-helper-globals) for more information.

## Install
Using npm:
```sh
npm install --save @babel/helper-globals
```
or using yarn:
```sh
yarn add @babel/helper-globals
```

---

# iCloud: web-app/node_modules/@babel/helper-compilation-targets/README.md

> **Source:** icloud://web-app/node_modules/@babel/helper-compilation-targets/README.md
> **Analyzed At:** 2026-06-13T06:32:47.614Z

## @babel/helper-compilation-targets
> Helper functions on Babel compilation targets
See our website [@babel/helper-compilation-targets](https://babeljs.io/docs/babel-helper-compilation-targets) for more information.

## Install
Using npm:
```sh
npm install --save @babel/helper-compilation-targets
```
or using yarn:
```sh
yarn add @babel/helper-compilation-targets
```

---

# iCloud: web-app/node_modules/@babel/generator/README.md

> **Source:** icloud://web-app/node_modules/@babel/generator/README.md
> **Analyzed At:** 2026-06-13T06:32:47.622Z

## @babel/generator
> Turns an AST into code.
See our website [@babel/generator](https://babeljs.io/docs/babel-generator) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20generator%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/generator
```
or using yarn:
```sh
yarn add @babel/generator --dev
```

---

# iCloud: web-app/node_modules/@babel/generator/node_modules/@babel/types/README.md

> **Source:** icloud://web-app/node_modules/@babel/generator/node_modules/@babel/types/README.md
> **Analyzed At:** 2026-06-13T06:32:47.629Z

## @babel/types
> Babel Types is a Lodash-esque utility library for AST nodes
See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20types%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/types
```
or using yarn:
```sh
yarn add @babel/types --dev
```

---

# iCloud: web-app/node_modules/@babel/core/README.md

> **Source:** icloud://web-app/node_modules/@babel/core/README.md
> **Analyzed At:** 2026-06-13T06:32:47.641Z

## @babel/core
> Babel compiler core.
See our website [@babel/core](https://babeljs.io/docs/babel-core) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20core%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/core
```
or using yarn:
```sh
yarn add @babel/core --dev
```

---

# iCloud: web-app/node_modules/@babel/core/node_modules/@babel/types/README.md

> **Source:** icloud://web-app/node_modules/@babel/core/node_modules/@babel/types/README.md
> **Analyzed At:** 2026-06-13T06:32:47.650Z

## @babel/types
> Babel Types is a Lodash-esque utility library for AST nodes
See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20types%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/types
```
or using yarn:
```sh
yarn add @babel/types --dev
```

---

# iCloud: web-app/node_modules/@babel/core/node_modules/@babel/traverse/README.md

> **Source:** icloud://web-app/node_modules/@babel/core/node_modules/@babel/traverse/README.md
> **Analyzed At:** 2026-06-13T06:32:47.669Z

## @babel/traverse
> The Babel Traverse module maintains the overall tree state, and is responsible for replacing, removing, and adding nodes
See our website [@babel/traverse](https://babeljs.io/docs/babel-traverse) for more information or the [issues](https://github.com/babel/babel/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3A%22pkg%3A%20traverse%22+is%3Aopen) associated with this package.

## Install
Using npm:
```sh
npm install --save-dev @babel/traverse
```
or using yarn:
```sh
yarn add @babel/traverse --dev
```

---

# iCloud: web-app/node_modules/@babel/core/node_modules/@babel/helpers/README.md

> **Source:** icloud://web-app/node_modules/@babel/core/node_modules/@babel/helpers/README.md
> **Analyzed At:** 2026-06-13T06:32:47.676Z

## @babel/helpers
> Collection of helper functions used by Babel transforms.
See our website [@babel/helpers](https://babeljs.io/docs/babel-helpers) for more information.

## Install
Using npm:
```sh
npm install --save-dev @babel/helpers
```
or using yarn:
```sh
yarn add @babel/helpers --dev
```

---

# iCloud: web-app/node_modules/@babel/compat-data/README.md

> **Source:** icloud://web-app/node_modules/@babel/compat-data/README.md
> **Analyzed At:** 2026-06-13T06:32:47.697Z

## @babel/compat-data
> The compat-data to determine required Babel plugins
See our website [@babel/compat-data](https://babeljs.io/docs/babel-compat-data) for more information.

## Install
Using npm:
```sh
npm install --save @babel/compat-data
```
or using yarn:
```sh
yarn add @babel/compat-data
```

---

# iCloud: web-app/node_modules/@babel/code-frame/README.md

> **Source:** icloud://web-app/node_modules/@babel/code-frame/README.md
> **Analyzed At:** 2026-06-13T06:32:47.704Z

## @babel/code-frame
> Generate errors that contain a code frame that point to source locations.
See our website [@babel/code-frame](https://babeljs.io/docs/babel-code-frame) for more information.

## Install
Using npm:
```sh
npm install --save-dev @babel/code-frame
```
or using yarn:
```sh
yarn add @babel/code-frame --dev
```

---

# iCloud: web-app/node_modules/@alloc/quick-lru/readme.md

> **Source:** icloud://web-app/node_modules/@alloc/quick-lru/readme.md
> **Analyzed At:** 2026-06-13T06:32:47.711Z

## quick-lru [![Build Status](https://travis-ci.org/sindresorhus/quick-lru.svg?branch=master)](https://travis-ci.org/sindresorhus/quick-lru) [![Coverage Status](https://coveralls.io/repos/github/sindresorhus/quick-lru/badge.svg?branch=master)](https://coveralls.io/github/sindresorhus/quick-lru?branch=master)
> Simple [“Least Recently Used” (LRU) cache](https://en.m.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_.28LRU.29)
Useful when you need to cache something and limit memory usage.
Inspired by the [`hashlru` algorithm](https://github.com/dominictarr/hashlru#algorithm), but instead uses [`Map`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Map) to support keys of any type, not just strings, and values can be `undefined`.

## Install
```
$ npm install quick-lru
```

## Usage
```js
const QuickLRU = require('quick-lru');

const lru = new QuickLRU({maxSize: 1000});

lru.set('🦄', '🌈');

lru.has('🦄');
//=> true

lru.get('🦄');
//=> '🌈'
```

## new QuickLRU(options?)
Returns a new instance.

## options
Type: `object`

## maxSize
*Required*\
Type: `number`
The maximum number of items before evicting the least recently used items.

## maxAge
Type: `number`\
Default: `Infinity`
The maximum number of milliseconds an item should remain in cache.
By default maxAge will be Infinity, which means that items will never expire.
Lazy expiration happens upon the next `write` or `read` call.
Individual expiration of an item can be specified by the `set(key, value, options)` method.

## onEviction
*Optional*\
Type: `(key, value) => void`
Called right before an item is evicted from the cache.
Useful for side effects or for items like object URLs that need explicit cleanup (`revokeObjectURL`).

## Instance
The instance is [`iterable`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Iteration_protocols) so you can use it directly in a [`for…of`](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for...of) loop.
Both `key` and `value` can be of any type.

## .set(key, value, options?)
Set an item. Returns the instance.
Individual expiration of an item can be specified with the `maxAge` option. If not specified, the global `maxAge` value will be used in case it is specified on the constructor, otherwise the item will never expire.

## .get(key)
Get an item.

## .has(key)
Check if an item exists.

## .peek(key)
Get an item without marking it as recently used.

## .delete(key)
Delete an item.
Returns `true` if the item is removed or `false` if the item doesn't exist.

## .clear()
Delete all items.

## .resize(maxSize)
Update the `maxSize`, discarding items as necessary. Insertion order is mostly preserved, though this is not a strong guarantee.
Useful for on-the-fly tuning of cache sizes in live systems.

## .keys()
Iterable for all the keys.

## .values()
Iterable for all the values.

## .entriesAscending()
Iterable for all entries, starting with the oldest (ascending in recency).

## .entriesDescending()
Iterable for all entries, starting with the newest (descending in recency).

## .size
The stored item count.
---
Get professional support for this package with a Tidelift subscription
Tidelift helps make open source sustainable for maintainers while giving companiesassurances about security, maintenance, and licensing for their dependencies.

---

# iCloud: web-app/node_modules/3d-force-graph/README.md

> **Source:** icloud://web-app/node_modules/3d-force-graph/README.md
> **Analyzed At:** 2026-06-13T06:32:47.719Z

## Examples
* [Basic](https://vasturiano.github.io/3d-force-graph/example/basic/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/basic/index.html))
* [Asynchronous load](https://vasturiano.github.io/3d-force-graph/example/async-load/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/async-load/index.html))
* [Larger graph (~4k elements)](https://vasturiano.github.io/3d-force-graph/example/large-graph/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/large-graph/index.html))
* [Directional arrows](https://vasturiano.github.io/3d-force-graph/example/directional-links-arrows/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/directional-links-arrows/index.html))
* [Directional moving particles](https://vasturiano.github.io/3d-force-graph/example/directional-links-particles/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/directional-links-particles/index.html))
* [Curved lines and self links](https://vasturiano.github.io/3d-force-graph/example/curved-links/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/curved-links/index.html))
* [Auto-colored nodes/links](https://vasturiano.github.io/3d-force-graph/example/auto-colored/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/auto-colored/index.html))
* [Text as nodes](https://vasturiano.github.io/3d-force-graph/example/text-nodes/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/text-nodes/index.html))
* [Images as nodes](https://vasturiano.github.io/3d-force-graph/example/img-nodes/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/img-nodes/index.html))
* [HTML in nodes](https://vasturiano.github.io/3d-force-graph/example/html-nodes/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/html-nodes/index.html))
* [Custom node geometries](https://vasturiano.github.io/3d-force-graph/example/custom-node-geometry/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/custom-node-geometry/index.html))
* [Gradient Links](https://vasturiano.github.io/3d-force-graph/example/gradient-links/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/gradient-links/index.html))
* [Text in Links](https://vasturiano.github.io/3d-force-graph/example/text-links/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/text-links/index.html))
* [Orbit controls](https://vasturiano.github.io/3d-force-graph/example/controls-orbit/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/controls-orbit/index.html))
* [Fly controls](https://vasturiano.github.io/3d-force-graph/example/controls-fly/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/controls-fly/index.html))
* [Camera automatic orbitting](https://vasturiano.github.io/3d-force-graph/example/camera-auto-orbit/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/camera-auto-orbit/index.html))
* [Click to focus on node](https://vasturiano.github.io/3d-force-graph/example/click-to-focus/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/click-to-focus/index.html))
* [Click to expand/collapse nodes](https://vasturiano.github.io/3d-force-graph/example/expandable-nodes/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/expandable-nodes/index.html))
* [Fix nodes after dragging](https://vasturiano.github.io/3d-force-graph/example/fix-dragged-nodes/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/fix-dragged-nodes/index.html))
* [Fit graph to canvas](https://vasturiano.github.io/3d-force-graph/example/fit-to-canvas/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/fit-to-canvas/index.html))
* [Highlight nodes/links](https://vasturiano.github.io/3d-force-graph/example/highlight/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/highlight/index.html))
* [Multiple Node Selection](https://vasturiano.github.io/3d-force-graph/example/multi-selection/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/multi-selection/index.html))
* [Dynamic data changes](https://vasturiano.github.io/3d-force-graph/example/dynamic/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/dynamic/index.html))
* [Node collision detection](https://vasturiano.github.io/3d-force-graph/example/collision-detection/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/collision-detection/index.html))
* [Manipulate link force distance](https://vasturiano.github.io/3d-force-graph/example/manipulate-link-force/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/manipulate-link-force/index.html))
* [Emit link particles on demand](https://vasturiano.github.io/3d-force-graph/example/emit-particles/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/emit-particles/index.html))
* [Force-directed tree (DAG mode)](https://vasturiano.github.io/3d-force-graph/example/tree/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/tree/index.html))
* [yarn.lock dependency graph (DAG mode)](https://vasturiano.github.io/3d-force-graph/example/dag-yarn/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/dag-yarn/index.html))
* [Add external objects to scene](https://vasturiano.github.io/3d-force-graph/example/scene/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/scene/index.html))
* [Bloom Post-Processing Effect](https://vasturiano.github.io/3d-force-graph/example/bloom-effect/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/bloom-effect/index.html))
* [Pause / Resume animation](https://vasturiano.github.io/3d-force-graph/example/pause-resume/) ([source](https://github.com/vasturiano/3d-force-graph/blob/master/example/pause-resume/index.html))

## ❤️ Support This Project
If you find this module useful and would like to support its development, you can [buy me a ☕](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=L398E7PKP47E8&currency_code=USD&source=url). Your contributions help keep open-source sustainable!
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=L398E7PKP47E8&currency_code=USD&source=url)

## Quick start
```js
import ForceGraph3D from '3d-force-graph';
```
or using a *script* tag
```html

```
then
```js
const myGraph = new ForceGraph3D(<myDOMElement>)
  .graphData(<myData>);
```

## Initialisation
```js
new ForceGraph3d(<domElement>, { configOptions })
```
| Config options | Description | Default |
| --- | --- | :--: |
| controlType: str | Which type of control to use to control the camera. Choice between [trackball](https://threejs.org/examples/misc_controls_trackball.html), [orbit](https://threejs.org/examples/#misc_controls_orbit) or [fly](https://threejs.org/examples/misc_controls_fly.html). | `trackball` |
| extraRenderers: array | If you wish to include custom objects that require a dedicated renderer besides `WebGL`, such as [CSS3DRenderer](https://threejs.org/docs/#examples/en/renderers/CSS3DRenderer), include in this array those extra renderer instances. | `[]` |

## Data input
| Method | Description | Default |
| --- | --- | :--: |
| jsonUrl([url]) | URL of JSON file to load graph data directly from, as an alternative to specifying graphData directly. | |
| nodeId([str]) | Node object accessor attribute for unique node id (used in link objects source/target). | `id` |
| linkSource([str]) | Link object accessor attribute referring to id of source node. | `source` |
| linkTarget([str]) | Link object accessor attribute referring to id of target node. | `target` |

## Container layout
| Method | Description | Default |
| --- | --- | :--: |
| width([px]) | Getter/setter for the canvas width. | *&lt;window width&gt;* |
| height([px]) | Getter/setter for the canvas height. | *&lt;window height&gt;* |
| backgroundColor([str]) | Getter/setter for the chart background color. | `#000011` |
| showNavInfo([boolean]) | Getter/setter for whether to show the navigation controls footer info. | `true` |

## Node styling
| Method | Description | Default |
| --- | --- | :--: |
| nodeRelSize([num]) | Getter/setter for the ratio of node sphere volume (cubic px) per value unit. | 4 |
| nodeVal([num, str or fn]) | Node object accessor function, attribute or a numeric constant for the node numeric value (affects sphere volume). | `val` |
| nodeLabel([str or fn]) | Node object accessor function or attribute for name (shown in label). Supports plain text, HTML string content or an [HTML element](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement). | `name` |
| nodeVisibility([boolean, str or fn]) | Node object accessor function, attribute or a boolean constant for whether to display the node. | `true` |
| nodeColor([str or fn]) | Node object accessor function or attribute for node color (affects sphere color). | `color` |
| nodeAutoColorBy([str or fn]) | Node object accessor function (`fn(node)`) or attribute (e.g. `'type'`) to automatically group colors by. Only affects nodes without a color attribute. | |
| nodeOpacity([num]) | Getter/setter for the nodes sphere opacity, between [0,1]. | 0.75   |
| nodeResolution([num]) | Getter/setter for the geometric resolution of each node, expressed in how many slice segments to divide the circumference. Higher values yield smoother spheres. | 8 |
| nodeThreeObject([Object3d, str or fn]) | Node object accessor function or attribute for generating a custom 3d object to render as graph nodes. Should return an instance of [ThreeJS Object3d](https://threejs.org/docs/index.html#api/core/Object3D). If a falsy value is returned, the default 3d object type will be used instead for that node.  | *default node object is a sphere, sized according to `val` and styled according to `color`.* |
| nodeThreeObjectExtend([bool, str or fn]) | Node object accessor function, attribute or a boolean value for whether to replace the default node when using a custom `nodeThreeObject` (`false`) or to extend it (`true`).  | `false` |

## Link styling
| Method | Description | Default |
| --- | --- | :--: |
| linkLabel([str or fn]) | Link object accessor function or attribute for name (shown in label). Supports plain text, HTML string content or an [HTML element](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement). | `name` |
| linkVisibility([boolean, str or fn]) | Link object accessor function, attribute or a boolean constant for whether to display the link line. A value of `false` maintains the link force without rendering it. | `true` |
| linkColor([str or fn]) | Link object accessor function or attribute for line color. | `color` |
| linkAutoColorBy([str or fn]) | Link object accessor function (`fn(link)`) or attribute (e.g. `'type'`) to automatically group colors by. Only affects links without a color attribute. | |
| linkOpacity([num]) | Getter/setter for line opacity of links, between [0,1]. | 0.2 |
| linkWidth([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the link line width. A value of zero will render a [ThreeJS Line](https://threejs.org/docs/#api/objects/Line) whose width is constant (`1px`) regardless of distance. Values are rounded to the nearest decimal for indexing purposes. | 0 |
| linkResolution([num]) | Getter/setter for the geometric resolution of each link, expressed in how many radial segments to divide the cylinder. Higher values yield smoother cylinders. Applicable only to links with positive width. | 6 |
| linkCurvature([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the curvature radius of the link line. Curved lines are represented as 3D bezier curves, and any numeric value is accepted. A value of `0` renders a straight line. `1` indicates a radius equal to half of the line length, causing the curve to approximate a semi-circle. For self-referencing links (`source` equal to `target`) the curve is represented as a loop around the node, with length proportional to the curvature value. Lines are curved clockwise for positive values, and counter-clockwise for negative values. Note that rendering curved lines is purely a visual effect and does not affect the behavior of the underlying forces. | 0 |
| linkCurveRotation([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the rotation along the line axis to apply to the curve. Has no effect on straight lines. At `0` rotation, the curve is oriented in the direction of the intersection with the `XY` plane. The rotation angle (in radians) will rotate the curved line clockwise around the "start-to-end" axis from this reference orientation. | 0 |
| linkMaterial([Material, str or fn]) | Link object accessor function or attribute for specifying a custom material to style the graph links with. Should return an instance of [ThreeJS Material](https://threejs.org/docs/#api/materials/Material). If a falsy value is returned, the default material will be used instead for that link. | *default link material is [MeshLambertMaterial](https://threejs.org/docs/#api/materials/MeshLambertMaterial) styled according to `color` and `opacity`.* |
| linkThreeObject([Object3d, str or fn]) | Link object accessor function or attribute for generating a custom 3d object to render as graph links. Should return an instance of [ThreeJS Object3d](https://threejs.org/docs/index.html#api/core/Object3D). If a falsy value is returned, the default 3d object type will be used instead for that link.  | *default link object is a line or cylinder, sized according to `width` and styled according to `material`.* |
| linkThreeObjectExtend([bool, str or fn]) | Link object accessor function, attribute or a boolean value for whether to replace the default link when using a custom `linkThreeObject` (`false`) or to extend it (`true`).  | `false` |
| linkDirectionalArrowLength([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the length of the arrow head indicating the link directionality. The arrow is displayed directly over the link line, and points in the direction of `source` > `target`. A value of `0` hides the arrow. | 0 |
| linkDirectionalArrowColor([str or fn]) | Link object accessor function or attribute for the color of the arrow head. | `color` |
| linkDirectionalArrowRelPos([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the longitudinal position of the arrow head along the link line, expressed as a ratio between `0` and `1`, where `0` indicates immediately next to the `source` node, `1` next to the `target` node, and `0.5` right in the middle. | 0.5 |
| linkDirectionalArrowResolution([num]) | Getter/setter for the geometric resolution of the arrow head, expressed in how many slice segments to divide the cone base circumference. Higher values yield smoother arrows. | 8 |
| linkDirectionalParticles([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the number of particles (small spheres) to display over the link line. The particles are distributed equi-spaced along the line, travel in the direction `source` > `target`, and can be used to indicate link directionality. | 0 |
| linkDirectionalParticleSpeed([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the directional particles speed, expressed as the ratio of the link length to travel per frame. Values above `0.5` are discouraged. | 0.01 |
| linkDirectionalParticleOffset([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the offset of the directional particles initial position, expressed as a value between 0 and 1, relative to a full position cycle. | 0 |
| linkDirectionalParticleWidth([num, str or fn]) | Link object accessor function, attribute or a numeric constant for the directional particles width. Values are rounded to the nearest decimal for indexing purposes. | 0.5 |
| linkDirectionalParticleColor([str or fn]) | Link object accessor function or attribute for the directional particles color. | `color` |
| linkDirectionalParticleResolution([num]) | Getter/setter for the geometric resolution of each directional particle, expressed in how many slice segments to divide the circumference. Higher values yield smoother particles. | 4 |
| linkDirectionalParticleThreeObject([Object3d, str or fn]) | Link object accessor function or attribute for a custom 3d object to use in the directional particles. Should return an instance of [ThreeJS Object3d](https://threejs.org/docs/index.html#api/core/Object3D). Activating this will ignore the set values for the particle's width, color and resolution. | |
| emitParticle(link) | An alternative mechanism for generating particles, this method emits a non-cyclical single particle within a specific link. The emitted particle shares the styling (speed, shape, color) of the regular particle props. A valid `link` object that is included in `graphData` should be passed as a single parameter. ||

## Render control
| Method | Description | Default |
| --- | --- | :--: |
| pauseAnimation() | Pauses the rendering cycle of the component, effectively freezing the current view and cancelling all user interaction. This method can be used to save performance in circumstances when a static image is sufficient. | |
| resumeAnimation() | Resumes the rendering cycle of the component, and re-enables the user interaction. This method can be used together with `pauseAnimation` for performance optimization purposes. | |
| zoomToFit([ms], [px], [nodeFilterFn]) | Automatically moves the camera so that all of the nodes become visible within its field of view, aiming at the graph center (0,0,0). If no nodes are found no action is taken. It accepts three optional arguments: the first defines the duration of the transition (in ms) to animate the camera motion (default: 0ms). The second argument is the amount of padding (in px) between the edge of the canvas and the outermost node location (default: 10px). The third argument specifies a custom node filter: `node => <boolean>`, which should return a truthy value if the node is to be included. This can be useful for focusing on a portion of the graph. | `(0, 10, node => true)` |
| postProcessingComposer() | Access the [post-processing composer](https://threejs.org/docs/#examples/en/postprocessing/EffectComposer). Use this to add post-processing [rendering effects](https://github.com/mrdoob/three.js/tree/dev/examples/jsm/postprocessing) to the scene. By default the composer has a single pass ([RenderPass](https://github.com/mrdoob/three.js/blob/dev/examples/jsm/postprocessing/RenderPass.js)) that directly renders the scene without any effects. ||
| lights([array]) | Getter/setter for the list of lights to use in the scene. Each item should be an instance of [Light](https://threejs.org/docs/#api/en/lights/Light). | [AmbientLight](https://threejs.org/docs/?q=ambient#api/en/lights/AmbientLight) + [DirectionalLight](https://threejs.org/docs/#api/en/lights/DirectionalLight) (from above) |
| scene() | Access the internal ThreeJS [Scene](https://threejs.org/docs/#api/scenes/Scene). Can be used to extend the current scene with additional objects not related to 3d-force-graph. | |
| camera() | Access the internal ThreeJS [Camera](https://threejs.org/docs/#api/cameras/PerspectiveCamera). | |
| renderer() | Access the internal ThreeJS [WebGL renderer](https://threejs.org/docs/#api/renderers/WebGLRenderer). ||
| controls() | Access the internal ThreeJS controls object. ||
| refresh() | Redraws all the nodes/links. |

## Force engine configuration
| Method | Description | Default |
| --- | --- | :--: |
| forceEngine([str]) | Getter/setter for which force-simulation engine to use ([*d3*](https://github.com/vasturiano/d3-force-3d) or [*ngraph*](https://github.com/anvaka/ngraph.forcelayout)). | `d3` |
| numDimensions([int]) | Getter/setter for number of dimensions to run the force simulation on (1, 2 or 3). | 3 |
| dagMode([str]) | Apply layout constraints based on the graph directionality. Only works correctly for [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) graph structures (without cycles). Choice between `td` (top-down), `bu` (bottom-up), `lr` (left-to-right), `rl` (right-to-left), `zout` (near-to-far), `zin` (far-to-near), `radialout` (outwards-radially) or `radialin` (inwards-radially). | |
| dagLevelDistance([num]) | If `dagMode` is engaged, this specifies the distance between the different graph depths. | *auto-derived from the number of nodes* |
| dagNodeFilter([fn]) | Node accessor function to specify nodes to ignore during the DAG layout processing. This accessor method receives a node object and should return a `boolean` value indicating whether the node is to be included. Excluded nodes will be left unconstrained and free to move in any direction. | `node => true` |
| onDagError([fn]) | Callback to invoke if a cycle is encountered while processing the data structure for a DAG layout. The loop segment of the graph is included for information, as an array of node ids. By default an exception will be thrown whenever a loop is encountered. You can override this method to handle this case externally and allow the graph to continue the DAG processing. Strict graph directionality is not guaranteed if a loop is encountered and the result is a best effort to establish a hierarchy. | *throws exception* |
| d3AlphaMin([num]) | Getter/setter for the [simulation alpha min](https://github.com/vasturiano/d3-force-3d#simulation_alphaMin) parameter, only applicable if using the d3 simulation engine. | `0` |
| d3AlphaDecay([num]) | Getter/setter for the [simulation intensity decay](https://github.com/vasturiano/d3-force-3d#simulation_alphaDecay) parameter, only applicable if using the d3 simulation engine. | `0.0228` |
| d3VelocityDecay([num]) | Getter/setter for the nodes' [velocity decay](https://github.com/vasturiano/d3-force-3d#simulation_velocityDecay) that simulates the medium resistance, only applicable if using the d3 simulation engine. | `0.4` |
| d3Force(str, [fn]) | Getter/setter for the internal forces that control the d3 simulation engine. Follows the same interface as `d3-force-3d`'s [simulation.force](https://github.com/vasturiano/d3-force-3d#simulation_force). Three forces are included by default: `'link'` (based on [forceLink](https://github.com/vasturiano/d3-force-3d#forceLink)), `'charge'` (based on [forceManyBody](https://github.com/vasturiano/d3-force-3d#forceManyBody)) and `'center'` (based on [forceCenter](https://github.com/vasturiano/d3-force-3d#forceCenter)). Each of these forces can be reconfigured, or new forces can be added to the system. This method is only applicable if using the d3 simulation engine. | |
| d3ReheatSimulation() | Reheats the force simulation engine, by setting the `alpha` value to `1`. Only applicable if using the d3 simulation engine. | |
| ngraphPhysics([object]) | Specify custom physics configuration for ngraph, according to its [configuration object](https://github.com/anvaka/ngraph.forcelayout#configuring-physics) syntax. This method is only applicable if using the ngraph simulation engine. | *ngraph default* |
| warmupTicks([int]) | Getter/setter for number of layout engine cycles to dry-run at ignition before starting to render. | 0 |
| cooldownTicks([int]) | Getter/setter for how many build-in frames to render before stopping and freezing the layout engine. | Infinity |
| cooldownTime([num]) | Getter/setter for how long (ms) to render for before stopping and freezing the layout engine. | 15000 |
| onEngineTick(fn) | Callback function invoked at every tick of the simulation engine. | - |
| onEngineStop(fn) | Callback function invoked when the simulation engine stops and the layout is frozen. | - |

## Interaction
| Method | Description | Default |
| --- | --- | :--: |
| onNodeClick(fn) | Callback function for node (left-button) clicks. The node object and the event object are included as arguments `onNodeClick(node, event)`. | - |
| onNodeRightClick(fn) | Callback function for node right-clicks. The node object and the event object are included as arguments `onNodeRightClick(node, event)`. | - |
| onNodeHover(fn) | Callback function for node mouse over events. The node object (or `null` if there's no node under the mouse line of sight) is included as the first argument, and the previous node object (or null) as second argument: `onNodeHover(node, prevNode)`. | - |
| onLinkClick(fn) | Callback function for link (left-button) clicks. The link object and the event object are included as arguments `onLinkClick(link, event)`. | - |
| onLinkRightClick(fn) | Callback function for link right-clicks. The link object and the event object are included as arguments `onLinkRightClick(link, event)`. | - |
| onLinkHover(fn) | Callback function for link mouse over events. The link object (or `null` if there's no link under the mouse line of sight) is included as the first argument, and the previous link object (or null) as second argument: `onLinkHover(link, prevLink)`. | - |
| onBackgroundClick(fn) | Callback function for click events on the empty space between the nodes and links. The event object is included as single argument `onBackgroundClick(event)`. | - |
| onBackgroundRightClick(fn) | Callback function for right-click events on the empty space between the nodes and links. The event object is included as single argument `onBackgroundRightClick(event)`. | - |
| linkHoverPrecision([int]) | Whether to display the link label when gazing the link closely (low value) or from far away (high value). | 1 |
| showPointerCursor(boolean or fn) | Whether to show a pointer cursor when hovering over clickable portions of the canvas. Accepts either a `boolean` constant or a callback function which receives the object currently under the cursor and is expected to return a `boolean` value. | `true` |
| enablePointerInteraction([boolean]) | Getter/setter for whether to enable the mouse tracking events. This activates an internal tracker of the canvas mouse position and enables the functionality of object hover/click and tooltip labels, at the cost of performance. If you're looking for maximum gain in your graph performance it's recommended to switch off this property. | `true` |
| enableNodeDrag([boolean]) | Getter/setter for whether to enable the user interaction to drag nodes by click-dragging. Only supported on the `d3` force engine. If enabled, every time a node is dragged the simulation is re-heated so the other nodes react to the changes. Only applicable if enablePointerInteraction is `true` and using the `d3` force engine. | `true` |
| enableNavigationControls([boolean]) | Getter/setter for whether to enable the trackball navigation controls used to move the camera using mouse interactions (rotate/zoom/pan). | `true` |

## Utility
| Method | Description |
| --- | --- |

## Input JSON syntax
```json
{
    "nodes": [
        {
          "id": "id1",
          "name": "name1",
          "val": 1
        },
        {
          "id": "id2",
          "name": "name2",
          "val": 10
        },
        ...
    ],
    "links": [
        {
            "source": "id1",
            "target": "id2"
        },
        ...
    ]
}
```
[npm-img]: https://img.shields.io/npm/v/3d-force-graph
[npm-url]: https://npmjs.org/package/3d-force-graph
[build-size-img]: https://img.shields.io/bundlephobia/minzip/3d-force-graph
[build-size-url]: https://bundlephobia.com/result?p=3d-force-graph
[npm-downloads-img]: https://img.shields.io/npm/dt/3d-force-graph
[npm-downloads-url]: https://www.npmtrends.com/3d-force-graph
![](https://github.com/vasturiano/3d-force-graph/blob/9376e16343721efd0416710c21db03ce8fa4dfb0/package.json#L57)

---

# iCloud: web-app/node_modules/3d-force-graph/node_modules/three-render-objects/README.md

> **Source:** icloud://web-app/node_modules/3d-force-graph/node_modules/three-render-objects/README.md
> **Analyzed At:** 2026-06-13T06:32:47.726Z

## Quick start
```js
import ThreeRenderObjects from 'three-render-objects';
```
or using a *script* tag
```html

```
then
```js
const myCanvas = new ThreeRenderObjects(<myDOMElement>)
  .objects(<myData>);
```

## Initialisation
```js
new ThreeRenderObjects(<domElement>, { configOptions })
```
| Config options | Description | Default |
| --- | --- | :--: |
| controlType: str | Which type of control to use to control the camera. Choice between [trackball](https://threejs.org/examples/misc_controls_trackball.html), [orbit](https://threejs.org/examples/#misc_controls_orbit) or [fly](https://threejs.org/examples/misc_controls_fly.html). | `trackball` |
| useWebGPU: boolean | Whether to use the `WebGPURenderer` instead of the default `WebGLRenderer`. | `false` |
| extraRenderers: array | If you wish to include objects that require a dedicated renderer besides `WebGL`, such as [CSS3DRenderer](https://threejs.org/docs/#examples/en/renderers/CSS3DRenderer), include in this array those extra renderer instances. | `[]` |
| waitForLoadComplete: boolean | Whether to wait until all the asynchronous loading operations are finished (such as the background image) before rendering the objects in the scene for the first time. | `true` |

## Data input
| Method | Description | Default |
| --- | --- | :--: |
| objects([array]) | Getter/setter for the list of objects to render. Each object should be an instance of [Object3D](https://threejs.org/docs/#api/core/Object3D). | `[]` |
| lights([array]) | Getter/setter for the list of lights to use in the scene. Each item should be an instance of [Light](https://threejs.org/docs/#api/en/lights/Light). | `[]` |

## Container layout
| Method | Description | Default |
| --- | --- | :--: |
| width([px]) | Getter/setter for the canvas width. | *&lt;window width&gt;* |
| height([px]) | Getter/setter for the canvas height. | *&lt;window height&gt;* |
| viewOffset([[number, number]]) | Getter/setter for the canvas center offset (`x`, `y`). | `[0, 0]` |
| skyRadius([number]) | Radius of the sphere that bounds the scene, in GL units. | 50000 |
| backgroundColor([str]) | Getter/setter for the canvas background color. | `#000011` |
| backgroundImageUrl([url]) | Getter/setter for the URL of the image to be used as scene background. If no image is provided, the background color is shown instead. | `null` |
| onBackgroundImageLoaded([fn]) | Callback function triggered when the background image has finished loading asynchronously and is rendered on the scene. ||
| showNavInfo([boolean]) | Getter/setter for whether to show the navigation controls footer info. | `true` |

## Render control
| Method | Description | Default |
| --- | --- | :--: |
| tick() | Re-render all the objects on the canvas. Essentially this method should be called at every frame, and can be used to control the animation ticks. ||
| zoomToFit([ms], [px], [objFilterFn]) | Automatically moves the camera so that all of the objects in the scene become visible within its field of view, while aiming at the scene center (0,0,0). If no objects are found no action is taken. It accepts three optional arguments: the first defines the duration of the transition (in ms) to animate the camera motion (default: 0ms). The second argument is the amount of padding (in px) between the edge of the canvas and the outermost object position (default: 10px). The third argument specifies a custom object filter: `obj => <boolean>`, which should return a truthy value if the object is to be included. This can be useful for focusing on a portion of the scene. | `(0, 10, obj => true)` |
| postProcessingComposer() | Access the [post-processing composer](https://threejs.org/docs/#examples/en/postprocessing/EffectComposer). Use this to add post-processing [rendering effects](https://github.com/mrdoob/three.js/tree/dev/examples/jsm/postprocessing) to the scene. By default the composer has a single pass ([RenderPass](https://github.com/mrdoob/three.js/blob/dev/examples/jsm/postprocessing/RenderPass.js)) that directly renders the scene without any effects. ||
| renderer() | Access the [WebGL renderer](https://threejs.org/docs/#api/renderers/WebGLRenderer) object. ||
| camera() | Access the [perspective camera](https://threejs.org/docs/#api/cameras/PerspectiveCamera) object. ||
| scene() | Access the [Scene](https://threejs.org/docs/#api/scenes/Scene) object. ||
| controls() | Access the camera controls object. ||

## Interaction
| Method | Description | Default |
| --- | --- | :--: |
| onClick(fn) | Callback function for object clicks with left mouse button. The object (or `null` if there's no object under the mouse line of sight), the event object and the intersection object are included as arguments `onClick(object, event, intersection)`. | - |
| onRightClick(fn) | Callback function for object right-clicks. The object (or `null` if there's no object under the mouse line of sight), the event object and the intersection object are included as arguments `onRightClick(object, event, intersection)`. | - |
| onHover(fn) | Callback function for object mouse over events. The object (or `null` if there's no object under the mouse line of sight), the previous hovered object (or `null`) and the intersection object are included as arguments: `onHover(obj, prevObj, intersection)`. | - |
| hoverOrderComparator([fn]) | Getter/setter for the comparator function to use when hovering over multiple objects under the same line of sight. This function can be used to prioritize hovering some objects over others. | By default, hovering priority is based solely on camera proximity (closest object wins). |
| hoverFilter([fn]) | Getter/setter for the filter function that defines whether an object is eligible for hovering and other interactions. This function receives an object as sole argument and should return a `boolean` value | `() => true` |
| lineHoverPrecision([int]) | Getter/setter for the precision to use when detecting hover events over [Line](https://threejs.org/docs/#api/objects/Line) objects. | 1 |
| pointsHoverPrecision([int]) | Getter/setter for the precision to use when detecting hover events over [Points](https://threejs.org/docs/#api/objects/Points) objects. | 1 |
| tooltipContent([str or fn]) | Object accessor function or attribute for label (shown in tooltip). Supports plain text, HTML string content, an [HTML element](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) or [React JSX](https://react.dev/learn/writing-markup-with-jsx). ||
| enablePointerInteraction([boolean]) | Getter/setter for whether to enable the mouse tracking events. This activates an internal tracker of the canvas mouse position and enables the functionality of object hover/click and tooltip labels, at the cost of performance. If you're looking for maximum gain in your render performance it's recommended to switch off this property. | `true` |
| pointerRaycasterThrottleMs([int]) | Getter/setter for the minimum amount of time (in ms) to wait between raycaster checks for the pointer tracker. Increasing this value will improve render performance at the cost of potential lag in pointer interactions. | `50` |
| hoverDuringDrag([boolean]) | Getter/setter for whether to trigger hover events while using the controls via pointer dragging.| `false` |
| clickAfterDrag([boolean]) | Getter/setter for whether to trigger a click event after dragging using the controls.| `false` |

## Utility
| Method | Description |
| --- | --- |
| intersectingObjects(x, y) | Utility method to retrieve the list of objects under the line of sight of the given viewport coordinates. Returns an array of [intersectObject](https://threejs.org/docs/#api/en/core/Raycaster.intersectObject), sorted by distance (from closest to farthest). |
[npm-img]: https://img.shields.io/npm/v/three-render-objects
[npm-url]: https://npmjs.org/package/three-render-objects
[build-size-img]: https://img.shields.io/bundlephobia/minzip/three-render-objects
[build-size-url]: https://bundlephobia.com/result?p=three-render-objects
[npm-downloads-img]: https://img.shields.io/npm/dt/three-render-objects
[npm-downloads-url]: https://www.npmtrends.com/three-render-objects

---

# iCloud: web-app/node_modules/3d-force-graph/node_modules/polished/LICENSE.md

> **Source:** icloud://web-app/node_modules/3d-force-graph/node_modules/polished/LICENSE.md
> **Analyzed At:** 2026-06-13T06:32:47.734Z

## MIT License
Copyright (c) 2016-Present Brian Hough and Maximilian Stoiber
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# iCloud: web-app/node_modules/3d-force-graph/node_modules/polished/README.md

> **Source:** icloud://web-app/node_modules/3d-force-graph/node_modules/polished/README.md
> **Analyzed At:** 2026-06-13T06:32:47.741Z

## Docs
**See the full documentation at [polished.js.org](http://polished.js.org/docs)!**

## Usage
`✨ polished` modules are meant to be used as stand-alone imports. You should avoid importing the entire library directly:
`import { clearFix, animation } from 'polished'`
~`import * as polished from 'polished`~
~`import polished from 'polished'`~
When `✨ polished` modules are imported properly, tree shaking in [webpack](https://webpack.js.org/guides/tree-shaking/) and [Rollup](https://github.com/rollup/rollup#tree-shaking) can be leveraged to reduce your bundle size.

## Browser Support
All Evergreen Browsers + IE11
As of v3.6.X we support `>0.5%, not dead, ie >= 11, not op_mini all` for all our builds.

## Flow Type Definitions
`✨ polished` has first-class [Flow](https://flow.org/) support with zero configuration to assist you in finding type errors while using our modules.

## Ignore ✨ polished source
Flow frequently updates and it is possible that the version you are running may cause you to run into errors coming from the `polished` package in your `node_modules` directory. You can add the following lines to your `.flowconfig` to ignore `polished` in those cases:
```bash
[ignore]
.*/node_modules/polished/.*
```

## TypeScript Definitions
`✨ polished` has [TypeScript](https://www.typescriptlang.org/) definitions to allow the library to be used in any TypeScript project. You will need to set `moduleResolution` to `node` in your `tsconfig.json` in order to use `✨ polished` with TypeScript.

## Babel plugin
You can optionally also use [`babel-plugin-polished`](https://github.com/styled-components/babel-plugin-polished) to compile the static function calls out and remove the (already tiny) runtime performance impact of using `✨ polished`.

## Why?
When writing styles in JavaScript, many people need Sass-style helper functions to be productive. `✨ polished` brings them to you in a nice, lightweight package tailor-made for styles in JavaScript.
The main difference with Sass is that it's written in a functional style and all color functions are curried. This means you can compose them together into your own reusable helpers with a `compose` function of your choice:
```JS
import { compose } from 'ramda' // Replace with any compose() function of your choice
import { lighten, desaturate } from 'polished'

// Create tone() helper
const tone = compose(lighten(0.1), desaturate(0.1))
```

## Why not `package-xyz`?
First of all, we didn't find another library that had everything we needed, and we don't care about installing a dozen packages separately.
Specifically most other packages that provide color functions do so in an object-oriented style, often with a fluent API that's very different from the Sass-style helpers. This means people that aren't very familiar with JavaScript might shy away from using them.
`✨ polished` was made as a standard library for everybody, no matter if they know JS inside out or not.

## Compatibility
✨ polished is **compatible with any library that accepts styles as JS objects**. This includes, but is by far not limited to, `styled-components`, radium, aphrodite, glamor, glamorous, jss and many more!
No matter if you're using [inline styles or CSS-in-JS](http://mxstbr.blog/2016/11/inline-styles-vs-css-in-js/), polished is for you.

## Contributors
This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].

## Backers
Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/polished#backer)]

## Sponsors
Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/polished#sponsor)]

## License
Copyright © 2016-2021 Brian Hough, Maximilian Stoiber, & Nik Graf. Licensed under the MIT License, see [LICENSE.md](LICENSE.md) for more information!

