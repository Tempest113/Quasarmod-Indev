#!/usr/bin/env python3
"""
patch_zz_giga_gui.py
─────────────────────
Applies the hardcoded differences from zz_giga_gui_main_menu.gui onto a
(possibly updated) z_giga_gui_main_menu.gui, writing the result to
zz_giga_gui_main_menu.gui.

Usage:
    python patch_zz_giga_gui.py [SOURCE] [OUTPUT]

Defaults:
    SOURCE  = z_giga_gui_main_menu.gui
    OUTPUT  = zz_giga_gui_main_menu.gui

Changes encoded in this script
───────────────────────────────
1. Indentation: leading tabs → 4-space indentation, trailing whitespace stripped.

2. Insert four new containerWindowType blocks (smbh_manipulator, core_mbrain,
   teraforge, quasarshipyard) after the closing "}" of the
   "supermassive_ehof" button container, immediately before the
   "### Right ###" section separator.

3. Insert the "quasarcraft_options" containerWindowType block after the
   closing "}" of the "o_systemcraft_options" container.
"""

import re
import sys
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def expand_leading_whitespace(line: str, tab_width: int = 4) -> str:
    stripped = line.lstrip('\t')
    n_tabs = len(line) - len(stripped)
    return (' ' * (n_tabs * tab_width) + stripped).rstrip()


def convert_leading_tabs(text: str) -> str:
    out = []
    for part in re.split(r'(\r\n|\r|\n)', text):
        if re.fullmatch(r'\r\n|\r|\n', part):
            out.append(part)
        else:
            out.append(expand_leading_whitespace(part))
    return ''.join(out)


