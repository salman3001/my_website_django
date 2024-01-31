/** @type {import('vite').UserConfig} */
import { defineConfig } from 'vite';
import copy from 'rollup-plugin-copy';
import fs from 'fs/promises';


export default defineConfig({
    root:'.',
    build: {
        outDir: 'core/static/core',
    },  
});