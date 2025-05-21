//! The build.rs file is necessary to unzip the rules.
//! rules.zip are needed so there is a way to get the rules dir into the build since you can't get it from the crate.
//!
//! Note: this only creates the Rules dir. Run build-addon.sh to actually build the NVDA addon.

use std::path::PathBuf;
use zip::ZipArchive;

fn main() {
    let archive = libmathcat::shim_filesystem::ZIPPED_RULE_FILES;
    let archive = std::io::Cursor::new(archive);
    let location = PathBuf::from("addon/globalPlugins/MathCAT");

    let mut zip_archive = ZipArchive::new(archive).unwrap();
    zip_archive.extract(&location).expect("Zip extraction failed");
}