def safe_replace(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 0:
        print(f"  WARNING: anchor not found for change '{label}' – skipping.")
        return text
    if count > 1:
        print(f"  WARNING: anchor for '{label}' found {count} times – "
              "replacing first occurrence only.")
        return text.replace(old, new, 1)
    return text.replace(old, new)


# ─────────────────────────────────────────────────────────────────────────────
# All hardcoded changes
# ─────────────────────────────────────────────────────────────────────────────

def apply_changes(text: str) -> str:
    NL = '\r\n'

    # ── Change 2 ─────────────────────────────────────────────────────────────
    # Insert smbh_manipulator, core_mbrain, teraforge, quasarshipyard blocks
    # after the closing "}" of the supermassive_ehof container, before the
    # "### Right ###" separator.

    new_left_blocks = (
            NL
            + '                ###################################' + NL
            + '                ### smbh manipulator ##############' + NL
            + '                ###################################' + NL
            + '                containerWindowType = {' + NL
            + '                    name = "smbh_manipulator_options"' + NL
            + '                    position = { x = 20 y = 65 }' + NL
            + '                    size = { width = 410 height = 34 }' + NL
            + '                    orientation = upper_left' + NL
            + NL
            + '                    effectButtonType = {' + NL
            + '                        name = "background_smbh_manipulator"' + NL
            + '                        spriteType = "GFX_giga_menu_button_bg"' + NL
            + '                        position = { x = 0 y = 0 }' + NL
            + '                        format = left' + NL
            + '                        no_clicksound = yes' + NL
            + '                        borderSize = { x = 10 y = 0 }' + NL
            + '                        font = "cg_16b"' + NL
            + '                        text = "giga_menu_name_smbh_manipulator"' + NL
            + '                        effect = "quasarmod_smbh_manipulator_tt"' + NL
            + '                    }' + NL
            + NL
            + '                    effectButtonType = { name = "smbh_manipulator_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "quasarmod_manipulator_disabled" }' + NL
            + '                    effectButtonType = { name = "smbh_manipulator_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } clicksound = interface effect = "quasarmod_manipulator_enabled" }' + NL
            + '                }' + NL
            + NL
            + '                ##############################' + NL
            + '                ### core mbrain ##############' + NL
            + '                ##############################' + NL
            + '                containerWindowType = {' + NL
            + '                    name = "core_mbrain_options"' + NL
            + '                    position = { x = 20 y = 105 }' + NL
            + '                    size = { width = 410 height = 34 }' + NL
            + '                    orientation = upper_left' + NL
            + NL
            + '                    effectButtonType = {' + NL
            + '                        name = "background_core_mbrain"' + NL
            + '                        spriteType = "GFX_giga_menu_button_bg"' + NL
            + '                        position = { x = 0 y = 0 }' + NL
            + '                        format = left' + NL
            + '                        no_clicksound = yes' + NL
            + '                        borderSize = { x = 10 y = 0 }' + NL
            + '                        font = "cg_16b"' + NL
            + '                        text = "giga_menu_name_core_mbrain"' + NL
            + '                        effect = "quasarmod_core_mbrain_tt"' + NL
            + '                    }' + NL
            + NL
            + '                    effectButtonType = { name = "core_mbrain_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "quasarmod_mbrain_disabled" }' + NL
            + '                    effectButtonType = { name = "core_mbrain_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } clicksound = interface effect = "quasarmod_mbrain_enabled" }' + NL
            + '                }' + NL
            + NL
            + '                ############################' + NL
            + '                ### teraforge ##############' + NL
            + '                ############################' + NL
            + '                containerWindowType = {' + NL
            + '                    name = "teraforge_options"' + NL
            + '                    position = { x = 20 y = 145 }' + NL
            + '                    size = { width = 410 height = 34 }' + NL
            + '                    orientation = upper_left' + NL
            + NL
            + '                    effectButtonType = {' + NL
            + '                        name = "background_teraforge"' + NL
            + '                        spriteType = "GFX_giga_menu_button_bg"' + NL
            + '                        position = { x = 0 y = 0 }' + NL
            + '                        format = left' + NL
            + '                        no_clicksound = yes' + NL
            + '                        borderSize = { x = 10 y = 0 }' + NL
            + '                        font = "cg_16b"' + NL
            + '                        text = "giga_menu_name_teraforge"' + NL
            + '                        effect = "quasarmod_teraforge_tt"' + NL
            + '                    }' + NL
            + NL
            + '                    effectButtonType = { name = "teraforge_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "quasarmod_teraforge_disabled" }' + NL
            + '                    effectButtonType = { name = "teraforge_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } clicksound = interface effect = "quasarmod_teraforge_enabled" }' + NL
            + '                }' + NL
            + NL
            + '                #################################' + NL
            + '                ### quasarshipyard ##############' + NL
            + '                #################################' + NL
            + '                containerWindowType = {' + NL
            + '                    name = "quasarshipyard_options"' + NL
            + '                    position = { x = 20 y = 185 }' + NL
            + '                    size = { width = 410 height = 34 }' + NL
            + '                    orientation = upper_left' + NL
            + NL
            + '                    effectButtonType = {' + NL
            + '                        name = "background_quasarshipyard"' + NL
            + '                        spriteType = "GFX_giga_menu_button_bg"' + NL
            + '                        position = { x = 0 y = 0 }' + NL
            + '                        format = left' + NL
            + '                        no_clicksound = yes' + NL
            + '                        borderSize = { x = 10 y = 0 }' + NL
            + '                        font = "cg_16b"' + NL
            + '                        text = "giga_menu_name_hyperquasaric_megashipyard"' + NL
            + '                        effect = "quasarmod_hyperquasaric_megashipyard_tt"' + NL
            + '                    }' + NL
            + NL
            + '                    effectButtonType = { name = "quasarshipyard_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "quasarmod_shipyard_disabled" }' + NL
            + '                    effectButtonType = { name = "quasarshipyard_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } clicksound = interface effect = "quasarmod_shipyard_enabled" }' + NL
            + '                }' + NL
            + NL
    )

    # Anchor: unique closing line of supermassive_ehof container + the long
    # "### Right ###" separator that immediately follows.
    right_separator = (
            '                ###################################################################################################################################################################################' + NL
            + '                ### Right #########################################################################################################################################################################' + NL
            + '                ###################################################################################################################################################################################'
    )

    ehof_anchor_old = (
            '                    effectButtonType = { name = "supermassive_ehof_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "giga_supermassive_ehof_disabled" }' + NL
            + '                    effectButtonType = { name = "supermassive_ehof_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } clicksound = interface effect = "giga_supermassive_ehof_enabled" }' + NL
            + '                }' + NL
            + NL
            + right_separator
    )
    ehof_anchor_new = (
            '                    effectButtonType = { name = "supermassive_ehof_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "giga_supermassive_ehof_disabled" }' + NL
            + '                    effectButtonType = { name = "supermassive_ehof_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } clicksound = interface effect = "giga_supermassive_ehof_enabled" }' + NL
            + '                }' + NL
            + new_left_blocks
            + right_separator
    )
    text = safe_replace(text, ehof_anchor_old, ehof_anchor_new,
                        'insert smbh_manipulator/core_mbrain/teraforge/quasarshipyard blocks')

    # ── Change 3 ─────────────────────────────────────────────────────────────
    # Insert quasarcraft_options block after the o_systemcraft_options closing
    # "}", before "effectButtonType { name = header_terraformers }".

    quasarcraft_block = (
            NL
            + '                ############################' + NL
            + '                ### quasarcraft ############' + NL
            + '                ############################' + NL
            + NL
            + '                containerWindowType = {' + NL
            + '                    name = "quasarcraft_options"' + NL
            + '                    position = { x = 450 y = -95 }' + NL
            + '                    size = { width = 410 height = 34 }' + NL
            + '                    orientation = upper_left' + NL
            + NL
            + '                    effectButtonType = {' + NL
            + '                        name = "background_o_systemcraft"' + NL
            + '                        spriteType = "GFX_giga_menu_button_bg"' + NL
            + '                        position = { x = 0 y = 0 }' + NL
            + '                        format = left' + NL
            + '                        no_clicksound = yes' + NL
            + '                        borderSize = { x = 10 y = 0 }' + NL
            + '                        font = "cg_16b"' + NL
            + '                        text = "giga_menu_name_quasarcraft"' + NL
            + '                        effect = "quasarmod_quasarcraft_tt"' + NL
            + '                    }' + NL
            + NL
            + '                    effectButtonType = { name = "quasarmod_quasarcraft_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "quasarmod_quasarcraft_enabled" }' + NL
            + '                    effectButtonType = { name = "quasarmod_quasarcraft_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } clicksound = interface effect = "quasarmod_quasarcraft_disabled" }' + NL
            + NL
            + '                }' + NL
            + NL
            + NL
    )

    # Anchor: unique close of o_systemcraft_options, then blank line, then
    # header_terraformers effectButtonType.
    osystemcraft_anchor_old = (
            '                    effectButtonType = { name = "stellar_manip_o_systemcraft_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "stellar_manip_o_systemcraft_enabled" }' + NL
            + '                    effectButtonType = { name = "stellar_manip_o_systemcraft_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } clicksound = interface effect = "stellar_manip_o_systemcraft_disabled" }' + NL
            + NL
            + '                }' + NL
            + NL
            + '                effectButtonType = {' + NL
            + '                    name = "header_terraformers"'
    )
    osystemcraft_anchor_new = (
            '                    effectButtonType = { name = "stellar_manip_o_systemcraft_enabled" spriteType = "GFX_giga_menu_enabled" position = { x = 380 y = 5 } no_clicksound = yes effect = "stellar_manip_o_systemcraft_enabled" }' + NL
            + '                    effectButtonType = { name = "stellar_manip_o_systemcraft_disabled" spriteType = "GFX_giga_menu_disabled" position = { x = 380 y = 5 } clicksound = interface effect = "stellar_manip_o_systemcraft_disabled" }' + NL
            + NL
            + '                }' + NL
            + quasarcraft_block
            + '                effectButtonType = {' + NL
            + '                    name = "header_terraformers"'
    )
    text = safe_replace(text, osystemcraft_anchor_old, osystemcraft_anchor_new,
                        'insert quasarcraft_options block')

    return text


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

# run this from the repo root
def main():
    hqm_ui = Path.cwd() / "Quasarmod-Indev" / "interface" / "zz_giga_gui_main_menu.gui"
    stellar_manip_ui = Path.cwd().parent / "Gigas-Stellar-Manipulation" / "Gigas-Stellar-Manipulation" / "interface" / "z_giga_gui_main_menu.gui"

    src = sys.argv[1] if len(sys.argv) > 1 else stellar_manip_ui
    dst = sys.argv[2] if len(sys.argv) > 2 else hqm_ui

    print(f"Reading source: {src}")
    with open(src, 'r', newline='', encoding='utf-8') as f:
        text = f.read()

    print("Converting leading tabs to spaces ...")
    text = convert_leading_tabs(text)

    print("Applying changes ...")
    text = apply_changes(text)

    print(f"Writing output: {dst}")
    with open(dst, 'w', newline='', encoding='utf-8') as f:
        f.write(text)

    print("Done.")


if __name__ == '__main__':
    main()