%define svn	3218
%define rel	4
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define dirname		%name
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.bz2
%define dirname		%name-%version
%endif

Name: 	 	libopensync-plugin-google-calendar
Version: 	0.22.1
Epoch:		1
Release: 	%{release}
Summary: 	OpenSync plugin for Google Calendar
License:	GPLv2+
Group:		Office
URL:		http://www.opensync.org
# For SVN:
# svn co http://svn.opensync.org/branches/branch-0.2X/plugins/google-calendar libopensync-plugin-google-calendar
Source0:	http://www.opensync.org/download/releases/%{distname}
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	python-httplib2
Requires:	python-httplib2
Requires:	python-pyxml
Requires:	libopensync >= %{epoch}:0.22
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise with Google
Calendar.

%prep
%setup -q -n %{dirname}

%build
%if %svn
autoreconf -i
%endif
# google-cal-helper is installed to libexecdir, we don't want it just
# in /usr/lib... - AdamW 2008/03
%configure2_5x --libexecdir=%{_libdir}/opensync
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
%{_libdir}/opensync/google-cal-helper



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.22.1-0.3218.4mdv2011.0
+ Revision: 620171
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1:0.22.1-0.3218.3mdv2010.0
+ Revision: 429819
- rebuild

* Mon Sep 01 2008 Austin Acton <austin@mandriva.org> 1:0.22.1-0.3218.2mdv2009.0
+ Revision: 278713
- requires python-pyxml

* Thu Mar 13 2008 Adam Williamson <awilliamson@mandriva.org> 1:0.22.1-0.3218.1mdv2008.1
+ Revision: 187331
- buildrequires python-httplib2
- some cleanups
- revert to 0.22 based on latest 0.22 spec in SVN: use upstream SVN snapshot from 0.2 branch as it has stable important fixes since 0.22 release

* Wed Mar 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.36-2mdv2008.1
+ Revision: 186996
- requires python-httplib2

* Thu Feb 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2008.1
+ Revision: 175986
- import libopensync-plugin-google-calendar


* Thu Feb 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2008.1
- first mdv release 
