# Ren'Py 7.8.7 Windows / Python 2.7 modules

The `Build Windows modules (Python 2.7)` workflow builds both Windows targets:

| Artifact | Target |
| --- | --- |
| `renpy-7.8.7-windows-x86_64-python2.7` | Windows 64-bit |
| `renpy-7.8.7-windows-i686-python2.7` | Windows 32-bit |

Download the artifacts from the GitHub Actions run. Extract the required
artifact into an existing Ren'Py 7.8.7 SDK directory, preserving its directory
structure and replacing the corresponding files. Both architectures can be
extracted into the same SDK. Keep a backup of the original SDK before replacing
files. The 64-bit launcher is `renpy.exe`; the 32-bit launcher is `renpy-32.exe`.

These are compiled modules and their Python runtime, not a standalone SDK.
The artifact includes `lib/py2-windows-<arch>/`, `lib/python2.7/`, a launcher,
and `SOURCE_COMMIT.txt`. Ren'Py and pygame_sdl2 native modules (including the
FFmpeg media reader) are linked into `librenpython.dll`, rather than separate
`.pyd` files. Use the artifacts with the matching 7.8.7 Python sources.

The official historical `renpy-build` tools cross-compile CPython 2.7.18 and
the Windows native dependencies on Ubuntu. Python 3.11 runs the build
orchestrator only; the generated modules and runtime target Python 2.7.18.
Build-tool and pygame_sdl2 revisions are pinned in the workflow. The Ren'Py
source revision comes from the triggering commit, including its local fixes.
The checkout is assigned the local branch name `fix` during CI because the
historical version resolver only defines the Python 2 release on that branch.
This preserves the triggering commit and does not change any remote branch.
The build also checks that the source package resolves to Ren'Py 7.8.7.

A subsequent Windows job executes each compiled interpreter and checks its
Python version, pointer size, and registration of the native media module.
This smoke check does not measure WebM playback memory usage.

Optional proprietary integrations such as Live2D require their separately
licensed SDKs and are not included by this workflow.
