Name:           icoutils
Version:        0.31.0
Release:        1%{?dist}
Summary:        Utility for extracting and converting Microsoft icon and cursor files

Group:          Applications/Multimedia
License:        GPLv3+
URL:            http://www.nongnu.org/icoutils/
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext 
BuildRequires:  libpng-devel
BuildRequires:  perl-Carp

Provides:       bundled(gnulib)

%description
The icoutils are a set of programs for extracting and converting images in
Microsoft Windows icon and cursor files. These files usually have the
extension .ico or .cur, but they can also be embedded in executables or
libraries.

%prep
%setup -q
autoreconf

for f in AUTHORS NEWS; do
  iconv -f ISO88592 -t UTF8 < $f > $f.utf8 && \
  touch -r $f $f.utf8 && \
  mv $f.utf8 $f 
done

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}


%files -f %{name}.lang
%doc README AUTHORS COPYING NEWS TODO ChangeLog
%{_bindir}/extresso
%{_bindir}/genresscript
%{_bindir}/icotool
%{_bindir}/wrestool
%{_mandir}/man1/*.1*


%changelog
* Mon Jun 17 2013 Martin Gieseking <martin.gieseking@uos.de> 0.31.0-1
- Updated to version 0.31.0.
- Dropped patches as they have been applied upstream.

* Thu May 16 2013 Richard W.M. Jones <rjones@redhat.com> 0.30.0-3
- Documentation fixes (RHBZ#948882).

* Sat Mar 23 2013 Martin Gieseking <martin.gieseking@uos.de> 0.30.0-2
- Rebuilt with recent autoconf for https://bugzilla.redhat.com/show_bug.cgi?id=925575

* Wed Mar 20 2013 Martin Gieseking <martin.gieseking@uos.de> 0.30.0-1
- updated to release 0.30.0
- dropped patch as it has been applied upstream
- removed old buildroot stuff

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Martin Gieseking <martin.gieseking@uos.de> 0.29.1-6
- added missing Provides: bundled(gnulib): https://bugzilla.redhat.com/show_bug.cgi?id=821764

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.29.1-4
- Rebuild for new libpng

* Mon May 16 2011 Martin Gieseking <martin.gieseking@uos.de> - 0.29.1-3
- fixed http://bugzilla.redhat.com/show_bug.cgi?id=701855
- minor spec cleanup

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Mar 20 2010 - Martin Gieseking <martin.gieseking@uos.de> - 0.29.1-1
- new upstream release fixes a segfault occurred in icotool
- fixed encoding of file AUTHORS

* Wed Feb 24 2010 - Martin Gieseking <martin.gieseking@uos.de> - 0.29.0-1
- updated to latest upstream release
- added newly available locales to package

* Mon Aug 17 2009 - Martin Gieseking <martin.gieseking@uos.de> - 0.28.0-1
- updated to latest upstream release
- changed license tag to GPLv3+

* Fri Aug 14 2009 - Martin Gieseking <martin.gieseking@uos.de> - 0.27.0-1
- updated to latest upstream release
- added missing BuildRequires
- patched wrestool/Makefile.am to fix ppc build failures

* Fri Apr 17 2009 - Eric Moret <eric.moret@gmail.com> - 0.26.0-1
- Initial spec
