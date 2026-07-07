# Must be EXCLUDED by vision-central's OWN .blitzyignore (build/**).
# This is the core ABK-4487 fix under test: a submodule's own .blitzyignore was
# previously never read at all.
def output():
    return "vision-central/build: should be excluded"
