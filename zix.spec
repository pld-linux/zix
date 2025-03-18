#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	Lightweight C library of portability wrappers and data structures
Summary(pl.UTF-8):	Lekka biblioteka C z funkcjami zgodności i strukturami danych
Name:		zix
Version:	0.6.2
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.xz
# Source0-md5:	a21f979f98d9185f5e72ba91df4a776a
URL:		http://drobilla.net/pages/software.html
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-sphinx_lv2_theme
BuildRequires:	sphinx-pdg >= 2
BuildRequires:	sphinxygen
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zix is a lightweight C library of portability wrappers and data
structures.

%description -l pl.UTF-8
Zix to lekka biblioteka C funkcji zgodności oraz struktur danych.

%package devel
Summary:	Header files for zix library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki zix
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for zix library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki zix.

%package apidocs
Summary:	API documentation for zix library
Summary(pl.UTF-8):	Dokumentacja API biblioteki zix
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for zix library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki zix.

%prep
%setup -q

%build
%meson \
	--default-library=shared \
	%{!?with_apidocs:-Ddocs=disabled} \
	-Dsinglehtml=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%attr(755,root,root) %{_libdir}/libzix-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzix-0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzix-0.so
%{_includedir}/zix-0
%{_pkgconfigdir}/zix-0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%dir %{_docdir}/zix-0
%{_docdir}/zix-0/html
%endif
