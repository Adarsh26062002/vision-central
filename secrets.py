# Must be EXCLUDED by the ROOT repo's .blitzyignore ("secrets.py"), even though this
# file lives inside a submodule. Root patterns are unanchored, so they still apply
# everywhere -- this is unchanged, pre-existing behavior (not part of the ABK-4487 fix).
API_KEY = "should-never-be-onboarded"
