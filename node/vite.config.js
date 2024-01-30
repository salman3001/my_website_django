import { defineConfig } from 'vite';
import copy from 'rollup-plugin-copy';

export default defineConfig({
    build: {
        outDir: 'static',
        assetsDir: 'node',
    },
    plugins: [
        copy({
            targets: [
                { src: 'static/index.html', dest: 'templates/node' },
                // You can add more copy targets if needed
            ],
            hook: 'writeBundle',
        }),
    ],
});