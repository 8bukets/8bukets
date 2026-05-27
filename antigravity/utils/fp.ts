/**
 * Functional Programming Utilities
 * Provides generic, reusable tools for declarative data pipelines.
 */

// A generic function type
type Func<A, B> = (arg: A) => B;

/**
 * Synchronous Pipe
 * Composes functions from left to right.
 */
export function pipe<A, B>(value: A, fn1: Func<A, B>): B;
export function pipe<A, B, C>(value: A, fn1: Func<A, B>, fn2: Func<B, C>): C;
export function pipe<A, B, C, D>(value: A, fn1: Func<A, B>, fn2: Func<B, C>, fn3: Func<C, D>): D;
export function pipe<A, B, C, D, E>(value: A, fn1: Func<A, B>, fn2: Func<B, C>, fn3: Func<C, D>, fn4: Func<D, E>): E;
export function pipe(value: any, ...fns: Function[]): any {
  return fns.reduce((acc, fn) => fn(acc), value);
}

/**
 * Asynchronous Pipe
 * Composes asynchronous or synchronous functions from left to right.
 */
export async function asyncPipe<A, B>(value: A | Promise<A>, fn1: Func<A, B | Promise<B>>): Promise<B>;
export async function asyncPipe<A, B, C>(value: A | Promise<A>, fn1: Func<A, B | Promise<B>>, fn2: Func<B, C | Promise<C>>): Promise<C>;
export async function asyncPipe<A, B, C, D>(value: A | Promise<A>, fn1: Func<A, B | Promise<B>>, fn2: Func<B, C | Promise<C>>, fn3: Func<C, D | Promise<D>>): Promise<D>;
export async function asyncPipe<A, B, C, D, E>(value: A | Promise<A>, fn1: Func<A, B | Promise<B>>, fn2: Func<B, C | Promise<C>>, fn3: Func<C, D | Promise<D>>, fn4: Func<D, E | Promise<E>>): Promise<E>;
export async function asyncPipe(value: any, ...fns: Function[]): Promise<any> {
  return fns.reduce(async (accPromise, fn) => {
    const acc = await accPromise;
    return fn(acc);
  }, Promise.resolve(value));
}

/**
 * Curried map
 */
export const map = <A, B>(fn: (item: A) => B) => (arr: A[]): B[] => arr.map(fn);

/**
 * Curried filter
 */
export const filter = <A>(fn: (item: A) => boolean) => (arr: A[]): A[] => arr.filter(fn);

/**
 * Curried reduce
 */
export const reduce = <A, B>(fn: (acc: B, item: A) => B, initial: B) => (arr: A[]): B => arr.reduce(fn, initial);
