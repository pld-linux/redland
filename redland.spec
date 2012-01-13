#
# Conditional build:
%bcond_with	threestore	# with 3store
#
Summary:	Redland - a library that provides a high-level interface for RDF
Summary(pl.UTF-8):	Redland - biblioteka udostępniająca wysokopoziomowy interfejs do RDF
Name:		redland
Version:	1.0.15
Release:	2
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0
Group:		Libraries
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	b0deb87f3c7d3237a3d587c1e0f2f266
URL:		http://librdf.org/
%if %{with threestore}
BuildRequires:	3store-devel >= 2.0
BuildRequires:	3store-devel < 3.0
%endif
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.11
BuildRequires:	db-devel
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libltdl-devel
BuildRequires:	libraptor2-devel >= 2.0.4
BuildRequires:	libtool >= 2:2.0
BuildRequires:	mysql-devel >= 3.23.58
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	rasqal-devel >= 1:0.9.25
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	unixODBC-devel
Requires:	libraptor2 >= 2.0.4
Requires:	rasqal >= 1:0.9.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Redland is a library that provides a high-level interface for RDF
allowing the RDF graph to be parsed from XML, stored, queried and
manipulated. Redland implements each of the RDF concepts in its own
class via an object based API, reflected into the other language APIs:
Perl, Python, Tcl, Java and Ruby. Some of the classes providing the
parsers, storage mechanisms and other elements are built as modules
that can be added or removed as required.

%description -l pl.UTF-8
Redland to biblioteka udostępniająca wysokopoziomowy interfejs do RDF,
pozwalająca na analizę grafu RDF z XML-a, jego przechowywanie,
odpytywanie i obróbkę. Redland zawiera implementacje każdego pojęcia z
RDF w osobnej klasie poprzez obiekt oparty na API, mający
odzwierciedlenie w API dla innych języków: Perla, Pythona, Tcl-a, Javy
i Ruby'ego. Część klas udostępniających analizatory, mechanizmy
przechowywania i inne elementy jest zbudowana jako moduły, które mogą
być dodawane lub usuwane w razie potrzeby.

%package devel
Summary:	Headers for Redland RDF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Redland RDF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	db-devel
Requires:	libltdl-devel
Requires:	libraptor2-devel >= 2.0.4
Requires:	rasqal-devel >= 1:0.9.25

%description devel
Headers for Redland RDF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Redland RDF.

%package static
Summary:	Static Redland RDF library
Summary(pl.UTF-8):	Statyczna biblioteka Redland RDF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Redland RDF library.

%description static -l pl.UTF-8
Statyczna biblioteka Redland RDF.

%package storage-mysql
Summary:	MySQL storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie MySQL dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-mysql
MySQL storage plugin for Redland RDF library.

%description storage-mysql -l pl.UTF-8
Wtyczka przechowywania danych w bazie MySQL dla biblioteki Redland
RDF.

%package storage-postgresql
Summary:	PostgreSQL storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie PostgreSQL dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-postgresql
PostgreSQL storage plugin for Redland RDF library.

%description storage-postgresql -l pl.UTF-8
Wtyczka przechowywania danych w bazie PostgreSQL dla biblioteki
Redland RDF.

%package storage-sqlite
Summary:	SQLite storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie SQLite dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-sqlite
SQLite storage plugin for Redland RDF library.

%description storage-sqlite -l pl.UTF-8
Wtyczka przechowywania danych w bazie SQLite dla biblioteki Redland
RDF.

%package storage-tstore
Summary:	3store storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie 3store dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-tstore
3store storage plugin for Redland RDF library.

%description storage-tstore -l pl.UTF-8
Wtyczka przechowywania danych w bazie 3store dla biblioteki Redland
RDF.

%package storage-virtuoso
Summary:	virtuoso storage plugin for Redland RDF library
Summary(pl.UTF-8):	Wtyczka przechowywania danych w bazie virtuoso dla biblioteki Redland RDF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description storage-virtuoso
virtuoso storage plugin for Redland RDF library.

%description storage-virtuoso -l pl.UTF-8
Wtyczka przechowywania danych w bazie virtuoso dla biblioteki Redland
RDF.

%prep
%setup -q

sed -i 's,bdbc_prefix/lib$,bdbc_prefix/%{_lib},' configure.ac

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_lib_iodbc_SQLConnect=no \
	--disable-ltdl-install \
	--enable-modular \
	--with-html-dir=%{_gtkdocdir} \
	--with-odbc-inc=/usr/include \
	--with-odbc-lib=/usr/%{_lib} \
	--with-raptor=system \
	--with-rasqal=system \
	--with-threads \
	--with%{!?with_threestore:out}-threestore

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/redland/*.{la,a}

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
%attr(755,root,root) %ghost %{_libdir}/librdf.so.0
%dir %{_libdir}/redland
%dir %{_datadir}/redland
%{_datadir}/redland/mysql-v*.ttl
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
%{_datadir}/redland/Redland.i
%{_pkgconfigdir}/redland.pc
%{_mandir}/man1/redland-config.1*
%{_mandir}/man3/redland.3*
%{_gtkdocdir}/redland

%files static
%defattr(644,root,root,755)
%{_libdir}/librdf.a

%files storage-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_mysql.so

%files storage-postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_postgresql.so

%files storage-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_sqlite.so

%files storage-virtuoso
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_virtuoso.so

%if %{with threestore}
%files storage-tstore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/redland/librdf_storage_tstore.so
%endif
