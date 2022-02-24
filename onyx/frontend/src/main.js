import VueLogger from "vuejs3-logger";
import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";

const options = {
  isEnabled: true,
  logLevel: "debug",
  stringifyArguments: false,
  showLogLevel: true,
  showMethodName: true,
  separator: "|",
  showConsoleColors: true,
};

createApp(App).use(VueLogger, options).mount("body");
