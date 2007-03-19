#
# Conditional build:
%bcond_with	threestore	# with 3store
#
Summary:	Redland - a library that provides a high-level interface for RDF
Summary(pl):	Redland - biblioteka udostêpniaj±ca wysokopoziomowy interfejs do RDF
Name:		redland
Version:	1.0.5
Release:	1
License:	LGPL v2.1+ or GPL v2+ or Apache v2
Group:		Libraries
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	43d909ff6ffa7f7559ad9af5620c8cbf
Patch0:		%{name}-link.patch
URL:		http://librdf.org/
%if %{with threestore}
BuildRequires:	3store-devel >= 2.0
BuildRequires:	3store-devel < 3.0
%endif
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	db-devel
BuildRequires:	libraptor-devel >= 1.4.13
BuildRequires:	libtool
BuildRequires:	mysql-devel >= 3.23.58
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	rasqal-devel >= 1:0.9.13
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	sqlite3-devel >= 3
Requires:	libraptor >= 1.4.13
Requires:	rasqal >= 1:0.9.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redland is a library that provides a high-level interface for RDF
allowing the RDF graph to be parsed from XML, stored, queried and
manipulated. Redland implements each of the RDF concepts in its own
class via an object based API, reflected into the other language APIs:
Perl, Python, Tcl, Java and Ruby. Some of the classes providing the
parsers, storage mechanisms and other elements are built as modules
that can be added or removed as required.

%description -l pl
Redland to biblioteka udostêpniaj±ca wysokopoziomowy interfejs do RDF,
pozwalaj±ca na analizê grafu RDF z XML-a, jego przechowywanie,
odpytywanie i obróbkê. Redland zawiera implementacje ka¿dego pojêcia z
RDF w osobnej klasie poprzez obiekt oparty na API, maj±cy
odzwierciedlenie w API dla innych jêzyków: Perla, Pythona, Tcl-a, Javy
i Ruby'ego. Czê¶æ klas udostêpniaj±cych analizatory, mechanizmy
przechowywania i inne elementy jest zbudowana jako modu³y, które mog±
byæ dodawane lub usuwane w razie potrzeby.

%package devel
Summary:	Headers for Redland RDF library
Summary(pl):	Pliki nag³ówkowe biblioteki Redland RDF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with threestore}
Requires:	3store-devel >= 2.0
Requires:	3store-devel < 3.0
%endif
Requires:	db-devel
Requires:	libraptor-devel >= 1.4.13
Requires:	mysql-devel >= 3.23.58
Requires:	postgresql-devel
Requires:	rasqal-devel >= 1:0.9.13
Requires:	sqlite3-devel >= 3

%description devel
Headers for Redland RDF library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Redland RDF.

%package static
Summary:	Static Redland RDF library
Summary(pl):	Statyczna biblioteka Redland RDF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Redland RDF library.

%description static -l pl
Statyczna biblioteka Redland RDF.

%package -n python-redland
Summary:	Python bindings for Redland RDF library
Summary(pl):	Pythonowy interfejs do biblioteki Redland RDF
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python

%description -n python-redland
Python bindings for Redland RDF library

%description -n python-redland -l pl
Pythonowy interfejs do biblioteki Redland RDF

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-threestore=%{!?with_threestore:no}%{?with_threestore:yes} \
	--with-raptor=system \
	--with-rasqal=system

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* FAQS.html LICENSE.html NEWS.html README.html RELEASE.html TODO.html
%attr(755,root,root) %{_bindir}/rdfproc
%attr(755,root,root) %{_bindir}/redland-db-upgrade
%attr(755,root,root) %{_libdir}/librdf.so.*.*.*
%{_mandir}/man1/rdfproc.1*
%{_mandir}/man1/redland-db-upgrade.1*

%files devel
%defattr(644,root,root,755)
%doc docs/{README.html,storage.html}
%attr(755,root,root) %{_bindir}/redland-config
%attr(755,root,root) %{_libdir}/librdf.so
%{_libdir}/librdf.la
%{_includedir}/librdf.h
%{_includedir}/rdf_*.h
%{_includedir}/redland.h
%dir %{_datadir}/redland
%{_datadir}/redland/Redland.i
%{_pkgconfigdir}/redland.pc
%{_mandir}/man1/redland-config.1*
%{_mandir}/man3/redland.3*
%{_gtkdocdir}/redland

%files static
%defattr(644,root,root,755)
%{_libdir}/librdf.a
