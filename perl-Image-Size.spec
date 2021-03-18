#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Image-Size
Version  : 3.300
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/Image-Size-3.300.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/Image-Size-3.300.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libimage-size-perl/libimage-size-perl_3.300-1.debian.tar.xz
Summary  : 'A library to extract height/width from images'
Group    : Development/Tools
License  : Artistic-1.0-Perl LGPL-2.1
Requires: perl-Image-Size-bin = %{version}-%{release}
Requires: perl-Image-Size-license = %{version}-%{release}
Requires: perl-Image-Size-man = %{version}-%{release}
Requires: perl-Image-Size-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Image::Size - Determine the size of images in several common formats
====================================================================

%package bin
Summary: bin components for the perl-Image-Size package.
Group: Binaries
Requires: perl-Image-Size-license = %{version}-%{release}

%description bin
bin components for the perl-Image-Size package.


%package dev
Summary: dev components for the perl-Image-Size package.
Group: Development
Requires: perl-Image-Size-bin = %{version}-%{release}
Provides: perl-Image-Size-devel = %{version}-%{release}
Requires: perl-Image-Size = %{version}-%{release}

%description dev
dev components for the perl-Image-Size package.


%package license
Summary: license components for the perl-Image-Size package.
Group: Default

%description license
license components for the perl-Image-Size package.


%package man
Summary: man components for the perl-Image-Size package.
Group: Default

%description man
man components for the perl-Image-Size package.


%package perl
Summary: perl components for the perl-Image-Size package.
Group: Default
Requires: perl-Image-Size = %{version}-%{release}

%description perl
perl components for the perl-Image-Size package.


%prep
%setup -q -n Image-Size-3.300
cd %{_builddir}
tar xf %{_sourcedir}/libimage-size-perl_3.300-1.debian.tar.xz
cd %{_builddir}/Image-Size-3.300
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Image-Size-3.300/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Image-Size
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Image-Size/dacd5d96ba4b6fd7caeb5be9d910b0a2377421a2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/imgsize

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Image::Size.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Image-Size/dacd5d96ba4b6fd7caeb5be9d910b0a2377421a2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/imgsize.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Image/Size.pm
