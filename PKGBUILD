# Maintainer: Fernando Celmer <email@fernandocelmer.com>

pkgname="linux-profile"
pkgver="1.0.19"
pkgrel=1
pkgdesc="🐧 Linux Profile Management CLI Tool"
arch=('any')
url="https://github.com/linux-profile/linux-profile"
license=('MIT')
depends=('python')
makedepends=('git' 'python-docutils' 'python-setuptools' 'python-packaging')
source=("$pkgname::https://github.com/linux-profile/$pkgname/archive/refs/tags/v$pkgver.tar.gz")
md5sums=('SKIP')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	./setup.py build
}

check() {
	cd "$srcdir/$pkgname-$pkgver"
	./setup.py test
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	./setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
