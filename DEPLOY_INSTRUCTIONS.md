# How to Deploy to GitHub Pages

I have converted your Dynamic Flask application into a Static Website (HTML + JavaScript) so it can be hosted on GitHub Pages.

## Steps to Deploy

1.  **Commit the changes**
    I have created `index.html` (the static version) and `.nojekyll`. You need to commit these to your repository.
    
    ```bash
    git add index.html .nojekyll
    git commit -m "Convert to static site for GitHub Pages"
    git push origin main
    ```

2.  **Enable GitHub Pages**
    - Go to your repository on GitHub: [https://github.com/Arjumaan/scientific-calculator](https://github.com/Arjumaan/scientific-calculator)
    - Click on **Settings** (tab at the top).
    - On the left sidebar, click on **Pages**.
    - Under **Build and deployment** > **Source**, select **Deploy from a branch**.
    - Under **Branch**, select `main` (or `master`) and folder `/ (root)`.
    - Click **Save**.

3.  **Wait for Deployment**
    - GitHub will take a minute or two to build your site.
    - Refresh the Pages settings page to see the URL of your live site (usually `https://arjumaan.github.io/scientific-calculator/`).

## Note on Changes
- The original `app.py` (Python backend) is no longer used for the live site. The logic has been rewritten in JavaScript inside `index.html`.
- History is now saved in the browser's **Local Storage** instead of a file, so each user has their own private history.
