from tests.spellbook import TARBALL_NAME, git_add_and_commit, build_srpm
        " - 0.1.0-1\n"
        "+- new upstream release: 0.1.0\n"
        "+\n"
        " * Sun Feb 24 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.0.0-1\n"
        " - No brewing, yet.\n" in git_diff
    srpm_path = list(sg_path.glob("beer-0.1.0-2.*.src.rpm"))[0]
    assert srpm_path.is_file()
    build_srpm(srpm_path)