# TODO: various language support (java, perl, php, ruby, tcl)
Summary:	Redland - a library that provides a high-level interface for RDF
Summary(pl):	Redland - biblioteka udostêpniaj±ca wysokopoziomowy interfejs do RDF
Name:		redland
Version:	0.9.16
Release:	0.1
License:	LGPL v2 or MPL 1.1
Group:		Libraries
Source0:	http://www.redland.opensource.ac.uk/dist/source/%{name}-%{version}.tar.gz
# Source0-md5:	d78c768825df2727aec8336fe9772d8d
Patch0:		%{name}-system-raptor.patch
URL:		http://www.redland.opensource.ac.uk/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	db-devel
BuildRequires:	libraptor-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	mysql-devel >= 3.23.58
BuildRequires:	openssl-devel >= 0.9.7d
BUildRequires:	rpm-pythonprov
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
RDF w odobnej klasie poprzez obiekt oparty na API, maj±cy
odzwierciedlenie w API dla innych jêzyków: Perla, Pythona, Tcl-a, Javy
i Ruby'ego. Czê¶æ klas udostêpniaj±cych analizatory, mechanizmy
przechowywania i inne elementy jest zbudowana jako modu³y, które mog±
byæ dodawane lub usuwane w razie potrzeby.

%package devel
Summary:	Headers for Redland RDF library
Summary(pl):	Pliki nag³ówkowe biblioteki Redland RDF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	db-devel
Requires:	libraptor-devel >= 1.2.0
Requires:	mysql-devel >= 3.23.58

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

%package rapper
Summary:	Raptor RDF parser test program with Redland RDF support
Summary(pl):	Testowy program parsera Raptor RDF ze wsparciem dla Redland RDF
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description rapper
Raptor RDF parser test program with Redland RDF support.

%description rapper -l pl
Testowy program parsera Raptor RDF ze wsparciem dla Redland RDF.

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
cd raptor
%{__aclocal}
%{__autoconf}
%{__autoheader}
# don't use -f here
automake -a -c --foreign
cd ..
%configure \
	--with-raptor=system \
	--with-python

#	--with-java --with-jdk=/usr/lib/java  -- builds, but can be only optional
#	--with-perl  -- needs INSTALLDIRS=vendor in perl/Makefile.am
#	--with-ruby  -- missing install -d before installing *.so
#	--with-tcl  -- missing install -d before installing *.so
#	--with-php  -- cannot find config.h
#	--with-ecma-cli=mono  -- TODO

%{__make}

# build rapper with Redland/RDF support
%{__make} -C raptor

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C raptor \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQS.html LICENSE.html NEWS.html README.html RELEASE.html TODO.html
%attr(755,root,root) %{_bindir}/rdfproc
%attr(755,root,root) %{_bindir}/redland-db-upgrade
%attr(755,root,root) %{_libdir}/librdf.so.*.*.*
%{_mandir}/man1/rdfproc.1*
%{_mandir}/man1/redland-db-upgrade.1*

%files devel
%defattr(644,root,root,755)
%doc docs/{README.html,overview.png,api}
%attr(755,root,root) %{_bindir}/redland-config
%attr(755,root,root) %{_libdir}/librdf.so
%{_libdir}/librdf.la
%{_includedir}/librdf.h
%{_includedir}/rdf_*.h
%{_includedir}/redland.h
%{_pkgconfigdir}/redland.pc
%{_mandir}/man1/redland-config.1*
%{_mandir}/man3/redland.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/librdf.a

%files rapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rapper
%{_mandir}/man1/rapper.1*

%files -n python-redland
%defattr(644,root,root,755)
%{py_sitedir}/RDF.py
%attr(755,root,root) %{py_sitedir}/Redland.so
