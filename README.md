# hello-world
Get started with deploying Python web apps with this simple app

This guide illustrates how you can deploy this hello-world app to Phemeral.
More docs can be found at: https://phemeral.dev/docs

1\. Create an Account

Sign up at [phemeral.dev](https://phemeral.dev/pricing). When your account is created, Phemeral automatically provisions an organization with a default project called **Launchpad** and three default environments: **Production**, **Staging**, and **Development**.

2\. Connect Your GitHub Account

1. Navigate to **User Settings**.
2. Click **Connect** in the GitHub section.
3. Authorize the Phemeral GitHub App on your GitHub account and grant it access to the repositories you want to deploy.

3\. Connect a Repository to Your Project
1. Open your project and go to the **Settings** tab.
2. Select the repository you want to deploy from the list of accessible repositories.
3. Map a branch (e.g. `main`) to an environment (e.g. **Production**).

4\. Deploy

Push a commit to your mapped branch. Phemeral automatically:

* Detects your Python framework, package manager, and project structure
* Builds and deploys your application
* Assigns a live URL on `.phemeral.app`

View the build status and logs from the deployment page in your dashboard.

