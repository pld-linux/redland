Summary:	-
Summary(pl):	-
Name:		redland
Version:	0.9.12
Release:	-
Epoch:		-
License:	LGPL v2 or MPL 1.1
Group:		-
Source0:	http://www.redland.opensource.ac.uk/dist/source/%{name}-%{version}.tar.gz
URL:		http://www.redland.opensource.ac.uk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
