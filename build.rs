//! The build.rs file is necessary to unzip the rules.
//! rules.zip are needed so there is a way to get the rules dir into the build since you can't get it from the crate.
//!
//! Note: this only creates the Rules dir. Run build-addon.sh to actually build the addon.

use std::path::PathBuf;
use zip::ZipArchive;

fn main() {
    // first remove the Rules directory
    std::fs::remove_dir_all("NVDA-addon/addon/globalPlugins/MathCAT/Rules")
        .expect("Failed to remove directory 'NVDA-addon/addon/globalPlugins/MathCAT/Rules'");
    let archive = libmathcat::ZIPPED_RULE_FILES;
    let archive = std::io::Cursor::new(archive);
    let location = PathBuf::from("NVDA-addon/addon/globalPlugins/MathCAT");

    let mut zip_archive = ZipArchive::new(archive).unwrap();
    zip_archive.extract(&location).expect("Zip extraction failed");

    // the test dir 'zz' doesn't need to be part of the addon
    std::fs::remove_dir_all("NVDA-addon/addon/globalPlugins/MathCAT/Rules/zz")
        .expect("Failed to remove directory 'NVDA-addon/addon/globalPlugins/MathCAT/Rules/zz'");
}