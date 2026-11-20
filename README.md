# Team Project – Online Shopping Modules
Modules: Login, Catalog
A small Python demonstration project organized using GitHub's feature-branch workflow.

## Project modules

| Member | Module | File | Branch |
|---|---|---|---|
| Student 1 | Login / authentication | `login.py` | `feature-login` |
| Student 2 | Product catalogue | `catalog.py` | `feature-catalog` |
| Student 3 | Shopping cart | `cart.py` | `feature-cart` |

> Replace Student 1, Student 2 and Student 3 with the actual team members' names.

## Requirements

- Python 3
- Git
- A GitHub repository
- Visual Studio Code (recommended)

## Run the modules

Open a terminal in the project folder and run:

```bash
python login.py
python catalog.py
python cart.py
```

## Branch strategy

- `main` contains the integrated project.
- Each module is developed on its own feature branch.
- Contributors push their branch and open a pull request (PR) into `main`.
- Another team member reviews the changes. Merge only after approval.
- Delete the feature branch after merging, if appropriate.

## Team workflow

1. Clone the repository: `git clone <repository-url>`
2. Enter the folder: `cd team-project`
3. Get the latest main branch: `git switch main` and `git pull origin main`
4. Create a module branch: `git switch -c feature-<module>`
5. Make and test the changes.
6. Stage and commit: `git add .` and `git commit -m "Add <module> module"`
7. Push the branch: `git push -u origin feature-<module>`
8. On GitHub, open a pull request with base `main` and compare the feature branch.
9. Request a review. The reviewer checks **Files changed**, leaves comments if needed, and approves.
10. After approval, merge the pull request into `main`.

## Demonstrating a merge conflict

For the lab demonstration, two branches can edit the same `Modules:` line in this README. Merge the first branch, then update the second branch with the latest `main`. Git will report a conflict if both branches changed that same line differently.

Resolve it by editing the file so it contains all modules, for example:

`Modules: Login, Catalog, Cart`

Remove Git's conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), then run:

```bash
git add README.md
git commit -m "Resolve README merge conflict"
git push
```

Return to the pull request on GitHub, confirm that the conflict is cleared, and merge it after review.

## Contribution guidelines

- Use a separate branch for each module or change.
- Write clear commit messages.
- Test changes before opening a pull request.
- Do not commit passwords, access keys, tokens, or `.env` files.
- Ask a teammate to review pull requests before merging.
