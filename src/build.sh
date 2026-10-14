#!/usr/bin/env bash
# Rebuild both level apps and refresh the site folder.
set -e
cd "$(dirname "$0")"

# ---- question banks (every answer is checked here; the build stops on an error) ----
python3 dump.py maths   part1,part2,part3,ext_maths,ext2_maths
python3 dump.py english eng1,eng2,eng3,ext_eng,ext2_eng
python3 dump.py science sci1,sci2,sci3,ext_sci,ext2_sci
python3 dump.py social  sst1,sst2,sst3,ext_sst,ext2_sst

python3 dump_bece.py bmaths     bmat1,bmat2
python3 dump_bece.py benglish   beng1,beng2
python3 dump_bece.py bscience   bsci1,bsci2,bsci3
python3 dump_bece.py bsocial    bsst1,bsst2,bsst3
python3 dump_bece.py brme       brme1,brme2
python3 dump_bece.py bcomputing bcomp1,bcomp2

# ---- theme the shell, build both apps, then the site ----
python3 hudify.py
python3 build_two.py
python3 make_site.py
echo "Done. Commit and push, or drag the site folder to Netlify."
