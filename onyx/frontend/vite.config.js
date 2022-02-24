import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import Dotenv from "dotenv-webpack";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  configureWebpack: {
    module: {
      plugins: [new Dotenv()],
      rules: [
        {
          test: /config.*config\.js$/,
          use: [
            {
              loader: "file-loader",
              options: {
                name: "app.config.js",
              },
            },
          ],
        },
      ],
    },
  },
});
