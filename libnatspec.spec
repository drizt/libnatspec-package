Summary:	Library for national and language-specific issues
Name:		libnatspec
Version:	0.2.6
Release:	4%{?dist}

License:	LGPLv2
Group:		Development/Tools
Url:		http://sourceforge.net/projects/natspec
Source:		https://downloads.sourceforge.net/project/natspec/natspec/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	popt-devel
BuildRequires:	autoconf, automake, libtool


%description
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.
See detailed description at %url.


%package	devel
Summary:	Development package of library for national and language-specific issues
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing extensions for %{name}.


%prep
%setup -q

# Fix permissions
chmod 644 profile/*
find examples -type f -exec chmod 644 {} \;

pushd examples
iconv -f KOI8-R catpkt-1.0-alt-natspec.patch -t UTF-8 > catpkt-1.0-alt-natspec.patch.new
mv catpkt-1.0-alt-natspec.patch.new catpkt-1.0-alt-natspec.patch
popd

iconv -f KOI8-R -t UTF-8 ChangeLog > ChangeLog.new
mv ChangeLog.new ChangeLog

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS README ChangeLog NEWS TODO README-ru.html
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man1/*


%files devel
%defattr(-,root,root,-)
%doc examples profile
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*


%changelog
* Sat Oct 27 2012 Ivan Romanov <drizt@land.ru> - 0.2.6-4
- Fedora package
- Dropped unusual %%clean stage and rm in %%install stage
- Dropped BuildRoot
- Fixed make install
- Uses %%{_isa}
- profile and examplese moved to -devel subpackage
- Fixed group for main package
- added dos2unix to BR

* Sat Mar 19 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.6-2
- rebuilt

* Sat Feb  6 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.6-1
- initial build for Fedora
