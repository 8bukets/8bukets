Quickstart for GitHub Pages
You can use GitHub Pages to showcase some open source projects, host a blog, or even share your résumé. This guide will help get you started on creating your next website.
Who can use this feature?
GitHub Pages is available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see GitHub's plans.

In this article
Introduction

In this guide, you'll create a user site at <username>.github.io.

Creating your website

In the upper-right corner of any page, select , then click New repository.

Screenshot of a GitHub dropdown menu showing options to create new items. The menu item "New repository" is outlined in dark orange.
Enter username.github.io as the repository name. Replace username with your GitHub username. For example, if your username is octocat, the repository name should be octocat.github.io.

Screenshot of GitHub Pages settings in a repository. The repository name field contains the text "octocat.github.io" and is outlined in dark orange.
Choose a repository visibility. For more information, see About repositories.

Toggle Add README to On.

Click Create repository.

Under your repository name, click  Settings. If you cannot see the "Settings" tab, select the dropdown menu, then click Settings.

Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.
In the "Code and automation" section of the sidebar, click  Pages.

Under "Build and deployment", under "Source", select Deploy from a branch.

Under "Build and deployment", under "Branch", use the branch dropdown menu and select a publishing source.

Screenshot of Pages settings in a GitHub repository. A menu to select a branch for a publishing source, labeled "None," is outlined in dark orange.
Optionally, open the README.md file of your repository. The README.md file is where you will write the content for your site. You can edit the file or keep the default content for now.

Visit username.github.io to view your new website. Note that it can take up to 10 minutes for changes to your site to publish after you push the changes to GitHub.

Changing the title and description

By default, the title of your site is username.github.io. You can change the title by editing the _config.yml file in your repository. You can also add a description for your site.

Click the Code tab of your repository.

In the file list, click _config.yml to open the file.

Click  to edit the file.

The _config.yml file already contains a line that specifies the theme for your site. Add a new line with title: followed by the title you want. Add a new line with description: followed by the description you want. For example:

theme: jekyll-theme-minimal
title: Octocat's homepage
description: Bookmark this to keep an eye on my project updates!
When you are finished editing the file, click Commit changes.

Next Steps

You've successfully created, personalized, and published your first GitHub Pages website but there's so much more to explore! Here are some helpful resources for taking your next steps with GitHub Pages:

Adding content to your GitHub Pages site using Jekyll: This guide explains how to add additional pages to your site.
Configuring a custom domain for your GitHub Pages site: You can host your site on GitHub's github.io domain or your own custom domain
