export default {
  async fetch(request, env, ctx) {
    return new Response('Hello World from sor8bukets worker!', {
      headers: { 'content-type': 'text/plain' },
    });
  },
};
