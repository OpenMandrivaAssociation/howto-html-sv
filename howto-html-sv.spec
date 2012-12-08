%define DATE	20030112
%define    language  Swedish
%define    lang      sv
%define format1      html-%{lang}
%define format2      HTML/%{lang}

Summary:   %language HOWTO documents (html format) from the Linux Documentation Project
Name:      howto-%{format1}
Version:	9.1
Release:	%mkrel 8
Group:		Books/Howtos

Source0:   %name.tar

Url:		http://www.linuxdoc.org/docs.html#howto
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

BuildRequires: howto-utils
Requires:    locales-%lang xdg-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
untar_howtos; makehowtoindex %lang %language > index.html; cp -a * $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > %{buildroot}%_datadir/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Howto %language
Comment=HOWTO documents (html format) from the Linux Documentation Project in %language
Exec=xdg-open %_datadir/doc/HOWTO/HTML/%lang/index.html
Icon=documentation_section
Terminal=false
Type=Application
Categories=Documentation;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}
%{_datadir}/applications/*.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 9.1-7mdv2011.0
+ Revision: 665432
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 9.1-6mdv2011.0
+ Revision: 605875
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 9.1-5mdv2010.1
+ Revision: 520710
- rebuilt for 2010.1

* Fri Jul 04 2008 Oden Eriksson <oeriksson@mandriva.com> 9.1-4mdv2009.0
+ Revision: 231703
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 9.1-3mdv2008.1
+ Revision: 150273
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 9.1-2mdv2008.0
+ Revision: 89690
- rebuild

* Sun Sep 09 2007 Funda Wang <fwang@mandriva.org> 9.1-1mdv2008.0
+ Revision: 83354
- Rebuild for new era
- Import howto-html-sv



* Thu Jul 07 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.5mdk
- fix menu entry (#16637)

* Thu Feb 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.4mdk
- new menu scheme

* Thu Feb 13 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.3mdk
- synchronize all howtos spec files
- use new howto-utils

* Wed Feb 05 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.2mdk
- fix menu entry
- rebuild for latest makehowtoindex %%lang %%language > index.html)

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.1mdk
- new snapshot

* Thu Aug 01 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.0-0.1mdk
- new snapshot
- add real url
- sanitize menu entry (fix menu-command-not-in-package)

* Thu Jan 29 2002 Adrien DEMAREZ <ademarez@mandrakesoft.com> 8.2-2mdk
- updated howtos

* Thu Jan 17 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-1mdk
- Fix menu entry (icon)

* Fri Sep 07 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-2mdk
- Modified menu entry so that it works with KDE and gnome

* Thu Aug 30 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Automatically updated

* Tue Mar 13 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 8.0-1mdk
- bump release number
- fix tmppath
- build with new howto-utils
- add language name to rpm summary & index file

* Fri Mar  2 2001 Etienne Faure  <etienne@mandrakesoft.com> 7.1-6mdk
- rebuild with new howto-utils

* Sat Jan 13 2001 Etienne Faure  <etienne@mandrakesoft.com> 7.1-5mdk
- modified menu entry

* Fri Dec 15 2000 Etienne Faure  <etienne@mandraksoft.com> 7.1-4mdk
- updated howtos
- added icons

* Wed Aug 23 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.1-3mdk
- add LN touch
- BM
- use new tool to autogenerate the menu (which was previously handly built by
  dadou :-( )
- fix buildrequires & requires

* Mon Apr 24 2000 Pixel <pixel@mandrakesoft.com> 7.1-2mdk
- change require (add locales-XX, change netscape to webclient)

* Thu Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 7.1-1mdk
- 7.1

* Wed Apr 05 2000 David BAUDENS <baudens@mandrakesoft.com> 7.0-2mdk
- 20000405

* Fri Jan 07 2000 - David BAUDENS <baudens@mandrakesoft.com>
- Build for 7.0

* Tue Dec 30 1999 - David BAUDENS <baudens@mandrakesoft.com>
- French HTML version

* Sat Dec 04 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 19991204
- Keep only html format (others are in contribs)

* Fri May 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- no <BASE HREF...> in howto-index.html

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Jan 26 1999 Cristian Gafton <gafton@redhat.com>
- updated howtos
- marked translations with %%lang(XX)
- get rid of pdf, ps and dvi formats

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- added the Serbian Howtos

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- updated archive
- added croatian and slovenian subpackages

* Wed Apr 15 1998 Cristian Gafton <gafton@redhat.com>
- updated archive
- subpackages for each language

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- fixed missing HOWTOs because the download ran out of space
- added an index html page for the howto-html package

* Thu Oct 23 1997 Otto Hammersmith <otto@redhat.com>
- untarred the html tarballs to obsolete the ldp package

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed description for the right date

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Sat Apr 19 1997 Otto Hammersmith <otto@redhat.com>
- Updated to more recent HOWTOs.
- In the next major version, %%{_docdir} really ought to be cleaned out.
  Right now, the ldp and howto packages overlap somewhat. (HTML docs,
  the former, however, only has tar.gz files)
  I didn't want to rearrange too much for 4.2, and there are other
  documentation issues such as /usr/info.
