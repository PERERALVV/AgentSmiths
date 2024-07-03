JAVASCRIPT_REACT = {
    "path": "javascript_react",
    "description": "React web app using Vite devserver/bundler",
    "summary": "\n".join([
        "* Initial setup with Vite for fast development",
        "* Basic project structure for React development",
        "* Development server setup for hot reloading",
        "* Minimal configuration to get started with React",
    ]),
    "install_hook": "npm install",
    "files": [
    {
        'summary': 'This file configures ESLint for the project. It sets up the environment, extends recommended rules from ESLint, React, and React Hooks, ignores certain files and directories, specifies parser options, sets React version for the project, and configures plugins and rules. The file uses the CommonJS module format.',
        'references': ['react/recommended.js', 'react/jsx-runtime.js', 'react-hooks/recommended.js', 'react-refresh.js'],
        'path': '.eslintrc.cjs'
    },
    {
        'summary': 'This file defines which files and directories should be ignored by Git. It includes patterns for common files and directories that are often not needed in version control, such as logs, build artifacts, and editor-specific files.',
        'references': [],
        'path': '.gitignore'
    },
    {
        'summary': "This file is the entry point for the web application. It defines the basic HTML structure of the application, including the title, viewport settings, and a reference to the main JavaScript file (`src/main.jsx`) that will handle the application's logic and rendering.",
        'references': ['src/main.jsx'],
        'path': 'index.html'
    },
    {
        'summary': "This file is a `package.json` file for a React project using Vite as a build tool. It defines the project's name, version, dependencies, and scripts for development, building, linting, and previewing the application. The `type` field is set to `module` to enable ES modules support. The `scripts` section defines commands for running the development server (`dev`), building the application for production (`build`), linting the code (`lint`), and starting a preview server (`preview`). The `dependencies` section lists the project's dependencies, including React and React DOM. The `devDependencies` section lists the development dependencies, including TypeScript type definitions for React and React DOM, the Vite plugin for React, ESLint, and its plugins for React, React hooks, and React refresh.",
        'references': [],
        'path': 'package.json'
    },
    {
        'summary': 'This file configures the Vite build tool for a React project. It uses the `@vitejs/plugin-react` plugin to enable React support in the build process.',
        'references': ['vite.config.js', 'react.js'],
        'path': 'vite.config.js'
    },
    {
        'summary': 'This file is an empty file used to ensure that the `public` directory is included in the Git repository. It is a common practice to use `.gitkeep` files in empty directories to prevent them from being ignored by Git.',
        'references': [],
        'path': 'public/.gitkeep'
    },
    {
        'summary': 'This file defines CSS styles for the root element of the application. It sets the maximum width, margin, padding, and text alignment for the root element.',
        'references': [],
        'path': 'src/App.css'
    },
    {
        'summary': 'The file defines a React component named `App` which renders a heading element displaying the value of the `project_name` variable. This component is the root component of the application and is exported as the default export.',
        'references': ['App.css'],
        'path': 'src/App.jsx'
    },
    {
        'summary': 'This CSS file defines styles for the root element and the body element. It sets font rendering options for the root element, and sets the margin, display, place-items, min-width, and min-height properties for the body element. It also defines a style for the h1 element, setting its font size and line height.',
        'references': [],
        'path': 'src/index.css'
    },
    {
        'summary': 'This file is the entry point for the React application. It renders the `App` component within a `React.StrictMode` context, which helps identify potential issues in the application. It also imports the `index.css` file for styling.',
        'references': ['react.js', 'react-dom.js', 'App.jsx', 'index.css'],
        'path': 'src/main.jsx'
    },
    {
        'summary': 'This file is an empty file used to tell Git to track this directory. It is commonly used to ensure that empty directories are included in version control.',
        'references': [],
        'path': 'src/assets/.gitkeep'
    }
]
}


{
        "vite.config.js": "Configuration file for Vite, a fast developer-friendly Javascript bundler/devserver.",
        "index.html": "Main entry point for the project. It includes a basic HTML structure with a root div element and a script tag importing a JavaScript file named main.jsx using the module type. References: src/main.jsx",
        ".eslintrc.cjs": "Configuration file for ESLint, a static code analysis tool for identifying problematic patterns found in JavaScript code. It defines rules for linting JavaScript code with a focus on React applications.",
        ".gitignore": "Specifies patterns to exclude files and directories from being tracked by Git version control system. It is used to prevent certain files from being committed to the repository.",
        "package.json": "Standard Nodejs package metadata file, specifies dependencies and start scripts. It also specifies that the project is a module.",
        "public/.gitkeep": "Empty file",
        "src/App.css": "Contains styling rules for the root element of the application, setting a maximum width, centering it on the page, adding padding, and aligning text to the center.",
        "src/index.css": "Defines styling rules for the root element, body, and h1 elements of a web page.",
        "src/App.jsx": "Defines a functional component that serves as the root component in the project. The component is exported as the default export. References: src/App.css",
        "src/main.jsx": "Main entry point for a React application. It imports necessary modules, renders the main component 'App' inside a 'React.StrictMode' component, and mounts it to the root element in the HTML document. References: App.jsx, index.css",
        "src/assets/.gitkeep": "Empty file",
}