APPNAME = "repository.beardypig.plugins"
VERSION = "1.1.0"
out = "build"


def configure(ctx):
    ctx.check_waf_version(mini='1.9.7')


def build(bld):
    bld(features="subst", source="addon.xml.in", target="addon.xml", APPNAME=APPNAME, VERSION=VERSION)
    for f in ('LICENSE', 'changelog.md', 'README.md'):
        bld(rule='cp ${SRC} ${TGT}', source=bld.path.make_node(f), target=bld.path.get_bld().make_node(f))


def dist(ctx):
    ctx.algo = "zip"
    ctx.base_path = ctx.path.make_node(out)
    ctx.base_name = APPNAME  # set the base directory for the archive
    ctx.arch_name = "{0}-{1}.{2}".format(APPNAME, VERSION, ctx.ext_algo.get(ctx.algo, ctx.algo))
    ctx.files = ctx.base_path.ant_glob("addon.xml changelog.md README.md LICENSE")
    ctx.files = ctx.path.ant_glob("build/addon.xml build/changelog.md build/README.md build/LICENSE")

